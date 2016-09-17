import unittest
from nose.tools import *
from vending_machine import VendingMachine

class TestVendingMachine:
    def test_release_change_when_no_payment_expects_0_change(self):
        # Arrange
        vending_machine = VendingMachine()

        # Act
        result = vending_machine.release_change()

        # Assert
        assert_true(result == 0)
        assert_equals(0, result)

    def test_release_change_with_payment_expects_change_returned(self):
        # Arrange
        vending_machine = VendingMachine()
        vending_machine.insert_coin(1)

        # Act
        result = vending_machine.release_change()

        # Assert
        assert_true(result > 0)
        assert_greater(result, 0)

    @unittest.skip("buy_product now returns an exception")
    def test_buy_product_with_no_payment_expects_nothing(self):
        # Arrange
        vending_machine = VendingMachine()

        # Act
        result = vending_machine.buy_product()

        # Assert
        assert_is_none(result)

    def test_buy_product_with_payment_expects_product(self):
        # Arrange
        vending_machine = VendingMachine()
        vending_machine.insert_coin(1)

        # Act
        result = vending_machine.buy_product()

        # Assert
        assert_is_not_none(result)

    @raises(RuntimeError)
    def test_buy_product_with_no_payment_expects_exception(self):
        # Arrange
        vending_machine = VendingMachine()

        # Act
        result = vending_machine.buy_product()

        # Assert
        # an exception should be raised
