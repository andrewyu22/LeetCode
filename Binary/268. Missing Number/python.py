class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Initialize a variable to store the sum of the numbers from 0 to n
        expected_sum = len(nums) * (len(nums) + 1) // 2
        # Initialize a variable to store the actual sum of the numbers in the input array
        actual_sum = sum(nums)
        # Return the difference between the expected sum and the actual sum, which is the missing number
        return expected_sum - actual_sum

# Time Complexity: O(n) & Space Complexity: O(1)