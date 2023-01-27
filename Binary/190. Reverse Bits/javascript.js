/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  let reversed = 0;
  for (let i = 0; i < 32; i++) {
    // Shift the input number to the right to get the rightmost bit
    let bit = n & 1;
    // Shift the reversed number to the left to make room for the next bit
    reversed = (reversed << 1) | bit;
    // Shift the input number to the right to get the next bit
    n = n >> 1;
  }
  return reversed >>> 0;
};

// Time and Space Complexity is: O(1)
