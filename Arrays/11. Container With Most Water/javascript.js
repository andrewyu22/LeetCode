var maxArea = function (height) {
  // Initialize two pointers, one at the beginning and one at the end of the array
  let left = 0;
  let right = height.length - 1;
  // Initialize a variable to keep track of the maximum area
  let maxArea = 0;
  // While the left pointer is less than the right pointer
  while (left < right) {
    // Calculate the area between the two pointers
    let area = Math.min(height[left], height[right]) * (right - left);
    // Update the max area if the current area is greater than the max
    maxArea = Math.max(maxArea, area);
    // If the left pointer's value is less than the right pointer's value
    if (height[left] < height[right]) {
      // Move the left pointer to the right
      left++;
    } else {
      // Otherwise, move the right pointer to the left
      right--;
    }
  }
  // Return the max area
  return maxArea;
};

// Time Complexity: O(n) & Space Complexity: O(1)
