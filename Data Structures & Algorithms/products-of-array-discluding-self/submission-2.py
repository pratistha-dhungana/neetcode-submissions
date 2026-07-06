class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = []
        left = []
        result = []
        right_product=1
       
        

        for i in range(len(nums)):
            if i == 0:
                left_product = 1
                left.append(left_product)
            else:
                left_product *= nums[i-1]
                left.append(left_product)
            
        for i in range(len(nums)-1,-1,-1): 
            if i == len(nums) - 1:
                right_product = 1
                right.append(right_product)
            else:
                right_product *= nums[i+1]
                right.append(right_product)
        right.reverse()
            
        for i in range(len(nums)):
            final_prod = left[i] * right[i]
            result.append(final_prod)
        return result
        