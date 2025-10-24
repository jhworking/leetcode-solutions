class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracketsDict = { "(" : ")", "[" : "]", "{" : "}" }
        stack = []
        if s.startswith("]") or s.startswith("}") or s.startswith(")") or len(s)%2 == 1:
            return False
        else:
            for bracket in s:
                if bracket in bracketsDict:
                    stack.append(bracket)
                else:
                    if not stack:
                        return False
                    top = stack.pop()
                    if bracketsDict[top] != bracket:
                        return False            
            if stack:
                return False  
                
        return True