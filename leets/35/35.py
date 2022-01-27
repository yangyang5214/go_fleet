# https://leetcode-cn.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums) -1 
        left, right = 0, length
        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1 
            else:
                left= mid + 1
        return left
