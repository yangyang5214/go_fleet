# -*- coding: UTF-8 -*-
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        分治法
        :param strs:
        :return:
        """

        def lcp(start: int, end: int):
            if start == end:
                return strs[start]
            mid = (start + end) // 2
            left, right = lcp(start, mid), lcp(mid + 1, end)
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]

        return "" if not strs else lcp(0, len(strs) - 1)

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        """
        横向比较
        :param strs:
        :return:
        """

        def get_prefix(str1: str, str2: str):
            min_len = min(len(str1), len(str2))
            for i in range(min_len):
                if str1[i] != str2[i]:
                    return str1[:i]
            return str1[:min_len]

        size = len(strs)
        common_prefix = strs[0]
        for i in range(1, size):
            common_prefix = get_prefix(common_prefix, strs[i])
            if not common_prefix:
                return ""
        return common_prefix

    def longestCommonPrefix1(self, strs: List[str]) -> str:

        min_length = len(strs[0])
        for item in strs[1:]:
            min_length = min(min_length, len(item))

        index = 0
        while index < min_length:
            if len(set([item[index] for item in strs])) != 1:
                break
            index = index + 1
        if index != 0:
            return strs[0][:index]
        return ''


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix(["a", "a"]))
    print(s.longestCommonPrefix(["a"]))
