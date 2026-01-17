# ============================================
# Password Hashing and Verification System
# Python Security Project
# ============================================

import hashlib
import getpass

# -------------------------------
# HASH PASSWORD FUNCTION
# -------------------------------
def hash_password(password):
    """
    Converts plain password into SHA-256 hash
    """
    return hashlib.sha256(password.encode()).hexdigest()


# -------------------------------
# VERIFY PASSWORD FUNCTION
# -------------------------------
def verify_password(stored_hash, entered_password):
    """
    Compares stored hash with hash of entered password
    """
    entered_hash = hash_password(entered_password)
    return stored_hash == entered_hash


# -------------------------------
# USER REGISTRATION
# -------------------------------
def register_user():
    print("\n--- USER REGISTRATION ---")
    
    username = input("Enter username: ")
    password = getpass.getpass("Create password: ")

    hashed_password = hash_password(password)

    print("\n✅ Registration Successful")
    print("Username:", username)
    print("Stored Hashed Password:", hashed_password)

    return username, hashed_password


# -------------------------------
# USER LOGIN
# -------------------------------
def login_user(stored_username, stored_hash):
    print("\n--- USER LOGIN ---")

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if username == stored_username and verify_password(stored_hash, password):
        print("\n✅ Login Successful")
    else:
        print("\n❌ Login Failed (Invalid Credentials)")


# -------------------------------
# MAIN PROGRAM
# -------------------------------
def main():
    print("========================================")
    print(" Password Hashing & Verification System ")
    print("========================================")

    stored_username = ""
    stored_hash = ""

    while True:
        print("\n1. Register User")
        print("2. Login User")
        print("3. Exit")

        choice = input("Choose option (1/2/3): ")

        if choice == "1":
            stored_username, stored_hash = register_user()

        elif choice == "2":
            if stored_hash == "":
                print("\n⚠ Please register first!")
            else:
                login_user(stored_username, stored_hash)

        elif choice == "3":
            print("\nExiting Program...")
            break

        else:
            print("\n❌ Invalid Choice")


# Run Program
main()
