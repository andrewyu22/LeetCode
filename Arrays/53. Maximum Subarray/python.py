class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize a variable to keep track of the current max sum
        currentMax = nums[0]
        # Initialize a variable to keep track of the overall max sum
        overallMax = nums[0]
        # Iterate through the array starting from the second element
        for i in range(1,len(nums)):
            # Update the current max sum by taking the maximum of the current element or the current max sum plus the current element
            currentMax = max(nums[i], currentMax + nums[i])
            # Update the overall max sum by taking the maximum of the current max sum or the overall max sum
            overallMax = max(overallMax, currentMax)
        return overallMax

# Time Complexity: O(n) & Space Complexity: O(1)