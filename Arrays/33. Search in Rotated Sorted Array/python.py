class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left pointer to 0 and right pointer to the last index of the array
        left, right = 0, len(nums) - 1
        # Continue the loop while left pointer is less than or equal to right pointer
        while left <= right:
            # Calculate the middle index of the array
            mid = (left + right) // 2
            # If the element at the middle index is equal to the target, return the middle index
            if nums[mid] == target:
                return mid
            # If the left half of the array is sorted
            if nums[left] <= nums[mid]:
                # Check if the target is within the range of the left and middle pointer
                if nums[left] <= target < nums[mid]:
                    # if yes, move the right pointer to the middle minus one
                    right = mid - 1
                else:
                    # if not, move the left pointer to the middle plus one
                    left = mid + 1
            # If the left half of the array is not sorted
            else:
                # Check if the target is within the range of the middle and right pointer
                if nums[mid] < target <= nums[right]:
                    # if yes, move the left pointer to the middle plus one
                    left = mid + 1
                else:
                    # if not, move the right pointer to the middle minus one
                    right = mid - 1
        # If the loop ends and we have not found the target, return -1
        return -1

# Time Complexity: O(log n) & Space Complexity: O(1)