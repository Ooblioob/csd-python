import unittest
from nose.tools import *
from payments import PaymentProcessor

class TestPaymentProcessor:
    def setup(self):
        self.processor = PaymentProcessor()

    def test_is_payment_made_with_no_payment(self):
        # Arrange

        # Act
        result = self.processor.is_payment_made()

        # Assert
        assert_false(result, "is_payment_made should have returned false for no payment")

    def test_is_payment_made_with_a_payment(self):
        # Arrange
        self.processor.make_payment(1)

        # Act
        result = self.processor.is_payment_made()

        # Assert
        assert_true(result, "should have returned true because a payment was made")

    def test_make_payment_expects_payment_nonzero(self):
        # Arrange

        # Act
        self.processor.make_payment(1)

        # Assert
        assert_not_equal(0, self.processor.payments)
