import random
import sys
import csv
import datetime
import os

def main():
    print("="*40)
    print("Welcome to CS50P Bank!")
    print("="*40)

    name_input = input("Full Name: ").title()

    # 프로그램 시작 시 파일에서 마지막 잔액 불러오기
    balance = load_balance(name_input)

    print()
    print("="*40)
    print("Service Menu")
    print("="*40)
    print("1. New Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Current Balance")
    print("0. Exit")
    print("="*40)

    while True:
        try:
            service = int(input("Select service number: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 5.")
            continue

        if service == 1:
            account_num = get_account()
            create_transaction_file(name_input)
            balance = 0
            print(f"Your Account Number: {account_num}")

        elif service == 2:
            try:
                amount = int(input("Deposit Amount in KOR: ₩"))
            except ValueError:
                print("Invalid amount")
                continue

            # [수정] 잔액이 변했는지 확인하는 로직 추가
            new_balance = deposit(balance, amount)

            if new_balance != balance:
                balance = new_balance
                record_transaction(name_input, balance, "Deposit", amount)
            # 잔액이 변하지 않았다면(금액 오류 등) 기록하지 않음

        elif service == 3:
            try:
                amount = int(input("Withdrawal Amount in KOR: ₩ "))
            except ValueError:
                print("Invalid amount")
                continue

            # [수정] 잔액이 변했는지 확인 (출금 실패시 기록 안 하기 위함)
            new_balance = withdraw(balance, amount)

            if new_balance != balance:
                balance = new_balance
                record_transaction(name_input, balance, "Withdrawal", amount)
            else:
                # withdraw 함수 내부에서 에러 메시지를 출력하므로 여기선 pass
                pass

        elif service == 4:
            display_account_history(name_input)

        elif service == 5:
            current_balance(balance)

        elif service == 0:
            print("Exit service! Thank you for using CS50P Bank.")
            sys.exit()

# ---------------- Functions ----------------

def get_account():
    part1 = random.randint(0, 999)
    part2 = random.randint(0, 99)
    part3 = random.randint(1000000, 9999999)
    return f"{part1:03}-{part2:02}-{part3}"


def create_transaction_file(name):
    """새로운 계좌 파일을 생성합니다 (덮어쓰기 방지)."""
    file_name = f"{name}'s Transaction File.csv"

    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file, delimiter='|') # 파이프 구분자
            writer.writerow(["Time", "Type", "Amount", "Current Balance"])
        print(f"Your Bank Account successfully opened and '{file_name}' created.")
    else:
        print(f"Account file for {name} already exists.")


def deposit(balance, amount):
    if amount <= 0:
        print("Invalid amount to deposit")
        return balance
    return balance + amount


def withdraw(balance, amount):
    if amount <= 0:
        print("Invalid amount to withdraw")
        return balance
    elif amount > balance:
        print("The Amount is not available to withdraw.")
        print(f"Your balance is ₩{balance:,}")
        return balance # [중요] 잔액 부족 시 원래 잔액 그대로 리턴
    return balance - amount


def record_transaction(name, balance, transaction_type, amount):
    """
    [구 transaction_history]
    거래가 성사되었을 때만 호출되어 파일에 기록을 남기는 함수입니다.
    """
    file_name = f"{name}'s Transaction File.csv"

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_amount = f"₩ {amount:,}"
    formatted_balance = f"₩ {balance:,}"

    transaction_data = [
        now, transaction_type, formatted_amount, formatted_balance
    ]

    # 파일이 존재하는지 확인 (없으면 생성)
    file_exists = os.path.exists(file_name)
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file, delimiter='|') # 파이프 구분자
        if not file_exists:
             writer.writerow(["Time", "Type", "Amount", "Current Balance"])
        writer.writerow(transaction_data)

    print("-" * 40)
    print(f"Transaction recorded: {transaction_type} {formatted_amount}. New balance: {formatted_balance}")
    print("-" * 40)


def current_balance(balance):
    print(f"Current Balance: ₩ {balance:,}")


def display_account_history(name):
    """
    [구 account_history]
    저장된 파일을 읽어서 화면에 보여주는 함수입니다.
    """
    file_name = f"{name}'s Transaction File.csv"

    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file, delimiter='|') # 파이프 구분자
            rows = list(reader)
            print(f"Transaction History for {name}")
            print(f"| {'Time':20} | {'Type':15} | {'Amount':10} | {'Current Balance':15} |")
            print("-" * 72)

            for row in rows:
                if row[0] == "Time": continue
                # 파이프로 깔끔하게 나누어진 데이터를 출력
                print(f"| {row[0]:20} | {row[1]:15} | {row[2]:10} | {row[3]:15} |")

    except FileNotFoundError:
        print(f"Transaction history file not found.")


