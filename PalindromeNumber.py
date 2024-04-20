class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        length = len(x_str) 
        for i in range(length):
            if (x_str[i] != x_str[length - 1 - i]):
                return False
        return True
        