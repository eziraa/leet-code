class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) > 50000:
            return 0
        letters = [c for c in s]
        long = 0
        longest = []
        for i in range(len(letters)):
            letter = letters[i]
            if letter not in longest:
                longest.append(letter)
            else:
                longest = longest[longest.index(letter)+1:]
                longest.append(letter)
            long = max(long, len(longest))
        return long


result = Solution().lengthOfLongestSubstring('au')
print(result)
