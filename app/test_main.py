from app.main import get_human_age


def test_zero_age_returns_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_below_first_threshold_returns_zero() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_threshold_returns_one() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_below_second_threshold_returns_one() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_second_threshold_returns_two() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_diverge_after_second_threshold() -> None:
    # cat: every 4 years = +1, dog: every 5 years = +1
    assert get_human_age(28, 28) == [3, 2]


def test_large_age() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_different_cat_and_dog_ages() -> None:
    assert get_human_age(15, 0) == [1, 0]
    assert get_human_age(0, 15) == [0, 1]


def test_cat_step_is_four_years() -> None:
    # after 24: each 4 cat years = +1 human year
    assert get_human_age(27, 0) == [2, 0]
    assert get_human_age(28, 0) == [3, 0]


def test_dog_step_is_five_years() -> None:
    # after 24: each 5 dog years = +1 human year
    assert get_human_age(0, 28) == [0, 2]
    assert get_human_age(0, 29) == [0, 3]
