# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        双层循环
        :param nums:
        :param k:
        :return:
        """
        m = {}
        for index, item in enumerate(nums):
            if item in m and abs(m[item] - index) <= k:
                return True
            else:
                m[item] = index
        return False

    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        """
        双层循环
        :param nums:
        :param k:
        :return:
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, i + k + 1):
                if j < length and nums[i] == nums[j]:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(s.containsNearbyDuplicate(nums, k))

    nums = [1, 0, 1, 1]
    k = 1
    print(s.containsNearbyDuplicate(nums, k))

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(s.containsNearbyDuplicate(nums, k))

    nums = [1]
    k = 1
    print(s.containsNearbyDuplicate(nums, k))

    nums = [99, 99]
    k = 2
    print(s.containsNearbyDuplicate(nums, k))
