class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        flag = False
        r = 1
        for i in range(length - 1, -1, -1):
            if flag:
                if s[i] != " ":
                    r += 1
                else:
                    return r
            else:
                if s[i] != " ":
                    flag = True
        return r

    def lengthOfLastWord1(self, s: str) -> int:
        """
        ignore...理解错题目了
        :param s:
        :return:
        """
        r, count = 0, 0
        for item in s:
            if item == " ":
                r = max(r, count)
                count = 0
            else:
                count += 1
        return max(r, count)  # 注意最后一次


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
    print(s.lengthOfLastWord("luffy is still joyboy"))
    print(s.lengthOfLastWord("Today is a nice day"))
