import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (14, 14, [0, 0]),  # до 15 лет ещё нет +1
        (16, 16, [1, 1]),  # первый год после 15
        (30, 30, [3, 3]),  # пример большого возраста
    ]
)
def test_human_age_conversion(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected