from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        """
        贪心算法

        每次遍历一个元素都得到当前的最优解
        :param nums:
        :return:
        """
        max_v = cur = nums[0]
        for item in nums[1:]:
            # 贪心思想，要不要当前的 item
            # if cur + item > cur , 则 更新 max_v
            cur = max(item, cur + item)
            max_v = max(max_v, cur)
        return max_v

    def maxSubArray1(self, nums: List[int]) -> int:
        """
        暴力
        :param nums:
        :return:
        """
        length = len(nums)
        r = nums[0]
        for i in range(length):
            flag = 0
            for j in range(i, length):
                flag = flag + nums[j]
                r = max(r, flag)
        return r


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums))

    nums = [5, 4, -1, 7, 8]
    print(s.maxSubArray(nums))

    nums = [1]
    print(s.maxSubArray(nums))

    nums = [-1]
    print(s.maxSubArray(nums))
