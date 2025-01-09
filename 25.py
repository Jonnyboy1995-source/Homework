from datetime import datetime
import shelve



class Balance:
    def __init__(self, account_id: int, full_name_owner: str, balance: float):
        self.account_id = account_id
        self.full_name_owner = full_name_owner
        self.balance = balance
        self.creation_time = datetime.now()

    def __str__(self):
        return self.full_name_owner, self.balance

    def __repr__(self):
        pass

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        pass

    def __sub__(self, other):
        return self.balance - other.balance

    def __mul__(self, other):
        return self.balance * other.balance

    def __len__(self):
        current_time = datetime.now()
        return int((current_time - self.creation_time).total_seconds() // 60)

    def save_to_file(self, filename):
        with shelve.open(filename) as db:
            db[str(self.account_id)] = self

    def load_from_file(self, account_id):
        with shelve.open(self) as db:
            return db.get(str(account_id))


b1 = Balance(8676230, "arya stark", 28000)
bg = Balance(6875533, "golum", 28000)
b2 = Balance(5979982, "jon snow", 79011)

print(bg == b1)
print(b1 != bg)
print(b1 > b2)
print(b1 < b2)
b3 = b1 + b2
print(b2 - b1)
print(b2 * b1)
print(len(b1))

b1.save_to_file("accounts")
loaded_b1 = Balance.load_from_file("accounts", 8676230)
print(f"Loaded account: {loaded_b1.full_name_owner}, {loaded_b1.balance}")
