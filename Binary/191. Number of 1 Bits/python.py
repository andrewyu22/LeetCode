class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a variable to store the number of 1 bits
        count = 0
        # Iterate while n is non-zero
        while n:
            # Get the rightmost bit of the input number by performing a bitwise AND with 1
            # If the bit is 1, increment the count
            count += n & 1
            # Shift the input number to the right by using the shift operator
            n = n >> 1
        return count

# Time and Space Complexity: O(1)