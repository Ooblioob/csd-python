import unittest
from hamcrest import *
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
        assert_false(result)
        assert_that(result, is_(equal_to(False)))

    def test_is_payment_made_with_a_payment(self):
        # Arrange
        self.processor.make_payment(1)

        # Act
        result = self.processor.is_payment_made()

        # Assert
        assert_true(result)
        assert_that(result, is_(equal_to(True)))

    def test_make_payment_expects_payment_nonzero(self):
        # Arrange

        # Act
        self.processor.make_payment(1)

        # Assert
        assert_not_equal(0, self.processor.payment)
        assert_that(self.processor.payment, is_not(equal_to(0)))
