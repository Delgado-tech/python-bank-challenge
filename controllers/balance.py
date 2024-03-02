class Balance():
    def __init__(self, amount: float):
        self.amount = amount

    def get(self):
        return self.amount
    
    def set(self, amount: float):
        self.amount = amount

    def add(self, amount: float):
        self.amount += amount

    def remove(self, amount: float):
        self.amount -= amount