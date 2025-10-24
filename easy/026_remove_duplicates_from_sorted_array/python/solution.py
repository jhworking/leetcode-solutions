class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqueArray = []
        for num in nums:
            if num not in uniqueArray:
                uniqueArray.append(num)
                
        for i in range(len(uniqueArray)):
            nums[i] = uniqueArray[i]
            
        return len(uniqueArray)
        