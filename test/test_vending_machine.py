import unittest
from hamcrest import *
from nose.tools import *
from vending_machine import VendingMachine
try:
    from mock import patch
except ImportError:
    from unittest.mock import patch

class TestVendingMachine:
    def setup(self):
        self.vending_machine = VendingMachine()

    def test_release_change_when_no_payment_expects_0_change(self):
        # Arrange

        # Act
        result = self.vending_machine.release_change()

        # Assert
        assert_true(result == 0)
        assert_equals(0, result)
        assert_that(result, is_(equal_to(0)))

    def test_release_change_with_payment_expects_change_returned(self):
        # Arrange
        self.vending_machine.insert_coin(1)

        # Act
        result = self.vending_machine.release_change()

        # Assert
        assert_true(result > 0)
        assert_greater(result, 0)
        assert_that(result, is_(greater_than(0)))

    @unittest.skip("buy_product now returns an exception")
    def test_buy_product_with_no_payment_expects_nothing(self):
        # Arrange

        # Act
        result = self.vending_machine.buy_product()

        # Assert
        assert_is_none(result)
        assert_that(result, is_(none()))

    @patch("payments.PaymentProcessor.is_payment_made")
    @patch("notifications.HQ.notify")
    def test_buy_product_with_payment_expects_product(self, notify_mock, is_payment_made_mock):
        # Arrange
        is_payment_made_mock.return_value = True

        # Act
        result = self.vending_machine.buy_product()

        # Assert
        assert_is_not_none(result)
        assert_that(result, is_(not_none()))

    #@raises(RuntimeError)
    @patch("payments.PaymentProcessor.is_payment_made")
    @patch("notifications.HQ.notify")
    def test_buy_product_with_no_payment_expects_exception(self, notify_mock, is_payment_made_mock):
        # Arrange
        is_payment_made_mock.return_value = False

        # Act
        #result = self.vending_machine.buy_product()

        # Assert
        assert_raises(RuntimeError, self.vending_machine.buy_product)
        assert_that(self.vending_machine.buy_product, raises(RuntimeError))

    @patch("payments.PaymentProcessor.is_payment_made")
    @patch("notifications.HQ.notify")
    def test_get_message_returns_success_message_with_successful_purchase(self, notify_mock, is_payment_made_mock):
        # Arrange
        is_payment_made_mock.return_value = True

        # Act
        self.vending_machine.buy_product()

        # Assert
        assert_equals(self.vending_machine.message, "Enjoy!")
        assert_that(self.vending_machine.message, is_(equal_to("Enjoy!")))

    @patch("payments.PaymentProcessor.is_payment_made")
    @patch("notifications.HQ.notify")
    def test_get_message_returns_insert_money_message_when_purchase_fails(self, notify_mock, is_payment_made_mock):
        # Arrange
        is_payment_made_mock.return_value = False

        # Act
        try:
            self.vending_machine.buy_product()
            assert False, "buy_product should have failed with exception"
        except:
            # Assert
            assert_equals(self.vending_machine.message, "Please insert money")
            assert_that(self.vending_machine.message, is_(equal_to("Please insert money")))

    @patch("payments.PaymentProcessor.is_payment_made")
    @patch("notifications.HQ.notify")
    def test_buy_product_with_payment_sends_notification(self, notify_mock, is_payment_made_mock):
        # Arrange
        is_payment_made_mock.return_value = True

        # Act
        self.vending_machine.buy_product()

        # Assert
        notify_mock.assert_called_with('product purchased')

    @patch("payments.PaymentProcessor.is_payment_made")
    @patch("notifications.HQ.notify")
    def test_buy_product_without_payment_sends_notification(self, notify_mock, is_payment_made_mock):
        # Arrange
        is_payment_made_mock.return_value = False

        # Act
        try:
            self.vending_machine.buy_product()
            assert False, "buy_product should have failed with exception"
        except:
            # Assert
            notify_mock.assert_called_with('unsuccessful purchase')
