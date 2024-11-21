class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        minlen = min(map(len, strs))
        max_common_prefix = ""
        for i in range(minlen):
            if len(set([s[i] for s in strs])) == 1:
                max_common_prefix += strs[0][i]
            else:
                break
        return max_common_prefix
