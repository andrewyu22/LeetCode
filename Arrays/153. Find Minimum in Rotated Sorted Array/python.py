    # Edge case: if the array is empty or has only one element, return that element
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    # Initialize the left and right pointers
    left, right = 0, len(nums) - 1
    # If the array is not rotated, the minimum element is the first element
    if nums[right] > nums[0]:
        return nums[0]
    # Binary search for the minimum element
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        # If the middle element is greater than the element to its right, the minimum element is to the right of the middle element
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        # If the middle element is less than the element to its left, the minimum element is to the left of the middle element
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        # If the middle element is greater than the first element, the minimum element is to the right of the middle element
        if nums[mid] > nums[0]:
            left = mid + 1
        # If the middle element is less than the first element, the minimum element is to the left of the middle element
        else:
            right = mid - 1