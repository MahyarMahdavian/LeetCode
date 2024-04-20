class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        common = strs[0]
        i = 0
        while i < len(strs):
            word = strs[i]
            if common == "" or word == "":
                return ""
            complete = True
            for j in range(min(len(common), len(word))):
                if word[j] == common[j]:
                    pass
                else:
                    complete = False
                    break
            if complete:
                common = common[0:j+1]
            else:
                common = common[0:j]
            i += 1

        return common