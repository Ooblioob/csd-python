from unittest import skip
from nose.tools import *
from vending_machine import VendingMachine
from mock import patch

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

    @skip("buy_product now returns an exception")
    def test_buy_product_with_no_payment_expects_nothing(self):
        # Arrange
        vending_machine = VendingMachine()

        # Act
        result = vending_machine.buy_product()

        # Assert
        assert_is_none(result)

    @patch("payments.PaymentProcessor.is_payment_made")
    @patch("notifications.HQ.notify")
    def test_buy_product_with_payment_expects_product(self, notify_mock, is_payment_made_mock):
        # Arrange
        vending_machine = VendingMachine()
        is_payment_made_mock.return_value = True

        # Act
        result = vending_machine.buy_product()

        # Assert
        assert_is_not_none(result)

    @patch("payments.PaymentProcessor.is_payment_made")
    @patch("notifications.HQ.notify")
    @raises(RuntimeError)
    def test_buy_product_with_no_payment_expects_exception(self, notify_mock, is_payment_made_mock):
        # Arrange
        vending_machine = VendingMachine()
        is_payment_made_mock.return_value = False

        # Act
        result = vending_machine.buy_product()

        # Assert
        # an exception should be raised

    @patch("payments.PaymentProcessor.is_payment_made")
    def test_buy_product_message_successful_purchase(self, is_payment_made_mock):
        # Arrange
        vending_machine = VendingMachine()
        is_payment_made_mock.return_value = True

        # Act
        vending_machine.buy_product()

        # Assert
        assert_equals(vending_machine.message, "Enjoy!")

    @patch("payments.PaymentProcessor.is_payment_made")
    def test_buy_product_message_unsuccessful_purchase(self, is_payment_made_mock):
        # Arrange
        vending_machine = VendingMachine()
        is_payment_made_mock.return_value = False

        # Act
        try:
            vending_machine.buy_product()
        except RuntimeError:
            assert_equals(vending_machine.message, "Please insert money")
        else:
            assert False, "Should have thrown a RuntimeError"


    @patch("payments.PaymentProcessor.is_payment_made")
    @patch("notifications.HQ.notify")
    def test_buy_product_with_payment_sends_notification(self, notify_mock, is_payment_made_mock):
        # Arrange
        vending_machine = VendingMachine()
        is_payment_made_mock.return_value = True

        # Act
        vending_machine.buy_product()

        # Assert
        notify_mock.assert_called_with('product purchased')
