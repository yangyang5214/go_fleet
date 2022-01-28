class Solution:
    def mySqrt(self, x: int) -> int:
        """
        二分查找
        :param x:
        :return:
        """
        result, l, r = 0, 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                result = mid
                l = mid + 1
            else:
                r = mid - 1
        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.mySqrt(8))
    # print(s.mySqrt(4))
    print(s.mySqrt(9))
    # print(s.mySqrt(10))
