# -*- coding: UTF-8 -*-


class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = 0
        r = 0
        for item in s:
            if item == '(':
                cur += 1
            elif item == ')':
                cur -= 1
            else:
                continue
            r = max(r, cur)
        return 0 if cur != 0 else r


if __name__ == '__main__':
    s = Solution()
    print(s.maxDepth("(1+(2*3)+((8)/4))+1"))
    print(s.maxDepth("(1)+((2))+(((3)))"))
    print(s.maxDepth("1+(2*3)/(2-1)"))
    print(s.maxDepth("1"))
