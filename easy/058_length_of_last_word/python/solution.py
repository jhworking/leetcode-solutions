class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cleanedString = s.strip()
        words = cleanedString.split(" ")
        
        return len(words[-1])