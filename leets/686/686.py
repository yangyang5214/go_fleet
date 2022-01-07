# -*- coding: UTF-8 -*-
class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        len_a = len(a)
        len_b = len(b)

        if len_a < len_b:
            r = 0
            index = 0
            while index < len_b:
                count = 0
                for j in range(len_a):
                    if index < len_b:
                        if a[j] == b[index]:
                            index += 1
                            count += 1
                        else:
                            if r == 0:
                                continue
                            else:
                                return -1
                if count == 0:
                    return -1
                r = r + 1
            return r
        else:
            # b is sub_str for a
            index = 0
            a = a + a
            while index < len_a * 2:
                count = 0
                for j in range(len_b):
                    # 说明不是子串
                    if b[j] == a[index]:
                        index = index + 1
                        count += 1
                    else:
                        break
                if count == len_b:
                    return 1 if index <= len_a else 2
                else:
                    index = index - count + 1
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.repeatedStringMatch('aabab', 'abaabab') == 2)
    print(s.repeatedStringMatch('abcd', 'abcdb') == -1)
    print(s.repeatedStringMatch('abaabaa', 'abaababaab') == -1)
    print(s.repeatedStringMatch('abcd', 'cdabcdab') == 3)
    print(s.repeatedStringMatch('abcabc', 'abc') == 1)
    print(s.repeatedStringMatch('a', 'a') == 1)
    print(s.repeatedStringMatch('abc', 'wyhd') == -1)

    print(s.repeatedStringMatch('aaac', 'aac') == 1)
    print(s.repeatedStringMatch('aa', 'a') == 1)
    print(s.repeatedStringMatch('abcabcabcabc', 'abac') == -1)
    #
    print(s.repeatedStringMatch('aaaaaaaaaaaaaaaaaaaaaab', 'ba') == 2)
