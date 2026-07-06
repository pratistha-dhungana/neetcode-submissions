class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        counter =0 
        print(seen)

        for i in range(len(nums)):
            value = nums[i]

            if value - 1 not in seen:
                chain_starter = value
                chain_counter = 1
                next_val = chain_starter + 1

                while next_val in seen:
                    chain_counter += 1 
                    next_val += 1

            
                if chain_counter > counter:
                    counter = chain_counter

        return counter
