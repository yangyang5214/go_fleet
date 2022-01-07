# -*- coding: UTF-8 -*-


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        m = {}
        r = []
        for i in range(length - 10 + 1):
            sub_str = s[i: i + 10]
            count = m.get(sub_str, 0)
            if count == 1:
                r.append(sub_str)
            m[sub_str] = count + 1
        return r


if __name__ == '__main__':
    s = Solution()
    # print(s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
    # print(s.findRepeatedDnaSequences('AAAAAAAAAAAAA'))
    print(s.findRepeatedDnaSequences('AAAAAAAAAAA'))
