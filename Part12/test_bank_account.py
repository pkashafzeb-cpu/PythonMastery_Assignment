
import pytest
from bank_account import BankAccount


@pytest.fixture
def account():
    return BankAccount("Ali", 1000)


def test_deposit(account):
    account.deposit(500)
    assert account.balance == 1500


def test_withdraw(account):
    account.withdraw(300)
    assert account.balance == 700


def test_transaction_history(account):
    account.deposit(500)
    account.withdraw(200)

    assert len(account.history) == 2
    assert account.history[0] == "Deposited Rs. 500"
    assert account.history[1] == "Withdrew Rs. 200"


def test_negative_deposit(account):
    with pytest.raises(ValueError):
        account.deposit(-100)


def test_withdraw_more_than_balance(account):
    with pytest.raises(ValueError):
        account.withdraw(1500)


def test_negative_withdrawal(account):
    with pytest.raises(ValueError):
        account.withdraw(-100)
