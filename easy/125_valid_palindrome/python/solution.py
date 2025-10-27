class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        lowercase_string = s.lower()
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', lowercase_string)
        
        if cleaned_string[0::] == cleaned_string[::-1]:
            return True
        else:
            return False