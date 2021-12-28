class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length <= 1:
            return length
        r = 1
        for index in range(length):
            cur = set()
            for i in range(index, length):
                if s[i] in cur:
                    r = max(r, len(cur))
                    break
                else:
                    cur.add(s[i])
            r = max(r, len(cur))
        return r

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length <= 1:
            return length
        cur = set()
        left = 0
        r = 0
        for i in range(length):
            item = s[i]
            while item in cur:
                cur.remove(s[left])
                left += 1
            cur.add(item)
            r = max(len(cur), r)
        return max(len(cur), r)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb') == 3)
    print(s.lengthOfLongestSubstring('bbbbb') == 1)
    print(s.lengthOfLongestSubstring('pwwkew') == 3)
    print(s.lengthOfLongestSubstring('aab') == 2)
    print(s.lengthOfLongestSubstring("asjrgapa") == 6)
