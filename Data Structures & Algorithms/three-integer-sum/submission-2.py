class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #target = 0 
        results = []
        

        nums.sort()

        
        for i in range(len(nums)):
            first = nums[i]

            # for duplicates, second element, if this is same to the one before the first element then cont
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i+1 # second element
            right = len(nums)-1 # last element

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left +=1 
                elif total > 0:
                    right -=1 
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left+=1 
                    right -=1 

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                        
            
        
        return results
