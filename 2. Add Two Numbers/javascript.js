/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  // Initialize a dummy node and a pointer to keep track of the current position
  let dummyHead = new ListNode(0);
  let curr = dummyHead;
  // Initialize a carry variable
  let carry = 0;
  // Iterate through both linked lists
  while (l1 !== null || l2 !== null) {
    // Get the value of the current node in l1 or 0 if l1 is shorter
    let x = l1 !== null ? l1.val : 0;
    // Get the value of the current node in l2 or 0 if l2 is shorter
    let y = l2 !== null ? l2.val : 0;
    // Add the values and the carry
    let sum = x + y + carry;
    // Update the carry
    carry = Math.floor(sum / 10);
    // Append the current digit to the result linked list
    curr.next = new ListNode(sum % 10);
    curr = curr.next;
    // Move to the next nodes
    if (l1 !== null) {
      l1 = l1.next;
    }
    if (l2 !== null) {
      l2 = l2.next;
    }
  }
  // If there is still a carry, append it to the result linked list
  if (carry > 0) {
    curr.next = new ListNode(carry);
  }
  return dummyHead.next;
};
