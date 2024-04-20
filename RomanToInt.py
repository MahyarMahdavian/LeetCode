class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Numbers = { 'I' : 1, 
                    'V' : 5, 
                    'X' : 10, 
                    'L' : 50, 
                    'C' : 100, 
                    'D' : 500, 
                    'M' :1000}
        result = 0
        i = 0
        while (i < len(s)):
            if (i < len(s) - 1) and (Numbers[s[i]] < Numbers[s[i+1]]):
                result = result + Numbers[s[i+1]] - Numbers[s[i]]
                i = i + 1
            else:
                result = result + Numbers[s[i]]
            i = i + 1 

        return result