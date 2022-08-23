import pytest

import starter_file


@pytest.mark.parametrize(
    "arg_one,arg_two,expected",
    [
        pytest.param(5, 5, 10, id="int, simple"),
        pytest.param(5.5, 4.6, 10.1, id="float, simple"),
        pytest.param("🐎", "🐙", "🐎🐙", id="emoji, stupid"),
    ],
)
def test_testable_func(arg_one, arg_two, expected):
    result = starter_file.adder(arg_one, arg_two)
    assert result == expected
