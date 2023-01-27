class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the final result
        result = []
        # Sort the input list
        nums.sort()
        
        # Iterate through the list, starting from the first element
        for i in range(len(nums)-2):
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Initialize two pointers, left and right
            left, right = i+1, len(nums)-1
            while left < right:
                # If the sum of the three elements is equal to zero
                if nums[i] + nums[left] + nums[right] == 0:
                    # Append the three elements to the result list
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate elements
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    # Move the pointers
                    left += 1
                    right -= 1
                # If the sum is less than zero
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                # If the sum is greater than zero
                else:
                    right -= 1
        # Return the final result
        return result

# Time Complexity: O(n^2) & Space Complexity: O(n)