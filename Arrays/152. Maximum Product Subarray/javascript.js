var maxProduct = function (nums) {
  // Initialize a variable to keep track of the current max product
  let currentMax = nums[0];
  // Initialize a variable to keep track of the current min product
  let currentMin = nums[0];
  // Initialize a variable to keep track of the overall max product
  let overallMax = nums[0];
  // Iterate through the array starting from the second element
  for (let i = 1; i < nums.length; i++) {
    // Store the current max and min products in temporary variables
    let tempMax = currentMax;
    let tempMin = currentMin;
    // Update the current max product by taking the maximum of the current element, current max product times the current element, and current min product times the current element
    currentMax = Math.max(
      nums[i],
      tempMax * nums[i],
      tempMin * nums[i]
    );
    // Update the current min product by taking the minimum of the current element, current max product times the current element, and current min product times the current element
    currentMin = Math.min(
      nums[i],
      tempMax * nums[i],
      tempMin * nums[i]
    );
    // Update the overall max product by taking the maximum of the current max product or the overall max product
    overallMax = Math.max(overallMax, currentMax);
  }
  return overallMax;
};

// Time Complexity: O(n) & Space Complexity: O(1)
