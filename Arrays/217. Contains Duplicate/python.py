class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set from the input list
        unique_nums = set(nums)
        # Compare the length of the set and the input list
        return len(unique_nums) != len(nums)

# Time & Space Complexity: O(n)