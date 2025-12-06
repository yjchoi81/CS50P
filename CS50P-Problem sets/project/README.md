# Welcon to CS50P Bank

#### Video Demo:  [https://youtu.be/jFdALRUW6gw]

#### Description:
This project allows users to open a bank account and records deposits, withdrawals, and balances into a CSV file.
The goal of this project is to implement a program that allows bank customers to select service numbers from a menu and perform banking tasks—such as opening an account, depositing, withdrawing, checking balances, and viewing transaction history—conveniently from anywhere, without visiting a physical bank.

<img width="317" height="388" alt="image" src="https://github.com/user-attachments/assets/2e36e525-e15e-4f97-9a42-fd157a435f57" />

## Project Structure

### project.py
This file implements the core functionality of the Bank system. It handles user input to process major transactions such as balance inquiries, deposits, and withdrawals, and manages/saves account data via CSV files.

### test_project.py
This file contains unit tests for all major functions in `project.py`. In particular, it focuses on verifying user input validation logic, such as ensuring only positive amounts are allowed for deposits and preventing withdrawals that exceed the balance.

### requirements.txt
A file listing the names and versions of all external Python libraries required to run this project.

### README.md
Explains the project introduction, installation instructions, main features, and usage.

## Functioning

### main()
Displays the menu options available to the customer and prompts them to select a service number. If a customer with the same name exists, it calls the `load_balance(name)` function to retrieve the transaction history saved in the CSV file. It then calls the appropriate function based on the service number selected by the customer.
If the customer selects service menu "0. Exit", the program terminates via `sys.exit()`.

### get_account()
When the customer selects service menu "1. New Account", this function generates a new 12-digit bank account number.
The created account consists of a format: `3 digits` - `2 digits` - `7 digits`.

### create_transaction_file(name)
Executed along with `get_account()` when the customer selects service menu "1. New Account". It creates a CSV file named after the customer (`{name}'s Transaction File.csv`).
The CSV file is created with the headers "Time", "Type", "Amount", and "Current Balance".

### deposit(balance, amount)
Provides deposit functionality when the customer selects service menu "2. Deposit".
If `amount` is negative, it prints "Invalid amount to deposit".
If a previous balance existed, it adds `amount` to `balance`; otherwise, it adds `amount` to 0.

### withdraw(balance, amount)
Provides withdrawal functionality when the customer selects service menu "3. Withdraw".
If `amount` is negative, it prints "Invalid amount to withdraw".
If `amount` is greater than `balance`, it prints "The Amount is not available to withdraw." along with the customer's current balance.

### record_transaction(name, balance, transaction_type, amount)
When the customer selects service menu 2 or 3 and a transaction is successfully completed (i.e., `balance` changes), this function is called to load the CSV file and append the transaction record.
It uses `datetime.datetime.now()` to record the date and time of the transaction.
The data is recorded in the CSV file in the order of: Time, `transaction_type`, `amount`, and `balance`.
It also prints the completed transaction details to the customer in the order of `transaction_type`, `amount`, and `balance`.

### display_account_history(name)
When the customer selects service menu "4. Transaction History", this function reads the records currently saved in the CSV file and prints them to the screen.

### current_balance(balance)
When the customer selects service menu "5. Current Balance", this function prints the current balance.

### load_balance(name)
A function that restores the balance by reading the last line of the file when the program starts.
It checks if the customer's file exists, and if so, retrieves the last transaction record.
If the file exists but only contains headers, or if the file does not exist, it returns 0, setting the `balance` to 0.

## TODO:
### Download
Download the Repository through Clone Repository or Download Zip

[https://github.com/code50/216629534/tree/main/project]

### Installation
After download, go to cmd and navigate to the project folder directory.

cd project

### Use pip to install needed libraries.

$ pip install -r requirements.txt

### Usage
Run the program python script project.py with python.

python project.py

Test the program python script test_project.py with pytest.

pytest test_project.py


## Note

The program is case-insensitive.

## Important

When writing your Full Name, please leave a space between your first and last name.
