function containsDuplicate(nums) {
  // Create a set to store the elements
  const elements = new Set();

  // Iterate through the list
  for (const num of nums) {
    // If the element is already in the set, return true
    if (elements.has(num)) {
      return true;
    }
    // Otherwise, add the element to the set
    else {
      elements.add(num);
    }
  }

  // If the loop completes, return false
  return false;
}

// Time & Space Complexity: O(n)
