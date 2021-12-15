# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [[] for _ in range(n)]
        for r in richer:
            g[r[1]].append(r[0])

        ans = [-1] * n
        for index in range(n):
            self.dfs(index, ans, g, quiet)
        return ans

    def dfs(self, x: int, ans, g, quiet):
        if ans[x] != -1:
            return
        ans[x] = x
        for y in g[x]:
            self.dfs(y, ans, g, quiet)
            if quiet[ans[y]] < quiet[ans[x]]:
                ans[x] = ans[y]


if __name__ == '__main__':
    s = Solution()
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]

    # [1], [2, 3], [], [4, 5, 6], [], [], [], [3]
    #  0    1       2    3         4   5  6    7

    print(s.loudAndRich(richer, quiet))
