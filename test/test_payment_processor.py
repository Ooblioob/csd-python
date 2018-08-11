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

    # Assert
    assert result == False
    assert_that(result, is_(equal_to(False)))

def test_is_payment_made_with_a_payment(processor):
    # Arrange
    processor.make_payment(1)

    # Act
    result = processor.is_payment_made()

    # Assert
    assert result == True
    assert_that(result, is_(equal_to(True)))

def test_make_payment_expects_payment_nonzero(processor):
    # Arrange

    # Act
    processor.make_payment(1)

    # Assert
    assert processor.payment != 0
    assert_that(processor.payment, is_not(equal_to(0)))
