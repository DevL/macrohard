import pytest
from leap_year import leap_year, LeapYearError


@pytest.mark.parametrize(
    "year, is_leap_year, opts",
    [
        (-45, False, {"julian": True}),
        (-44, False, {"julian": True}),
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
        (1700, True, {"julian": True}),
        (1700, False, {}),
        (1789, False, {}),
        (1800, False, {}),
        (1880, True, {}),
        (1899, False, {}),
        (1900, False, {}),
        (1900, True, {"spreadsheet": True}),
        (1900, True, {"julian": True}),
        (1900, True, {"julian": True, "spreadsheet": True}),
        (1901, False, {}),
        (1901, False, {"spreadsheet": True}),
        (1901, False, {"spreadsheet": True, "julian": True, }),
        (1912, True, {}),
        (1929, False, {}),
        (1960, True, {}),
        (1977, False, {}),
        (1980, True, {}),
        (2000, True, {}),
        (2020, True, {}),
        (4816, True, {}),
        (4817, False, {}),
        (4818, False, {"julian": True}),
        (4820, True, {"ignore_astronomical_drift": True}),
        (4820, True, {"julian": True})
    ],
)
def test_leap_year(year, is_leap_year, opts):
    assert leap_year(year, **opts) == is_leap_year


@pytest.mark.parametrize(
    "year, message, opts",
    [
        (0, "Year 0 does not exist", {}),
        (0, "Year 0 does not exist", {"julian": True}),
        ("1900", "Year must be an integer", {}),
        (1900.1, "Year must be an integer", {}),
        (-1, "Year -1 precedes the Gregorian calendar", {}),
        (1581, "Year 1581 precedes the Gregorian calendar", {}),
        (-46, "Year -46 precedes the Julian calendar", {"julian": True}),
        (4818, "The Gregorian calendar is out of sync with the astronomical calendar in year 4818", {}),
    ],
)
def test_leap_year_handles_bad_input(year, message, opts):
    with pytest.raises(LeapYearError, match=message):
        leap_year(year, **opts)
