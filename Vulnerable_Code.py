import hashlib
import os
import pickle
import sqlite3
import subprocess

# Hardcoded credentials
PASSWORD = "admin123"
API_KEY = "sk_live_1234567890"

conn = sqlite3.connect("users.db")


def authenticate(username, password):
    # SQL Injection
    query = (
        "SELECT * FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )

    cursor = conn.cursor()
    cursor.execute(query)

    return cursor.fetchone()


def calculate_md5(password):
    # Weak hash
    return hashlib.md5(password.encode()).hexdigest()


def list_directory(path):
    # Command Injection + insecure subprocess call
    subprocess.call("ls " + path, shell=True)


def load_user(filename):
    # Unsafe deserialization
    with open(filename, "rb") as f:
        return pickle.load(f)

def duplicated_logic(a, b):
    if a > b:
        return a - b
    else:
        return b - a


def duplicated_logic2(a, b):
    if a > b:
        return a - b
    else:
        return b - a


def insecure_temp_file(data):
    with open("/tmp/output.txt", "w") as f:
        f.write(data)


if __name__ == "__main__":
    user = input("Username: ")
    password = input("Password: ")

    print(authenticate(user, password))

    directory = input("Directory: ")
    list_directory(directory)

    print(calculate_md5(password))