class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize an array of the same length as nums with all elements set to 1
        result = [1 for _ in range(len(nums))]
        # Initialize a variable to keep track of the product so far
        productSoFar = 1
        # Iterate through the array from left to right
        for i in range(len(nums)):
            # Multiply the current element of the result array with the product so far and store it in the result array
            result[i] *= productSoFar
            # Update the product so far by multiplying it with the current element of the nums array
            productSoFar *= nums[i]
        # Reset the product so far to 1
        productSoFar = 1
        # Iterate through the array from right to left
        for i in range(len(nums)-1,-1,-1):
            # Multiply the current element of the result array with the product so far and store it in the result array
            result[i] *= productSoFar
            # Update the product so far by multiplying it with the current element of the nums array
            productSoFar *= nums[i]
        return result

# Time & Space Complexity: O(n)