var twoSum = function (nums, target) {
  // Initialize a map to store the values and their indices
  let map = new Map();
  // Iterate through the array
  for (let i = 0; i < nums.length; i++) {
    // Check if the complement of the current number (target - nums[i]) exists in the map
    if (map.has(target - nums[i])) {
      // If it does, return the indices of the complement and the current number
      return [map.get(target - nums[i]), i];
    }
    // If the complement does not exist, add the current number and its index to the map
    map.set(nums[i], i);
  }
};
