# Relex Solutions - Live Coding Interview Task
## Problem: Longest Substring Without Repeating Characters
Given a string `s`, find the length of the **longest substring** without repeating characters.
### Examples:
**Example 1:**
Input: s = "abcabcbb" Output: 3 Explanation: The answer is "abc", with the length of 3.

**Example 2:**
Input: s = "bbbbb" Output: 1 Explanation: The answer is "b", with the length of 1.

**Example 3:**
Input: s = "pwwkew" Output: 3 Explanation: The answer is "wke", with the length of 3.

**Example 4:**
Input: s = "" Output: 0

### Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
## Requirements:
1. **Implement an efficient solution** - Use a sliding window approach
2. **Time Complexity:** O(n)
3. **Space Complexity:** O(min(m, n)) where m is the character set size
4. **Error Handling:** Handle edge cases (empty string, single char, all unique, etc.)
5. **Test Cases:** Write comprehensive test cases
6. **Code Quality:** Clean, readable code with comments
## Deliverable:
Create a solution file: `solution.py`
The file should contain:
- Function: `lengthOfLongestSubstring(s: str) -> int`
- Comprehensive test cases
- Proper documentation
## Time Limit:
This is a live coding task. Complete implementation with tests should be submitted.
