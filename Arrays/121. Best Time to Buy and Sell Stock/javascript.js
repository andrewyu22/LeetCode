var maxProfit = function (prices) {
  // Initialize minPrice as Infinity and maxProfit as 0
  let minPrice = Infinity;
  let maxProfit = 0;
  // Iterate over the prices array
  for (let i = 0; i < prices.length; i++) {
    // Update minPrice with the min between current and previous minPrice
    minPrice = Math.min(minPrice, prices[i]);
    // Update maxProfit with the max between current maxProfit and the difference between current price and minPrice
    maxProfit = Math.max(maxProfit, prices[i] - minPrice);
  }
  return maxProfit;
};

//Time complexity: O(n) & Space complexity: O(1)