def load_balance(name):
    """
    프로그램 시작 시, 파일의 마지막 줄을 읽어 잔액을 복구하는 함수입니다.
    """
    file_name = f"{name}'s Transaction File.csv"
    current_balance = 0

    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file, delimiter='|') # 파이프 구분자
            rows = list(reader)

            if len(rows) <= 1:
                return 0

            last_transaction = rows[-1]
            balance_str = last_transaction[3].replace('₩', '').replace(',', '').strip()
            current_balance = int(balance_str)

    except (FileNotFoundError, IndexError, ValueError):
        # 파일이 없으면 그냥 0원으로 시작 (안내 메시지 생략 가능)
        return 0

    return current_balance


if __name__ == "__main__":
    main()

"""
import random
import sys
import csv
import datetime

name = None
balance = 0

def main():
    global name
    print("="*40)
    print("Welcom to CS50P Bank!")
    print("="*40)
    name = input("Full Name: ").title()
    load_balance()

    print()
    print("="*40)
    print("Service Menu")
    print("="*40)
    print("1. New Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Current Balance")
    print("0. Exit")
    print("="*40)

    while True:
        try:
            service = int(input("Select service number: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 5.")
            continue

        if service == 1 :
            account_num = get_account()
            create_transaction_file(name)
            print(f"Your Account Number: {account_num}")

        elif service == 2 :
            try:
                deposit_amount = int(input("Deposit Amount in KOR: ₩"))
            except ValueError:
                print("Invalid amount")
                continue
            deposit(deposit_amount)
            transaction_history("Deposit", deposit_amount)

        elif service == 3 :
            try:
                withdrawal_amount = int(input("Withdrawal Amount in KOR:₩  "))
            except ValueError:
                print("Invalid amount")
                continue
            withdraw(withdrawal_amount)
            transaction_history("Withdrawal", withdrawal_amount)

        elif service == 4 :
            account_history(name)

        elif service == 5 :
            current_balance()

        elif service == 0 :
            print("Exit service! Thank you for using CS50P Bank.")
            sys.exit()


def get_account():
    degit1 = random.randint(0,999)
    degit2 = random.randint(0,99)
    degit3 = random.randint(1000000, 9999999)

    degit1 = str(degit1).zfill(3)
    degit2 = str(degit2).zfill(2)
    degit3 = str(degit3)#.zfill(7)

    account_num = degit1 + '-' + degit2 + '-' + degit3
    return account_num


def create_transaction_file(name):
    file_name = f"{name}'s Transaction File.csv"
    with open (file_name, "w", newline ="") as file :
        writer = csv.writer(file)
        writer.writerow(["Time", "Type", "Amount", "Current Balance"])
    print(f"Your Bank Account successfully opened and '{file_name}' created.")



def deposit(amount):
    global balance
    if amount <= 0:
        print("Invalid amount to deposit")
    else:
        balance += amount
    return balance


def withdraw(amount):
    global balance

    if amount <= 0:
        print("Invalid amount to withdraw")
    elif amount > balance:
        print("The Amount is not available to withdraw.")
        print(f"Your balance is ₩{balance}")
    else:
        balance -= amount
    return balance


def transaction_history(transaction_type, amount): #create a txt file for the account history
    global name
    global balance

    file_name = f"{name}'s Transaction File.csv"

    if amount <=0:
        print("Amount must be positive")
        return
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_amount = f"₩ {amount:,}"
    formatted_balance = f"₩ {balance:,}"

    transaction_data = [
        now, transaction_type, formatted_amount, formatted_balance
    ]

    with open (file_name, "a", newline="") as file :
        writer = csv.writer(file)
        writer.writerow(transaction_data)
    print("-"*40)
    print(f"Transaction recorded: {transaction_type} {formatted_amount}. New balance: {formatted_balance}")
    print("-"*40)

def current_balance():
    global balance
    print(f"Current Balance: ₩ {balance:,}")

def account_history(name):
    file_name = f"{name}'s Transaction File.csv"

    try:
        with open(file_name, "r", newline = "") as file:
            reader = csv.reader(file)
            print(f"Transaction History for {name}")
            for row in reader:
                print(f"| {row[0]:20} | {row[1]:15} | {row[2]:10} | {row[3]:15} |")
    except FileNotFoundError:
        print(f"Transaction history file not found.")

def load_balance():
    global balance
    global balance
    file_name = f"{name}'s Transaction File.csv"
    try:
        with open(file_name, "r", newline = "") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                balance = 0
                return

            last_transaction = rows[-1]
            balance_str = last_transaction[3].replace('₩', '').replace(',', '').strip()
            balance = int(balance_str)

    except FileNotFoundError:
        print("You do not have a Bank Account yet")

if __name__ == "__main__":
    main()
"""
