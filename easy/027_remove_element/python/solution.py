class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        newNums = []
        for num in nums:
            if num == val:
                continue
            else:
                newNums.append(num)

        for i in range(len(newNums)):
            nums[i] = newNums[i]

        return len(newNums)