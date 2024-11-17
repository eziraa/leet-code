class Solution(object):

    def isPalinrome(self, x):
        """
        :type x: str
        : rtype: bool
        """
        s = str(x)
        if s != s[::-1]:
            return False
        return True
