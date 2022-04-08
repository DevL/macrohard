def leap_year(year, julian=False, spreadsheet=False, ignore_astronomical_drift=False):
    if year == 0:
        raise LeapYearError("Year 0 does not exist")
    if type(year) != int:
        raise LeapYearError("Year must be an integer")
    if julian:
        return julian_leap_year(year)
    return gregorian_leap_year(year, spreadsheet, ignore_astronomical_drift)


def julian_leap_year(year):
    if year < -45:
        raise LeapYearError(f"Year {year} precedes the Julian calendar")
    if -45 < year <= -9 and year % 3 == 0:
        return True
    elif year >= 8 and year % 4 == 0:
        return True
    return False


def gregorian_leap_year(year, spreadsheet, ignore_astronomical_drift):
    if year < 1582:
        raise LeapYearError(f"Year {year} precedes the Gregorian calendar")
    if year >= 4818 and ignore_astronomical_drift is False:
        raise LeapYearError(
            f"The Gregorian calendar is out of sync with the astronomical calendar in year {year}"
        )
    if spreadsheet and year == 1900:
        return True
    if year % 100 == 0 and year % 400 != 0:
        return False
    return year % 4 == 0


class LeapYearError(Exception):
    pass
