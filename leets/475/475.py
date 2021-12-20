# -*- coding: UTF-8 -*-


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        m = {}
        for heater in heaters:
            for house in houses:
                if house in m:
                    cur = min(abs(heater - house), m.get(house))
                else:
                    cur = abs(heater - house)
                m[house] = cur

        r = 0
        for _, v in m.items():
            r = max(r, v)
        return r

    def findRadius1(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters)
        r = -1
        for house in houses:
            min_distance = self.binarySearch(heaters, house)
            if r < 0:
                r = min_distance
            else:
                r = max(min_distance, r)
        return r

    def binarySearch(self, heaters, house):
        """
        查找当前离 house 最近 的  heater
        :param heaters:
        :param house:
        :return:
        """
        l = 0
        r = len(heaters) - 1
        if heaters[r] <= house:
            return house - heaters[r]
        while l < r:
            mid = l + (r - l + 1) // 2
            if heaters[mid] > house:
                r = mid - 1
            else:
                l = mid
        cur = abs(house - heaters[l])
        cur_next = abs(house - heaters[l + 1]) if l + 1 < len(heaters) else cur + 1
        return min(cur, cur_next)


if __name__ == '__main__':
    s = Solution()

    houses = [1, 5]
    heaters = [10]

    houses = [1, 2, 3]
    heaters = [2]
    houses = [1, 5]
    heaters = [2]

    houses = [1, 2, 3, 4]
    heaters = [1, 4]
    print(s.findRadius1(houses, heaters))
