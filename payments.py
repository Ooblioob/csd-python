class PaymentProcessor:
    def __init__(self):
        self.payments = 0

    def is_payment_made(self):
        return self.payments > 0

    def make_payment(self, count):
        self.payments += count
