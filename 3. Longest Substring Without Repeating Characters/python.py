class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a variable to keep track of the maximum length of the substring
        longest = 0
        # Initialize a dictionary to keep track of the characters in the current substring
        seen = {}
        # Initialize a variable to keep track of the start of the current substring
        start = 0
        # Iterate through the string
        for i in range(len(s)):
            # Get the current character
            char = s[i]
            # If the current character has been seen before
            if char in seen:
                # Update the start of the current substring
                start = max(start, seen[char])
            # Update the maximum length of the substring
            longest = max(longest, i - start + 1)
            # Add the current character and its position to the seen dictionary
            seen[char] = i+1
        return longest

# Time Complexity O(n) and Space Complexity O(k) where k is the size of the character set