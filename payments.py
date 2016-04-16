class PaymentProcessor:
    def __init__(self):
        self.payment = 0

    def is_payment_made(self):
        return self.payment > 0

    def make_payment(self, count):
        self.payment = count * 25
