
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    m = {}
    for index in range(len(nums)):
        num = nums[index]
        r = target - num
        if r not in m:
            m[num] = index
        else:
            return m[r], index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
