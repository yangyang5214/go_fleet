from typing import List


class Solution:
    """
    移除 nums[i] == val 的元素
    """

    def removeElement1(self, nums: List[int], val: int) -> int:
        print("before: {} ,val: {}".format(nums, val))
        length = len(nums)
        index = 0
        for i in range(length):
            if nums[i] != val:  # 不同元素
                if index != i:
                    nums[index] = nums[i]
                index = index + 1
        print("after: {} ".format(nums))
        return index

    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return left


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(s.removeElement(nums, val))
    print(nums)

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(s.removeElement(nums, val))
    print(nums)
