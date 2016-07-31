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
        assert_equals(0, result)

    def test_release_change_with_payment_expects_change_returned(self):
        # Arrange
        vending_machine = VendingMachine()
        vending_machine.insert_coin(1)

        # Act
        result = vending_machine.release_change()

        # Assert
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

    def test_get_message_returns_success_message_with_successful_purchase(self):
        # Arrange
        vending_machine = VendingMachine()
        vending_machine.insert_coin(1)

        # Act
        vending_machine.buy_product()

        # Assert
        assert_equals(vending_machine.message, "Enjoy!")

    def test_get_message_returns_insert_money_message_when_purchase_fails(self):
        # Arrange
        vending_machine = VendingMachine()

        # Act
        try:
            vending_machine.buy_product()
            assert False, "buy_product should have failed with exception"
        except:
            # Assert
            assert_equals(vending_machine.message, "Please insert money")
