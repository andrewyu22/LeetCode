class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMax = nums[0]
        # Initialize a variable to keep track of the current min product
        currentMin = nums[0]
        # Initialize a variable to keep track of the overall max product
        overallMax = nums[0]
        # Iterate through the array starting from the second element
        for i in range(1,len(nums)):
            # Store the current max and min products in temporary variables
            tempMax = currentMax
            tempMin = currentMin
            # Update the current max product by taking the maximum of the current element, current max product times the current element, and current min product times the current element
            currentMax = max(nums[i], tempMax * nums[i], tempMin * nums[i])
            # Update the current min product by taking the minimum of the current element, current max product times the current element, and current min product times the current element
            currentMin = min(nums[i], tempMax * nums[i], tempMin * nums[i])
            # Update the overall max product by taking the maximum of the current max product or the overall max product
            overallMax = max(overallMax, currentMax)
        # return the overall max product
        return overallMax

# Time Complexity: O(n) & Space Complexity: O(1)