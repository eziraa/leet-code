class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0 or len(s) > 1000:
            return ""

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_palin = ""
        for i in range(len(s)):
            odd_palindrome = expand_from_center(i, i)
            if len(odd_palindrome) > len(max_palin):
                max_palin = odd_palindrome

            even_palindrome = expand_from_center(i, i + 1)
            if len(even_palindrome) > len(max_palin):
                max_palin = even_palindrome

        return max_palin
