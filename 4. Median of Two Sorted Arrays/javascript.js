var findMedianSortedArrays = function (nums1, nums2) {
  // Initialize an empty array to store the combined elements of nums1 and nums2
  let arr = [];
  // Store the total length of both input arrays
  let totalLen = nums1.length + nums2.length;
  // If the total length of both arrays is 1, return the single element in either array
  if (totalLen === 1) return nums1.length === 1 ? nums1[0] : nums2[0];

  // Determine the length of the new array (arr) based on whether the total length is even or odd
  let arr_len =
    totalLen % 2 === 0 ? totalLen / 2 + 1 : Math.ceil(totalLen / 2);

  // Initialize variables to keep track of the current index of nums1 and nums2
  let i = 0;
  let j = 0;
  // While the new array (arr) is not yet at the desired length
  while (arr.length < arr_len) {
    // Compare the current element of nums1 and nums2
    if (i < nums1.length && j < nums2.length) {
      // If the current element of nums1 is less than or equal to the current element of nums2
      if (nums1[i] <= nums2[j]) {
        // Add the current element of nums1 to the new array (arr)
        arr.push(nums1[i]);
        // Increment the index of nums1
        i++;
      } else {
        // Add the current element of nums2 to the new array (arr)
        arr.push(nums2[j]);
        // Increment the index of nums2
        j++;
      }
      // If nums1 has reached the end
    } else if (i >= nums1.length) {
      // Add the remaining elements of nums2 to the new array (arr)
      arr.push(nums2[j]);
      j++;
      // If nums2 has reached the end
    } else {
      // Add the remaining elements of nums1 to the new array (arr)
      arr.push(nums1[i]);
      i++;
    }
  }
  // If the total length of both input arrays is even, return the average of the two middle elements
  // If the total length of both input arrays is odd, return the middle element
  return totalLen % 2 === 0
    ? (arr[arr.length - 1] + arr[arr.length - 2]) / 2
    : arr[arr.length - 1];
};

// Time & Space Complexity is O(n)
