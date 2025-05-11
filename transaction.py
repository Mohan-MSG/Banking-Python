from models import Session, User, Transaction as TransactionModel
import time

class Transactions:

    def __init__(self, user_id):
        """Initialize the Transactions class."""
        self.user_id = user_id
        self.session = Session()
        value = 0
        while value != 4:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. Exit")
            value = int(input("Enter the value: "))
            if value == 1:
                self.deposit()
            elif value == 2:
                self.withdraw()
            elif value == 3:
                self.balance()
            elif value == 4:
                self.session.close()
                break
            else:
                print("Invalid value")

    def deposit(self):
        """Handles the deposit operation."""
        user = self.session.query(User).filter_by(id=self.user_id).first()
        if user is None:
            print("User ID not found.")
            return

        try:
            amount = float(input("Enter the Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return
        
        user.total_balance += amount
        transaction = TransactionModel(user_id=self.user_id, type="deposit", amount=amount)
        self.session.add(transaction)
        self.session.commit()
        print("Deposit successful. New balance:", user.total_balance)

    def withdraw(self):
        """Handles the withdrawal operation."""
        user = self.session.query(User).filter_by(id=self.user_id).first()
        if user is None:
            print("User ID not found.")
            return

        try:
            amount = float(input("Enter the Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
            elif amount > user.total_balance:
                print("Insufficient balance.")
                return
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return
        
        user.total_balance -= amount
        transaction = TransactionModel(user_id=self.user_id, type="withdraw", amount=amount)
        self.session.add(transaction)
        self.session.commit()
        print("Withdrawal successful. New balance:", user.total_balance)

    def balance(self):
        """Displays the balance of the user."""
        print("1. View Balance")
        print("2. Transaction History")
        print("3. Back")
        value = int(input("Enter the value: "))
        if value == 1:
            self.view_balance()
        elif value == 2:
            self.transaction_history()
        elif value == 3:
            return
    
    def view_balance(self):
        """Displays the current balance."""
        user = self.session.query(User).filter_by(id=self.user_id).first()
        if user is None:
            print("User ID not found.")
            return
        
        print("Current Balance:", user.total_balance)
        time.sleep(1)
        
    
    def transaction_history(self):
        transactions = self.session.query(TransactionModel).filter_by(user_id=self.user_id).all()
        if not transactions:
            print("No transaction history found.")
            return
        
        time.sleep(1)
        print("Loading Transaction History...")
        time.sleep(2)
        
        for transaction in transactions:
            print(f"Type: {transaction.type}")
            print(f"Amount: {transaction.amount}")
            print(f"Timestamp: {transaction.timestamp}")
            print("-" * 30)
        time.sleep(2)
