class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        暴力破解

        超出时间限制
        :param haystack:
        :param needle:
        :return:
        """
        if not needle or needle == haystack:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            flag = True
            index = i
            for j in range(len(needle)):
                if index > len(haystack) - 1 or haystack[index] != needle[j]:
                    flag = False
                    break
                else:
                    index = index + 1
            if flag:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("hello", "ll"))  # 2
    print(s.strStr("aaaaa", "bba"))  # -1
    print(s.strStr("", ""))  # 0
    print(s.strStr("baa", "a"))  # 1
    print(s.strStr("mississippi", "issi"))  # 1
    print(s.strStr("mississippi", "issipp"))  # 4
    print(s.strStr("mississippi", "issipi"))  # -1
