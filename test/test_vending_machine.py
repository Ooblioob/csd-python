import pytest
from hamcrest import *
from vending_machine import VendingMachine

@pytest.fixture
def vending_machine():
    return VendingMachine()

def test_release_change_when_no_payment_expects_0_change(vending_machine):
    # Arrange

    # Act
    result = vending_machine.release_change()

    # Assert
    assert result == 0
    assert_that(result, is_(equal_to(0)))

def test_release_change_with_payment_expects_change_returned(vending_machine):
    # Arrange
    vending_machine.insert_coin(1)

    # Act
    result = vending_machine.release_change()

    # Assert
    assert result > 0
    assert_that(result, is_(greater_than(0)))

@pytest.mark.skip("buy_product now returns an exception")
def test_buy_product_with_no_payment_expects_nothing(vending_machine):
    # Arrange

    # Act
    result = vending_machine.buy_product()

    # Assert
    assert result is None
    assert_that(result, is_(none()))

def test_buy_product_with_payment_expects_product(vending_machine):
    # Arrange
    vending_machine = VendingMachine()
    vending_machine.insert_coin(1)

    # Act
    result = vending_machine.buy_product()

    # Assert
    assert result is not None
    assert_that(result, is_(not_none()))

def test_buy_product_with_no_payment_expects_exception(vending_machine):
    # Arrange
    
    # Act
    #result = vending_machine.buy_product()
    with pytest.raises(RuntimeError):
        vending_machine.buy_product()
    assert_that(vending_machine.buy_product, raises(RuntimeError))

    # Assert
    # an exception should be raised

def test_get_message_returns_success_message_with_successful_purchase(vending_machine):
    # Arrange
    vending_machine.insert_coin(1)

    # Act
    vending_machine.buy_product()

    # Assert
    assert vending_machine.message == "Enjoy!"
    assert_that(vending_machine.message, is_(equal_to("Enjoy!")))

def test_get_message_returns_insert_money_message_when_purchase_fails(vending_machine):
    # Arrange

    # Act
    try:
        vending_machine.buy_product()
        assert False, "buy_product should have failed with exception"
    except:
        # Assert
        assert vending_machine.message == "Please insert money"
        assert_that(vending_machine.message, is_(equal_to("Please insert money")))
