from math import floor
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = []
        total.extend(nums1)
        total.extend(nums2)
        total.sort()
        isEven = len(total) % 2 == 0
        mid = floor(len(total) / 2)
        if isEven:
            return (total[mid] + total[mid-1]) / 2
        else:
            return total[mid]


result = Solution().findMedianSortedArrays([1, 3], [2])

print(result)

result = Solution().findMedianSortedArrays([1, 2], [3, 4])

print(result)

result = Solution().findMedianSortedArrays([0, 0], [0, 0])

print(result)
