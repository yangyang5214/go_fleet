# -*- coding: UTF-8 -*-

class Solution:
    MAPPING = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        r = 0
        for index, item in enumerate(s):
            r = r + Solution.MAPPING.get(item)
            if index - 1 >= 0 and Solution.MAPPING.get(item) > Solution.MAPPING.get(s[index - 1]):
                r = r - Solution.MAPPING.get(s[index - 1]) * 2
        return r

    def romanToInt1(self, s: str) -> int:

        length = len(s)
        if length == 1:
            return Solution.MAPPING.get(s)
        r, index = 0, 1
        while index < length:
            cur = Solution.MAPPING.get(s[index - 1])
            _next = Solution.MAPPING.get(s[index])
            if _next > cur:
                r = r + _next - cur
                # 保留前一位
                _next = Solution.MAPPING.get(s[index + 1]) if index + 1 < length else 0
                index = index + 2
            else:
                r = r + cur
                index = index + 1
        return r + _next


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('IV') == 4)
    print(s.romanToInt('MDCXCV') == 1695)
    print(s.romanToInt('III') == 3)
    # M(1000) + CM(900) + XC(90) + IV(4)
    print(s.romanToInt('MCMXCIV') == 1994)
    # M(1000) + M(1000) + CM(900) + X(10) + X(10) + V(5)
    print(s.romanToInt('MMCDXXV') == 2425)
    print(s.romanToInt('LVIII') == 58)
    print(s.romanToInt('IX') == 9)
    print(s.romanToInt('IV') == 4)
