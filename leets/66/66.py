from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        digits[-1] = digits[-1] + 1  # 最后一位 +1
        for i in range(length - 1, -1, -1):
            val = digits[i]
            if val >= 10:
                digits[i] = val % 10
                if i - 1 >= 0:
                    digits[i - 1] = digits[i - 1] + 1
            else:
                digits[i] = val
                break
        return [1] + digits if digits[0] == 0 else digits  # 处理 length 溢出 情况


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([9, 9]))
    print(s.plusOne([1, 9, 9]))
    print(s.plusOne([4, 3, 2, 1]))
    print(s.plusOne([0]))
