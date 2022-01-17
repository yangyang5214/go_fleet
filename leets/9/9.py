# -*- coding: UTF-8 -*-

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        r = 0
        while True:
            temp = x % 10
            r = r * 10 + temp
            x = x // 10
            if x <= r:
                break
        return r == x or r // 10 == x

    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        length = len(s)
        for index in range(length // 2):
            if s[index] != s[length - index - 1]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(10) is False)
    print(s.isPalindrome(88888) is True)
    print(s.isPalindrome(123) is False)
    print(s.isPalindrome(100) is False)
    print(s.isPalindrome(121) is True)
    print(s.isPalindrome(1234) is False)
    print(s.isPalindrome(1221) is True)
    print(s.isPalindrome(-121) is False)
    print(s.isPalindrome(10) is False)
    print(s.isPalindrome(11) is True)
