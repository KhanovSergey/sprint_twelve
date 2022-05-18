import pytest

from l_fibonacci_modulo import fibonacciModulo


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ([10, 1], 9),
        ([3, 1], 3),
        ([921756, 5], 1737),
        ([1000000, 8], 26937501)
    ]
)
def test_l_fibonacci_modulo(input, expected_result):
    assert fibonacciModulo(input[0], input[1]) == expected_result
