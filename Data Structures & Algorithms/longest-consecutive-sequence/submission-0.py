class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        counter = 0

        for number in seen:
            sequence_starter = number - 1 

            if sequence_starter not in seen:
                sequence_starter = number
                current_length = 1

                next_number = sequence_starter+1

                while next_number in seen:
                    current_length+=1
                    sequence_starter = next_number
                    next_number = sequence_starter+1
                counter = max(counter, current_length)

        return counter
            
        
            
        