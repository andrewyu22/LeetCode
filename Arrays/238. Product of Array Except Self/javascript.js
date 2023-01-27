var productExceptSelf = function (nums) {
  // Initialize an array of the same length as nums with all elements set to 1
  let result = Array(nums.length).fill(1);
  // Initialize a variable to keep track of the product so far
  let productSoFar = 1;
  // Iterate through the array from left to right
  for (let i = 0; i < nums.length; i++) {
    // Multiply the current element of the result array with the product so far and store it in the result array
    result[i] *= productSoFar;
    // Update the product so far by multiplying it with the current element of the nums array
    productSoFar *= nums[i];
  }
  // Reset the product so far to 1
  productSoFar = 1;
  // Iterate through the array from right to left
  for (let i = nums.length - 1; i >= 0; i--) {
    // Multiply the current element of the result array with the product so far and store it in the result array
    result[i] *= productSoFar;
    // Update the product so far by multiplying it with the current element of the nums array
    productSoFar *= nums[i];
  }
  return result;
};

// Time & Space Complexity: O(n)
