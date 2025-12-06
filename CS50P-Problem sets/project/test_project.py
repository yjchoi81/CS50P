import pytest
import os
import csv
# [수정] 바뀐 함수 이름 import
from project import get_account, create_transaction_file, deposit, withdraw, record_transaction, current_balance, display_account_history, load_balance

#---------setup variables
test_name = "test_user"
test_file = f"{test_name}'s Transaction File.csv"

def setup_module(module):
    if os.path.exists(test_file):
        os.remove(test_file)

def teardown_module(module):
    if os.path.exists(test_file):
        os.remove(test_file)

#--------- Test Functions ---------

def test_get_account():
    account_num = get_account()
    assert len(account_num) == 14
    assert '-' in account_num
    parts = account_num.split('-')
    assert len(parts) == 3

def test_create_transaction_file():
    create_transaction_file(test_name)
    assert os.path.exists(test_file)

    # 구분자 | 확인
    with open(test_file, "r", newline="") as file:
        reader = csv.reader(file, delimiter='|')
        header = next(reader)
        assert header == ["Time", "Type", "Amount", "Current Balance"]

def test_deposit():
    assert deposit(0, 100) == 100
    assert deposit(100, 50) == 150
    assert deposit(150, -200) == 150

def test_withdraw():
    assert withdraw(200, 50) == 150
    assert withdraw(150, 300) == 150 # 잔액 부족 시 그대로 150 리턴
    assert withdraw(150, -10) == 150

def test_record_transaction():
    # [수정] 함수 이름 변경 반영
    create_transaction_file(test_name)
    record_transaction(test_name, 200, "Deposit", 200)

    with open(test_file, "r", newline="") as file:
        reader = csv.reader(file, delimiter='|')
        rows = list(reader)

        assert len(rows) == 2
        history = rows[1]
        assert history[1] == "Deposit"
        assert history[2] == "₩ 200"
        assert history[3] == "₩ 200"

def test_current_balance(capsys):
    current_balance(1234567)
    captured = capsys.readouterr()
    assert "Current Balance: ₩ 1,234,567" in captured.out

def test_load_balance():
    if os.path.exists(test_file):
        os.remove(test_file)
    create_transaction_file(test_name)

    # 테스트용 데이터 주입 (구분자 |)
    with open(test_file, "a", newline="") as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(["2025-12-03 10:00:00", "Final Load Test", "₩ 500", "₩ 600"])

    loaded_bal = load_balance(test_name)
    assert loaded_bal == 600

def test_display_account_history(capsys):
    # [수정] 함수 이름 변경 반영
    if os.path.exists(test_file):
        os.remove(test_file)
    create_transaction_file(test_name)

    with open(test_file, "a", newline="") as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(["2025-12-04 10:00:00", "Deposit", "₩ 5,000", "₩ 5,000"])

    display_account_history(test_name)
    captured = capsys.readouterr()

    # 출력 확인
    assert "| Deposit         |" in captured.out
    assert "| ₩ 5,000    |" in captured.out


"""import pytest
import os
import csv
import project
from project import get_account, create_transaction_file, deposit, withdraw, transaction_history, current_balance, account_history, load_balance

#---------setup the variables for testing
test_name = "test_user"
test_file = f"{test_name}'s Transaction File.csv"

#--------- setup Function---------

def setup_module(module):
    # [수정] project 모듈 내부의 변수를 초기화해야 함
    project.name = test_name
    project.balance = 0

    if os.path.exists(test_file):
        os.remove(test_file)


def teardown_module(module):
    if os.path.exists(test_file):
        os.remove(test_file)

#--------- Test Function---------

def test_get_account():
    account_num = get_account()
    assert len(account_num) == 13
    assert '-' in account_num

    parts = account_num.split('-')
    assert len(parts) == 3
    assert len(parts[0]) == 3
    assert len(parts[1]) == 2
    assert len(parts[2]) == 7


def test_create_transaction_file():
    create_transaction_file(test_name)
    assert os.path.exists(test_file)

    with open(test_file, "r", newline = "") as file:
        reader = csv.reader(file)
        header = next(reader)

        assert header == ["Time", "Type", "Amount", "Current Balance"]

def test_deposit():

    project.balance = 0

    deposit(100)
    assert project.balance == 100  # [수정] project.balance 확인
    deposit(50)
    assert project.balance == 150
    deposit(-200)
    assert project.balance == 150

def test_withdraw():
    project.balance = 200

    withdraw(50)
    assert project.balance == 150
    withdraw(300)
    assert project.balance == 150


def test_transaction_history():
    project.balance = 200

    create_transaction_file(test_name)
    transaction_history("Test Deposit", 200)

    with open(test_file, "r", newline = "") as file:
        reader = csv.reader(file)
        rows = list(reader)

        assert len(rows) ==2

        history = rows[1]
        assert history[1] == "Test Deposit"
        assert history[2] == "₩ 200"
        assert history[3] == "₩ 200"



def test_current_balance(capsys):
    project.balance = 1234567  # [수정]
    current_balance()
    captured = capsys.readouterr()
    assert captured.out == "Current Balance: ₩ 1234567 \n"

    project.balance = 0  # [수정]
    current_balance()
    captured = capsys.readouterr()
    assert captured.out == "Current Balance: ₩ 0 \n"



def test_account_history(capsys):
    global name
    create_transaction_file(test_name)

    test_transactions = [
        ["2025-12-04 10:00:00", "Deposit", "₩ 5,000", "₩ 5,000"],
        ["2025-12-04 11:00:00", "Withdrawal", "₩ 2,000", "₩ 3,000"]
    ]
    with open(test_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(test_transactions)

    account_history(test_name)
    captured = capsys.readouterr()
    output_result = [
        # title
        f"Transaction History for {test_name}\n",
        # header
        f"| {'Time':20} | {'Type':15} | {'Amount':10} | {'Current Balance':15} |\n",
        # first row
        f"| {'2025-12-04 10:00:00':20} | {'Deposit':15} | {'₩ 5,000':10} | {'₩ 5,000':15} |\n",
        # second row
        f"| {'2025-12-04 11:00:00':20} | {'Withdrawal':15} | {'₩ 2,000':10} | {'₩ 3,000':15} |\n",
    ]

    assert captured.out == "".join(output_result)

def test_account_history_file_not_found(capsys):
    name = "NonExistentUser"

    account_history(name)
    captured = capsys.readouterr()

    assert captured.out.strip() == "Transaction history file not found."

def test_load_balance():
    project.balance = 0  # [수정]

    create_transaction_file(test_name)
    final_balance_data = [
        ["2025-12-03 10:00:00", "Final Load Test", "₩ 500", "₩ 600"]
    ]
    with open(test_file, "a", newline ="") as file:
        writer = csv.writer(file)
        writer.writerows(final_balance_data)

    load_balance()
    assert project.balance == 600"""
