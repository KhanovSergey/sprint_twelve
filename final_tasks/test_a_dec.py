import pytest

from final_tasks.a_dec import main


@pytest.mark.parametrize(
    "input, expected_result",
    [([4, 4], ('push_front', 861), ('push_front', -819), ('pop_back', None), ('pop_back', None),
      )
     ]
)
def test_a_dec(input, expected_result):
    assert main(input[0], input[1]) == expected_result
