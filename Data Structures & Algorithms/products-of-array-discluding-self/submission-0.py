class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1

        for ind in range(len(nums)):
            result[ind] = prefix
            prefix *= nums[ind]
        
        postfix = 1

        for ind in range(len(nums)-1,-1,-1):
            result[ind] *= postfix
            postfix *= nums[ind]
        
        return result