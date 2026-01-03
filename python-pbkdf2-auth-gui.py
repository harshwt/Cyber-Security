'''
Secure Authentication System (PBKDF2-HMAC)
=======================================

Description
-----------
This project is a simple Python-based authentication system with a graphical
user interface (GUI) built using Tkinter. It demonstrates secure password
storage using salted hashing with PBKDF2-HMAC (SHA-256).

The goal of this project is educational: to learn and demonstrate secure
password handling practices and basic authentication logic.


Features
--------
- User registration and login
- Secure password hashing using PBKDF2-HMAC (SHA-256)
- Unique random salt per user
- Protection against rainbow table attacks
- Simple Tkinter GUI
- In-memory user storage (no plaintext passwords)


Technologies Used
-----------------
- Python 3
- hashlib (PBKDF2-HMAC)
- os.urandom (cryptographically secure salt)
- hmac.compare_digest (safe hash comparison)
- Tkinter (GUI)


How It Works
------------
1. During registration:
   - A random 16-byte salt is generated
   - The password is hashed using PBKDF2-HMAC with SHA-256
   - The salt and hash are stored for the user

2. During login:
   - The stored salt is retrieved
   - The entered password is hashed again using the same parameters
   - The new hash is compared with the stored hash securely


Security Notes
--------------
- Passwords are never stored in plaintext
- Each user has a unique salt
- PBKDF2 makes brute-force attacks significantly slower
- This project is for learning purposes and is not production-ready


Limitations
-----------
- Users are stored in memory only (data is lost when the program closes)
- No account lockout or rate limiting
- No persistent database
- GUI is minimal by design


How to Run
----------
1. Make sure Python 3 is installed
2. Clone the repository
3. Run the script:

   python main.py

4. Use the GUI to register and log in users


Learning Goals
--------------
- Understand secure password hashing
- Learn how salts protect against precomputed attacks
- Practice using PBKDF2-HMAC in Python
- Combine security logic with a GUI
- Build a foundation for further security and reverse engineering studies


Future Improvements
-------------------
- Persistent storage (SQLite or JSON)
- Argon2 or bcrypt support
- Login attempt limits
- Password strength checks
- Export as a reverse engineering or CTF challenge

Author
------
Harshwardhan Tiwari

'''
# Code below... 

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

