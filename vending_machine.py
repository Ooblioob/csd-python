class VendingMachine:
    def __init__(self):
        self.payment = 0

    def release_change(self):
        if self.payment > 0:
            return 1
        else:
            return 0

    def insert_coin(self, count):
        self.payment = count * 25

    def buy_product(self):
        if self.payment != 0:
            return 'product'
        else:
            return None
