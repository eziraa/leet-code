

class Solution(object):

    def maxProduct(self, nums):
        if len(nums) < 1 or len(nums) > 20000:
            return 0
        if len(nums) == 1:
            return nums[0]

        max_product = 0
        max_num = max(nums)

        for num in nums:
            if num > 10 or num < -10:
                return 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                max_product = max(max_product, self.bulk_product(nums[i:j]))

        return max(max_product, max_num)

    def bulk_product(self, nums):
        result = 1
        for num in nums:
            result *= num
        return result
