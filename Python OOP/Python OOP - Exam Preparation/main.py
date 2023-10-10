class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []
        self.start = 0

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    def add_transaction(self, amount):
        self.__validate_amount(amount)
        self._transactions.append(amount)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account._transactions.append(amount_to_add)
        return f"New balance: {account.balance}"

    @staticmethod
    def __validate_amount(amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return self

    def __next__(self):
        end = len(self._transactions)

        if self.start == end:
            raise StopIteration

        current_value = self._transactions[self.start]
        self.start += 1
        return current_value

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        new_owner = f"{self.owner}&{other.owner}"
        new_amount = self.amount + other.amount
        new_transactions = self._transactions + other._transactions

        new_account = Account(new_owner, new_amount)

        for t in new_transactions:
            new_account.add_transaction(t)

        return new_account


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
