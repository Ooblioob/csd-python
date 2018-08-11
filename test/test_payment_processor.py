import pytest
from hamcrest import *
from payments import PaymentProcessor

@pytest.fixture
def processor():
    return PaymentProcessor()

def test_is_payment_made_with_no_payment(processor):
    # Arrange

    # Act
    result = processor.is_payment_made()

    assert result == False, "is_payment_made should have returned false for no payment"

def test_is_payment_made_with_a_payment(processor):
    # Arrange
    processor.make_payment(1)

    # Act
    result = processor.is_payment_made()

    # Assert
    assert result == True, "should have returned true because a payment was made"

def test_make_payment_expects_payment_nonzero(processor):
    # Arrange

    # Act
    processor.make_payment(1)

    # Assert
    assert processor.payments != 0
