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


