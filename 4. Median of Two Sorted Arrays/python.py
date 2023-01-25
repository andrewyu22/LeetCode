class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # This function finds the median of two sorted arrays (nums1 and nums2)
        # Initialize an empty list to store the combined elements of nums1 and nums2
        arr = []
        # Store the total length of both input lists
        totalLen = len(nums1) + len(nums2)

        # If the total length of both lists is 1, return the single element in either list
        if totalLen == 1:
            return nums1[0] if len(nums1) == 1 else nums2[0]

        # Determine the length of the new list (arr) based on whether the total length is even or odd
        if totalLen % 2 == 0:
            arr_len = (totalLen / 2) + 1
        else:
            arr_len = (totalLen+1) / 2

        # Initialize variables to keep track of the current index of nums1 and nums2
        i = 0
        j = 0
        # While the new list (arr) is not yet at the desired length
        while len(arr) < arr_len:
            # Compare the current element of nums1 and nums2
            if i < len(nums1) and j < len(nums2):
                # If the current element of nums1 is less than or equal to the current element of nums2
                if nums1[i] <= nums2[j]:
                    # Add the current element of nums1 to the new list (arr)
                    arr.append(nums1[i])
                    # Increment the index of nums1
                    i += 1
                else:
                    # Add the current element of nums2 to the new list (arr)
                    arr.append(nums2[j])
                    # Increment the index of nums2
                    j += 1
            # If nums1 has reached the end
            elif i >= len(nums1):
                # Add the remaining elements of nums2 to the new list (arr)
                arr.append(nums2[j])
                j += 1
            # If nums2 has reached the end
            else:
                # Add the remaining elements of nums1 to the new list (arr)
                arr.append(nums1[i])
                i += 1
        print(arr)
        # If the total length of both input lists is even, return the average of the two middle elements
        # If the total length of both input lists is odd, return the middle element
        return (arr[-1] + arr[-2]) / 2 if totalLen % 2 == 0 else arr[-1]

# Time & Space Complexity is O(n)