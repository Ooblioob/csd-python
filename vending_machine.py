class VendingMachine:
    def __init__(self):
        self.payment = 0
        self.message = 'Please insert money'

    def release_change(self):
        if self.payment > 0:
            return 1
        else:
            return 0

    def insert_coin(self, count):
        self.payment = count * 25

    def buy_product(self):
        if self.payment != 0:
            self.message = 'Enjoy!'
            return 'product'
        else:
            raise RuntimeError("Cannot buy product without payment")

