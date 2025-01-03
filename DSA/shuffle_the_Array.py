from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Shuffle the array by interleaving the first half with the second half.

        param:
            nums: List of integers to shuffle.
            n: Length of the first half of the list.
        
        return:
            List of integers after shuffling.
        """
        shuffled_nums = []
        # Loop through the first half of the list
        for i in range(n):
            # Append the ith element from the first half
            shuffled_nums.append(nums[i])
            # Append the ith element from the second half
            shuffled_nums.append(nums[i + n])
        return shuffled_nums

# Example usage
sol = Solution()
print(sol.shuffle([3, 6, 9, 4, 5, 8], 3))  # Output: [3, 4, 6, 5, 9, 8]
print(sol.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))  # Output: [1, 4, 2, 3, 3, 2, 4, 1]
print(sol.shuffle([1, 1, 2, 2], 2))  # Output: [1, 2, 1, 2]