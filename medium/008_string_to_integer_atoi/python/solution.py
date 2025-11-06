class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip() # Strip leading white strip
        if not s:
            return 0

        sign = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]

        if not s or not s[0].isdigit():
            return 0

        num_str = ""
        for char in s:
            if char.isdigit():
                num_str += char
            else:
                break

        num = int(num_str) * sign

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN

        return num