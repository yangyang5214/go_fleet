# https://leetcode.cn/problems/duplicate-zeros/solution/liang-ci-bian-li-yuan-di-by-verygoodlee-wv6c/
def duplicateZeros(arr):
    """
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    """
    count = 0  # 统计有多少个0
    for i in range(len(arr)):
        if arr[i] == 0:
            count = count + 1
    print(count)

    # 倒叙
    for i in range(len(arr) - 1, -1, - 1):
        if arr[i] == 0:
            count = count - 1
        print(arr)
        if i + count < len(arr):
            arr[i + count] = arr[i]
            print(arr)
            if arr[i] == 0 and i + count + 1 < len(arr):
                arr[i + count + 1] = 0
                print(arr)

    print(arr)


if __name__ == '__main__':
    duplicateZeros([8, 4, 5, 0, 0, 0, 0, 7])
    duplicateZeros([0, 1, 7, 6, 0, 2, 0, 7])  # [0, 0, 1, 7, 6, 0, 0, 2]
    duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
    duplicateZeros([0, 1])
    duplicateZeros([0, 1, 0])
    duplicateZeros([1, 1, 0, 1])
    duplicateZeros([1, 1, 0, 1, 1])
