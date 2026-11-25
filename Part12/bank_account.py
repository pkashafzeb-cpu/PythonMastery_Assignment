{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c521f998",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "class BankAccount:\n",
    "    def __init__(self, owner: str, balance: float = 0):\n",
    "        self.owner = owner\n",
    "        self.balance = balance\n",
    "        self.history = []\n",
    "\n",
    "    def deposit(self, amount: float) -> None:\n",
    "        if amount <= 0:\n",
    "            raise ValueError(\"Deposit amount must be positive\")\n",
    "\n",
    "        self.balance += amount\n",
    "        self.history.append(f\"Deposited Rs. {amount}\")\n",
    "\n",
    "    def withdraw(self, amount: float) -> None:\n",
    "        if amount <= 0:\n",
    "            raise ValueError(\"Withdrawal amount must be positive\")\n",
    "\n",
    "        if amount > self.balance:\n",
    "            raise ValueError(\"Insufficient balance\")\n",
    "\n",
    "        self.balance -= amount\n",
    "        self.history.append(f\"Withdrew Rs. {amount}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd702229",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
