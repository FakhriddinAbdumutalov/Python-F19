class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: ${self.balance:.2f}"
    def check_balance(self):
        return self.balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    def transfer(self, target_account, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred ${amount:.2f} to Account {target_account.account_number}.")
        else:
            print("Transfer failed. Check amount or balance.")
class Bank:
    def __init__(self):
        self.accounts = {}
    def add_account(self, account_number, account_holder, initial_balance=0):
        if account_number not in self.accounts:
            new_account = Account(account_number, account_holder, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account {account_number} created for {account_holder}.")
        else:
            print(f"Account {account_number} already exists.")
    def get_account(self, account_number):
        return self.accounts.get(account_number, None)
    def list_all_accounts(self):
        if self.accounts:
            for account in self.accounts.values():
                print(account)
        else:
            print("No accounts available.")
    def handle_account_operations(self):
        while True:
            print("\nBanking System")
            print("1. Add Account")
            print("2. Check Balance")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Transfer Money")
            print("6. List All Accounts")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                account_number = input("Enter account number: ")
                account_holder = input("Enter account holder name: ")
                initial_balance = float(input("Enter initial balance (default 0): ") or 0)
                self.add_account(account_number, account_holder, initial_balance)
            elif choice == "2":
                account_number = input("Enter account number: ")
                account = self.get_account(account_number)
                if account:
                    print(f"Balance for Account {account_number}: ${account.check_balance():.2f}")
                else:
                    print(f"Account {account_number} not found.")
            elif choice == "3":
                account_number = input("Enter account number: ")
                account = self.get_account(account_number)
                if account:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                else:
                    print(f"Account {account_number} not found.")
            elif choice == "4":
                account_number = input("Enter account number: ")
                account = self.get_account(account_number)
                if account:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                else:
                    print(f"Account {account_number} not found.")
            elif choice == "5":
                account_number = input("Enter your account number: ")
                account = self.get_account(account_number)
                if account:
                    target_account_number = input("Enter target account number: ")
                    target_account = self.get_account(target_account_number)
                    if target_account:
                        amount = float(input("Enter transfer amount: "))
                        account.transfer(target_account, amount)
                    else:
                        print(f"Target account {target_account_number} not found.")
                else:
                    print(f"Account {account_number} not found.")
            elif choice == "6":
                self.list_all_accounts()
            elif choice == "7":
                print("Exiting the banking system.")
                break
            else:
                print("Invalid choice. Please try again.")
def main():
    bank = Bank()
    bank.handle_account_operations()
if __name__ == "__main__":
    main()
