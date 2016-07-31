import unittest
from hamcrest import *
from nose.tools import *
from vending_machine import VendingMachine

class TestVendingMachine:
    def setup(self):
        self.vending_machine = VendingMachine()

    def test_release_change_when_no_payment_expects_0_change(self):
        # Arrange

        # Act
        result = self.vending_machine.release_change()

        # Assert
        assert_that(result, is_(equal_to(0)))

    def test_release_change_with_payment_expects_change_returned(self):
        # Arrange
        self.vending_machine.insert_coin(1)

        # Act
        result = self.vending_machine.release_change()

        # Assert
        assert_that(result, is_(greater_than(0)))

    @unittest.skip("buy_product now returns an exception")
    def test_buy_product_with_no_payment_expects_nothing(self):
        # Arrange

        # Act
        result = self.vending_machine.buy_product()

        # Assert
        assert_that(result, is_(none()))

    def test_buy_product_with_payment_expects_product(self):
        # Arrange
        self.vending_machine.insert_coin(1)

        # Act
        result = self.vending_machine.buy_product()

        # Assert
        assert_that(result, is_(not_none()))

    @raises(RuntimeError)
    def test_buy_product_with_no_payment_expects_exception(self):
        # Arrange

        # Act
        result = self.vending_machine.buy_product()

        # Assert
        # an exception should be raised

    def test_get_message_returns_success_message_with_successful_purchase(self):
        # Arrange
        self.vending_machine.insert_coin(1)

        # Act
        self.vending_machine.buy_product()

        # Assert
        assert_that(self.vending_machine.message, is_(equal_to("Enjoy!")))

    def test_get_message_returns_insert_money_message_when_purchase_fails(self):
        # Arrange

        # Act
        try:
            self.vending_machine.buy_product()
            assert False, "buy_product should have failed with exception"
        except:
            # Assert
            assert_that(self.vending_machine.message, is_(equal_to("Please insert money")))
