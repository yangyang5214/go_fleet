# -*- coding: UTF-8 -*-


def dayOfYear(date):
    """
    :type date: str
    :rtype: int
    """
    m = {
        1: 1,
        3: 1,
        4: 0,
        5: 1,
        6: 0,
        7: 1,
        8: 1,
        9: 0,
        10: 1,
        11: 0,
        12: 1,
    }
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    r = day

    def get_offset_of_year(year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return -1
        return -2

    for index in range(1, month):
        if index == 2:
            flag = get_offset_of_year(year)
        else:
            flag = m.get(index)
        r = r + 30 + flag
    return r


if __name__ == '__main__':
    print(dayOfYear("2019-01-09") == 9)
    print(dayOfYear("2019-02-10") == 41)
    print(dayOfYear("2003-03-01") == 60)
    print(dayOfYear("2004-03-01") == 61)
    print(dayOfYear("2008-10-10") == 284)
