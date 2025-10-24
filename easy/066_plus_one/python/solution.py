class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        newDigitString = "".join(str(digit) for digit in digits)
        newDigit = int(newDigitString) + 1
        newDigitList = []
        for num in str(newDigit):
            newDigitList.append(int(num))
        
        return newDigitList