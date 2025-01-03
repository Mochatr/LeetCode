from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the complement of the number and its index
        num_to_index = {}

        # Loop through each number in the list
        for index, num in enumerate(nums):
            # Calculate the needed number to reach the target
            needed = target - num
            # Check if the needed number is already seen
            if needed in num_to_index:
                # Return the current index and the index of the needed number
                return [num_to_index[needed], index]
            # Store the index of the current number
            num_to_index[num] = index
        
        # Return an empty list if no solution is found
        return []

# Example usage
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print("Output:", result)  # Output should be [0, 1]
