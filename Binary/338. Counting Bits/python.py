# dynamic programming approach
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize an array to store the number of 1 bits for each number from 0 to num
        dp = [0] * (n+1)
        for i in range(1, n+1):
            # The number of 1 bits for the current number is equal to the number of 1 bits for (i & (i - 1)) + 1
            dp[i] = dp[i & (i - 1)] + 1
        return dp

# Time & Space Comeplxity: O(n)