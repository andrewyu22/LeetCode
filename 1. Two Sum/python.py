class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary to store the values and their indices
        d = {}
        # Iterate through the array
        for i, num in enumerate(nums):
            # Check if the complement of the current number (target - num) exists in the dictionary
            if target - num in d:
                # If it does, return the indices of the complement and the current number
                return [d[target - num], i]
            # If the complement does not exist, add the current number and its index to the dictionary
            d[num] = i