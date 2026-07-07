class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0 
        results = []
        

        sorted_nums = sorted(nums)

        
        for i in range(len(sorted_nums)):
            first = sorted_nums[i]

            target = 0 - first
            
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            for j in range(i+1, len(sorted_nums)):
                second = sorted_nums[j]
                third = target - sorted_nums[j]

                if j > i+1 and sorted_nums[j] == sorted_nums[j-1]:
                    continue

                if third in sorted_nums[j+1:]:
                    results.append([first, second, third])
            
        
        return results
