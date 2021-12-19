# -*- coding: UTF-8 -*-


class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # 恐怖。。。
        if n == 1:
            return 1

        m = {}
        judge = {}
        for item in trust:
            m[item[0]] = m.get(item[0], 0) + 1
            judge[item[1]] = judge.get(item[1], 0) + 1

        for k, v in judge.items():
            if k not in m and v == n - 1:
                return k
        return -1


if __name__ == '__main__':
    s = Solution()
    n = 4
    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]

    n = 3
    trust = [[1, 2], [2, 3]]

    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]

    n = 3
    trust = [[1, 3], [2, 3]]

    n = 2
    trust = [[1, 2]]
    print(s.findJudge(n, trust))
