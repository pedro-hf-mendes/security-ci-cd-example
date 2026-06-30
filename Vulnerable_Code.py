import hashlib
import pickle
import sqlite3
import subprocess


conn = sqlite3.connect("users.db")


def authenticate():
    username = input("Username: ")
    password = input("Password: ")

    #
    # SQL Injection
    #
    query = (
        "SELECT * FROM users "
        "WHERE username='"
        + username
        + "' AND password='"
        + password
        + "'"
    )

    cursor = conn.cursor()
    cursor.execute(query)

    return cursor.fetchall()


def execute_command():
    command = input("Command: ")

    #
    # Command Injection
    #
    subprocess.run(command, shell=True)


def deserialize():
    filename = input("File: ")

    #
    # Unsafe deserialization
    #
    with open(filename, "rb") as f:
        data = pickle.loads(f.read())

    return data


def hash_password():
    password = input("Password: ")

    #
    # Weak cryptography
    #
    return hashlib.md5(password.encode()).hexdigest()


def calculator():
    expression = input("Expression: ")

    #
    # Arbitrary code execution
    #
    return eval(expression)


if __name__ == "__main__":
    authenticate()
    execute_command()
    deserialize()
    hash_password()
    calculator()