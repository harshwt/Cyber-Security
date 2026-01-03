import hashlib, os, hmac
import tkinter as tk

users = {}

def register():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        lbl_result.config(text="Username and password required!")
        return

    if username in users:
        lbl_result.config(text="User already exists!")
        return

    salt = os.urandom(16)
    hash_pwd = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100_000
    )

    users[username] = {"salt": salt, "hash": hash_pwd}
    lbl_result.config(text=f"User {username} registered successfully!")

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username not in users:
        lbl_result.config(text="User not found!")
        return

    salt = users[username]["salt"]
    stored_hash = users[username]["hash"]

    new_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100_000
    )

    if hmac.compare_digest(new_hash, stored_hash):
        lbl_result.config(text="Login successful!")
    else:
        lbl_result.config(text="Invalid password!")

# GUI setup
root = tk.Tk()
root.title("Mini User Database System")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=5, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

btn_register = tk.Button(root, text="Register", command=register)
btn_register.grid(row=2, column=0, padx=20, pady=20)

btn_login = tk.Button(root, text="Login", command=login)
btn_login.grid(row=2, column=1, padx=20, pady=20)

lbl_result = tk.Label(root, text="")
lbl_result.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
