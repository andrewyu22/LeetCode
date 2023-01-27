var missingNumber = function (nums) {
  // Initialize a variable to store the sum of the numbers from 0 to n
  let expectedSum = (nums.length * (nums.length + 1)) / 2;
  // Initialize a variable to store the actual sum of the numbers in the input array
  let actualSum = 0;
  // Iterate through the input array
  for (let i = 0; i < nums.length; i++) {
    // Add the current number to the actual sum
    actualSum += nums[i];
  }
  // Return the difference between the expected sum and the actual sum, which is the missing number
  return expectedSum - actualSum;
};

// Time Complexity: O(n) & Space Complexity: O(1)
