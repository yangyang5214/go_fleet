class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        arrs = text.split(' ')
        length = len(arrs)
        result = []
        for index in range(0, length - 2):
            if arrs[index] == first and arrs[index + 1] == second:
                result.append(arrs[index + 2])
                index += 2
        return result
