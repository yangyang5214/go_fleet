# -*- coding: UTF-8 -*-

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        r = [0]
        # 依次遍历 从 1 -> n ，求格雷码 [1:n] 前闭后闭
        for i in range(1, n + 1):
            count = 1 << i
            flag = 1 << (i - 1)

            # 只处理后一半（前一半是复制过来的）
            for j in range(count // 2, count):
                r.append(r[count - 1 - j] + flag)
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(1))
    print(s.grayCode(2))
    print(s.grayCode(3))
