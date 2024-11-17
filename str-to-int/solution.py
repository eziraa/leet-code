class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) <= 0:
            return 0
        if len(s) > 200:
            return s
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1

        if not s[0].isdigit():
            return 0
        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1
        s = s[:i]
        n = int(s) * sign

        return n


result = Solution().myAtoi("-91283472332")

print(result)
