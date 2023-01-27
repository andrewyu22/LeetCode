var maxSubArray = function (nums) {
  // Initialize a variable to keep track of the current max sum
  let currentMax = nums[0];
  // Initialize a variable to keep track of the overall max sum
  let overallMax = nums[0];
  // Iterate through the array starting from the second element
  for (let i = 1; i < nums.length; i++) {
    // Update the current max sum by taking the maximum of the current element or the current max sum plus the current element
    currentMax = Math.max(nums[i], currentMax + nums[i]);
    // Update the overall max sum by taking the maximum of the current max sum or the overall max sum
    overallMax = Math.max(overallMax, currentMax);
  }
  return overallMax;
};

// Time Complexity: O(n) & Space Complexity: O(1)
