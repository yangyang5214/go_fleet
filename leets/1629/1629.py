# -*- coding: UTF-8 -*-


class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        r = keysPressed[0]
        flag = releaseTimes[0]

        length = len(releaseTimes)
        for index in range(1, length):
            item = keysPressed[index]
            time = releaseTimes[index] - releaseTimes[index - 1]
            if time > flag:
                r = item
                flag = time
            elif time == flag:
                r = max(item, r)
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.slowestKey([9, 29, 49, 50], "cbcd"))
    print(s.slowestKey([12, 23, 36, 46, 62], "spuda"))
