# -*- coding: UTF-8 -*-

class Solution:

    def merge(self, nums1, m, nums2, n):
        """
        将 nums2 合并到 nums1

        从后往前遍历
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """
        i, j = m - 1, n - 1
        index = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[index] = nums2[j]
                j -= 1
            else:
                nums1[index] = nums1[i]
                i -= 1
            index = index - 1

        # 将 nums2 没遍历完的赋值给 nums1
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]

    def merge1(self, nums1, m, nums2, n):
        """
        将 nums2 合并到 nums1

        从前往后遍历

        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """
        if not nums2:
            return
        r = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                r.append(nums1[i])
                i += 1
            else:
                r.append(nums2[j])
                j += 1
        if i < m:
            r = r + nums1[i:m]
        elif j < n:
            r = r + nums2[j:n]

        # nums1 重新赋值
        nums1[:] = r

    def mergeTwoLists(self, list1: list, list2: list) -> list:
        """
        合并两个有序数组

        头部开始合并
        :param list1:
        :param list2:
        :return:
        """
        if not list1:
            return list2
        if not list2:
            return list1
        len_m = len(list1)
        len_n = len(list2)

        r = []
        i, j = 0, 0
        while i < len_m and j < len_n:
            if list1[i] <= list2[j]:
                r.append(list1[i])
                i += 1
            else:
                r.append(list2[j])
                j += 1

        if i < len_m:
            r = r + list1[i:]
        elif j < len_n:
            r = r + list2[j:]
        return r


if __name__ == '__main__':
    s = Solution()
    l1 = [1, 2, 4, 0, 0, 0]
    l2 = [1, 3, 4]
    s.merge(l1, 3, l2, 3)
    print(l1)

    l1 = [1, 0, 0]
    l2 = [3, 4]
    s.merge(l1, 1, l2, 2)
    print(l1)

    l1 = [1]
    l2 = []
    s.merge(l1, 1, l2, 0)
    print(l1)

    l1 = []
    l2 = [1]
    s.merge(l1, 0, l2, 1)
    print(l1)

    l1 = [2, 3, 0, 0, 0]
    l2 = [1, 1, 1]
    s.merge(l1, 2, l2, 3)
    print(l1)
