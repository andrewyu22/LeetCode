var climbStairs = function (n) {
  // create an array to store the number of ways to reach each step
  let dp = new Array(n + 1);
  // initialize the first two steps with 1 way each
  dp[0] = 1;
  dp[1] = 1;
  // loop through the remaining steps
  for (let i = 2; i <= n; i++) {
    // the number of ways to reach the current step is the sum of the ways to reach the previous two steps
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  // return the number of ways to reach the nth step
  return dp[n];
};

// Time & Space Complexity: O(n)
