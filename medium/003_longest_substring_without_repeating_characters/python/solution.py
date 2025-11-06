class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        setA = set()
        maxCount = 0
        count = 0
        start = 0
        
        if not s:
            return maxCount

        for end in range(len(s)):
            char = s[end]

            while char in setA:    
                setA.remove(s[start])
                start += 1
                count -= 1

            setA.add(char)
            count += 1
            maxCount = max(maxCount, count)
                    
        return maxCount