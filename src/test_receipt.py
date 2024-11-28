# tests for receipt functions
import pytest

from src import receipt_code

@pytest.mark.parametrize("input", [1.23,2,45.55543])
def test_round_values(input):
    value = receipt_code.round_value(input)
    assert value == round(input,2)

@pytest.mark.parametrize("input", ["three",True])
def test_round_type(input):
    with pytest.raises(TypeError) as error:
        receipt_code(input)
        assert error.value.args[0] == "was expecting command to be int or float, but got a str or bool"