var lengthOfLongestSubstring = function (s) {
  // Initialize a variable to keep track of the maximum length of the substring
  let longest = 0;
  // Initialize an object to keep track of the characters in the current substring
  let seen = {};
  // Initialize a variable to keep track of the start of the current substring
  let start = 0;
  // Iterate through the string
  for (let i = 0; i < s.length; i++) {
    // Get the current character
    let char = s[i];
    // If the current character has been seen before
    if (seen[char]) {
      // Update the start of the current substring
      start = Math.max(start, seen[char]);
    }
    // Update the maximum length of the substring
    longest = Math.max(longest, i - start + 1);
    // Add the current character and its position to the seen object
    seen[char] = i + 1;
  }
  return longest;
};

// Time Complexity O(n) and Space Complexity O(k) where k is the size of the character set
