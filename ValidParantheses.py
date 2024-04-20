class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opened = []
        for bracket in s:
            if bracket in "([{":
                opened.append(bracket)
            elif not opened:
                return False
            elif bracket == ")" and opened[-1] == "(" or \
                 bracket == "]" and opened[-1] == "[" or \
                 bracket == "}" and opened[-1] == "{":
                 opened.pop()
            else:
                return False
        if not opened:
            return True
        else: return False