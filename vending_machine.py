from payments import PaymentProcessor
from notifications import HQ

class VendingMachine:
    def __init__(self):
        self.payment_processor = PaymentProcessor()
        self.message = 'Please insert money'
        self.hq = HQ()

    def release_change(self):
        if self.payment_processor.is_payment_made():
            return 1
        else:
            return 0

    def insert_coin(self, count):
        self.payment_processor.make_payment(count)

    def buy_product(self):
        if self.payment_processor.is_payment_made():
            self.message = "Enjoy!"
            self.hq.notify('product purchased')
            return 'product'
        else:
            self.hq.notify('unsuccessful purchase')
            raise RuntimeError("Cannot buy product without payment")

    def get_message(self):
        return self.message
