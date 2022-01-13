# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def dominantIndex1(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return 0
        if nums[0] >= nums[1]:
            max_index, second_index = 0, 1
        else:
            max_index, second_index = 1, 0
        for i in range(2, length):
            if nums[i] > nums[second_index]:
                if nums[i] > nums[max_index]:
                    second_index = max_index
                    max_index = i
                else:
                    second_index = i
        return max_index if nums[max_index] >= nums[second_index] * 2 else -1

    def dominantIndex(self, nums: List[int]) -> int:
        m1, m2, r = -1, -1, 0
        for index, item in enumerate(nums):
            if item > m1:
                m2 = m1
                m1 = item
                r = index
            elif item > m2:
                m2 = item
        return r if m1 >= m2 * 2 else -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 0]
    print(s.dominantIndex(nums) == 0)

    nums = [3, 6, 1, 0]
    print(s.dominantIndex(nums) == 1)

    nums = [1, 2, 3, 4]
    print(s.dominantIndex(nums) == -1)

    nums = [1]
    print(s.dominantIndex(nums) == 0)

    nums = [0, 0, 1, 2]
    print(s.dominantIndex(nums) == 3)
