class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize a variable to store the reversed bits
        reversed = 0
        # Iterate through all 32 bits of the input number
        for i in range(32):
            # Get the rightmost bit of the input number
            bit = n & 1
            # Shift the reversed number to the left and add the next bit
            reversed = (reversed << 1) | bit
            # Shift the input number to the right
            n = n >> 1
        return reversed

# Time and Space Complexity is: O(1)