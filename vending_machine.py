class VendingMachine:
    def __init__(self):
        self.payment = 0

    def release_change(self):
        if self.payment > 0:
            return 1
        else:
            return 0
