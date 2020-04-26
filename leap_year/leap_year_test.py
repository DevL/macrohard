import pytest
from leap_year import leap_year, LeapYearError


@pytest.mark.parametrize(
    "year, is_leap_year, opts",
    [
        (-45, False, {"julian": True}),
        (-42, True, {"julian": True}),
        (-40, False, {"julian": True}),
        (-39, True, {"julian": True}),
        (-38, False, {"julian": True}),
        (-36, True, {"julian": True}),
        (-12, True, {"julian": True}),
        (-10, False, {"julian": True}),
        (-9, True, {"julian": True}),
        (-6, False, {"julian": True}),
        (-5, False, {"julian": True}),
        (-1, False, {"julian": True}),
        (4, False, {"julian": True}),
        (8, True, {"julian": True}),
        (12, True, {"julian": True}),
        (1789, False, {}),
        (1800, False, {}),
        (1880, True, {}),
        (1899, False, {}),
        (1900, False, {}),
        (1901, False, {}),
        (1912, True, {}),
        (1929, False, {}),
        (1960, True, {}),
        (1977, False, {}),
        (1980, True, {}),
        (2000, True, {}),
        (2020, True, {}),
        (4816, True, {}),
        (4817, False, {}),
    ],
)
def test_leap_year(year, is_leap_year, opts):
    assert leap_year(year, **opts) == is_leap_year


@pytest.mark.parametrize(
    "year, message, opts",
    [
        (0, "Year 0 does not exist", {}),
        ("1900", "Year must be an integer", {}),
        (1900.1, "Year must be an integer", {}),
        (-1, "Year -1 is not gregorian", {}),
        (1581, "Year 1581 is not gregorian", {}),
        (1582, "Year 1582 is not julian", {"julian": True}),
        (4818, "Out of sync with astronomical calendar in year 4818", {}),
    ],
)
def test_leap_year_handles_bad_input(year, message, opts):
    with pytest.raises(LeapYearError, match="message"):
        leap_year(year, **opts)
