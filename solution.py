def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Uses a sliding window approach with a hash map to track character positions.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
        
    Time Complexity: O(n) - single pass through the string
    Space Complexity: O(min(m, n)) where m is the character set size
    """
    if not s:
        return 0
    
    char_index = {}
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        char = s[right]
        
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


def test_lengthOfLongestSubstring():
    """Comprehensive test cases for the function."""
    
    # Example 1: Basic case with repeating characters
    assert lengthOfLongestSubstring("abcabcbb") == 3
    print("✓ Test 1 passed: 'abcabcbb' -> 3 (substring 'abc')")
    
    # Example 2: All same characters
    assert lengthOfLongestSubstring("bbbbb") == 1
    print("✓ Test 2 passed: 'bbbbb' -> 1 (substring 'b')")
    
    # Example 3: Mixed repeating pattern
    assert lengthOfLongestSubstring("pwwkew") == 3
    print("✓ Test 3 passed: 'pwwkew' -> 3 (substring 'wke')")
    
    # Example 4: Empty string
    assert lengthOfLongestSubstring("") == 0
    print("✓ Test 4 passed: '' -> 0 (empty string)")
    
    # Edge case: Single character
    assert lengthOfLongestSubstring("a") == 1
    print("✓ Test 5 passed: 'a' -> 1 (single character)")
    
    # Edge case: All unique characters
    assert lengthOfLongestSubstring("abcdefg") == 7
    print("✓ Test 6 passed: 'abcdefg' -> 7 (all unique)")
    
    # Edge case: Two characters, one repeating
    assert lengthOfLongestSubstring("au") == 2
    print("✓ Test 7 passed: 'au' -> 2 (two unique)")
    
    # Edge case: Space and special characters
    assert lengthOfLongestSubstring("a b c") == 3
    print("✓ Test 8 passed: 'a b c' -> 3 (includes spaces)")
    
    # Edge case: Numbers
    assert lengthOfLongestSubstring("123121") == 3
    print("✓ Test 9 passed: '123121' -> 3 (substring '312')")
    
    # Edge case: Long repeating at end
    assert lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzabcdefg") == 26
    print("✓ Test 10 passed: Full alphabet repeated -> 26")
    
    # Edge case: Repeating at beginning
    assert lengthOfLongestSubstring("aabcdef") == 6
    print("✓ Test 11 passed: 'aabcdef' -> 6 (substring 'bcdef')")
    
    # Edge case: Multiple groups
    assert lengthOfLongestSubstring("dvdf") == 3
    print("✓ Test 12 passed: 'dvdf' -> 3 (substring 'vdf')")
    
    print("\n✅ All 12 tests passed!")


if __name__ == "__main__":
    test_lengthOfLongestSubstring()
