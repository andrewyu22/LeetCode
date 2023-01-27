var hammingWeight = function (n) {
  // Initialize a variable to store the number of 1 bits
  let count = 0;
  // Iterate until the input number is 0
  while (n !== 0) {
    // Get the rightmost bit of the input number by performing a bitwise AND with 1
    // If the bit is 1, increment the count
    count += n & 1;
    // Shift the input number to the right by using a bitwise shift
    n = n >>> 1;
  }
  return count;
};

// Time and Space Complexity: O(1)
