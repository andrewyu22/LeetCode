var getSum = function (a, b) {
  // Iterate until there is no carry
  while (b !== 0) {
    // Carry now contains common set bits of a and b
    let carry = a & b;
    // Sum of bits of a and b where at least one of the bits is not set
    a = a ^ b;
    // Carry is shifted by one so that adding it to a gives the required sum
    b = carry << 1;
  }
  return a;
};

// Time & Space Complexity: O(1)
