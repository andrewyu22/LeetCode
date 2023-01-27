// dynamic programming approach
var countBits = function (n) {
  // Initialize an array to store the number of 1 bits for each number from 0 to num
  let dp = new Array(n + 1).fill(0);
  for (let i = 1; i <= n; i++) {
    // The number of 1 bits for the current number is equal to the number of 1 bits for (i & (i - 1)) + 1
    dp[i] = dp[i & (i - 1)] + 1;
  }
  return dp;
};

// Time & Space Comeplxity: O(n)
