
# Name: Kashaf
# Part 12 - Build: Test Grade Function

import pytest
from part5_func import grade


# Test all eight grade boundaries
@pytest.mark.parametrize(
    "marks, expected",
    [
        (32, "Fail"),
        (33, "D"),
        (59, "D"),
        (60, "C"),
        (69, "C"),
        (70, "B"),
        (79, "B"),
        (80, "A")
    ]
)
def test_grade_boundaries(marks, expected):
    assert grade(marks) == expected


# Test invalid marks
def test_invalid_marks():
    with pytest.raises(ValueError):
        grade(101)
