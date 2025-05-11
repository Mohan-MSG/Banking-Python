from transaction import Transactions
from admin import Admin_User
from user import User
from models import Session, User as UserModel

import random
import time
import re

def create_acc():
    session = Session()
    while True:
        phone = input("Enter the Phone Number (10 digits): ").lstrip("0")
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Invalid phone number. Please enter a 10-digit number.")
    
    existing_user = session.query(UserModel).filter_by(phone=phone).first()
    if existing_user:
        print("This phone number is already associated with an account. Please log in.")
        session.close()
        login()
        return

    existing_ids = {user.id for user in session.query(UserModel).all()}
    temp = random.randint(10000000, 99999999)
    while temp in existing_ids:
        temp = random.randint(10000000, 99999999)

    uname = input("Enter the Username: ").capitalize()
    password = input("Enter the Password: ")
    
    uname_pattern = r'^[A-Za-z\s]{5,10}+$'
    password_pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    while not re.match(password_pattern, password) or not re.match(uname_pattern, uname):
        print("Password must be at least 8 characters long and contain at least one uppercase letter, one digit, and one special character.")
        print("Username must be between 5 and 10 characters long and contain only letters and spaces.")
        uname = input("Enter the Username: ").capitalize()
        password = input("Enter the Password: ")

    new_user = UserModel(
        id=temp,
        username=uname,
        phone=phone,
        password=password,
        total_balance=0
    )

    print("Creating Account...")
    time.sleep(1)
    print("Please wait...")
    time.sleep(3)

    session.add(new_user)
    session.commit()
    session.close()

    print("Account Created Successfully")
    print("User ID:", temp)

def login():
    uid = input("Enter the User ID: ")

    if uid == "admin":
        password = input("Enter the Password: ")
        if password == "admin":
            Admin_User.admin()
            return

    session = Session()
    user = session.query(UserModel).filter_by(id=int(uid)).first()
    session.close()

    if user:
        password = input("Enter the Password: ")
        if user.password == password:
            print("Login Successful")
            time.sleep(1)
            print("Loading...")
            time.sleep(2)
            Transactions(int(uid))
        else:
            print("Invalid Password")
    else:
        print("Invalid User ID. Please Create an Account")
        create_acc()

if __name__ == "__main__":
    login()