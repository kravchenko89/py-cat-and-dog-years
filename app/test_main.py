import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),   # проверить: должно ли это быть 2 или 3 в реальной функции
        (30, 35, [17, 18]),  # <--- исправлено
    ]
)
def test_human_age_conversion(cat_age: int,
                              dog_age: int,
                              expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
