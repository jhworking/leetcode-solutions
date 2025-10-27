class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num in nums:
            if counts[num] == 1:
                return num