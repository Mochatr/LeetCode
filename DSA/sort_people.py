"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

 

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
"""
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n = len(names)

        for i in range(n-1):
            for j in range(n-i-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]

        return names

# Example
mySolution = Solution()
names = ["Michael", "Charlie", "Leon"]
heights = [190, 165, 179]
print(mySolution.sortPeople(names, heights))