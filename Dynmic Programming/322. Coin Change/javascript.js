var coinChange = function (coins, amount) {
  // create an array to store the minimum number of coins for each value
  let dp = new Array(amount + 1).fill(amount + 1);
  // initialize the first value with 0 as it takes 0 coins to make 0 cents
  dp[0] = 0;
  // loop through the coins
  for (let coin of coins) {
    // loop through the values from the coin value to the total amount
    for (let i = coin; i <= amount; i++) {
      // update the minimum number of coins for the current value
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }
  // return -1 if the amount cannot be made with the given coins
  return dp[amount] > amount ? -1 : dp[amount];
};

// Time Complexity: O(a * c) where a is the amount and c is the number of coins
// Space Complexity: O(a)
