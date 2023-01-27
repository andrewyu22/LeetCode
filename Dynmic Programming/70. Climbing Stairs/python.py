class Solution:
    def climbStairs(self, n: int) -> int:
        # create a list to store the number of ways to reach each step
        dp = [0]*(n+1)
        # initialize the first two steps with 1 way each
        dp[0], dp[1] = 1, 1
        # loop through the remaining steps
        for i in range(2, n+1):
            # the number of ways to reach the current step is the sum of the ways to reach the previous two steps
            dp[i] = dp[i-1] + dp[i-2]
        # return the number of ways to reach the nth step
        return dp[n]

# Time & Space Complexity: O(n)