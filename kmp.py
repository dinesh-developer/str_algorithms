def _create_lps_array(pattern):
    """
    Build the LPS (Longest Proper Prefix which is also Suffix) array
    
    Args:
        pattern (str): The pattern string 
    Returns:
        list: List of integers representing LPS values
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # length of the previous longest prefix suffix

    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # Backtrack
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_match(text, pattern):
    """
    Find all occurrences of pattern in text using KMP algorithm

    Args:
        text (str): The main text to search within.
        pattern (str): The pattern to search for.

    Returns:
        list: A list of starting indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)
    result = []

    if m == 0: # Empty pattern always matches at every position
        return list(range(n + 1))
    
    if m > n:
        return result

    lps = _create_lps_array(pattern)

    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            result.append(i - j)  # match found
            j = lps[j - 1]  # continue searching

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]  # use LPS to skip comparisons
            else:
                i += 1
    return result


# Time complexity = O(n+m) for creating lps & iterating over text
# Space Complexity = O(m) for storing lps


# text = 'bacbababacaca'
# pattern = 'ababaca'

# text = "AABAACAADAABAABA"
# pattern = "AABA"

text = "ababcababcabc"
pattern = "abc"

result = kmp_match(text,pattern)
if result:
    print(f"Pattern found at indices: {result}")
else:
    print("Pattern not found")






# More about searching. Now that we have our lps array, we use it to efficiently search the Text.

# Initialize two pointers:
    # i: Pointer for the Text (starts at 0).
    # j: Pointer for the Pattern (starts at 0).
# Loop while i is less than N (length of Text):
    # If text[i] matches pattern[j]:
        # Increment both i and j. (We found a match for the current characters).
    # If j reaches M (length of Pattern):
        # SUCCESS! We found an occurrence of the pattern. The match starts at i - j.
        # To find all occurrences, we don't stop. We need to "reset" j using the lps array: j = lps[j - 1]. This is crucial because the pattern might overlap itself (e.g., finding "ABAB" in "ABABCABAB").
    # If text[i] does NOT match pattern[j]:
        # If j is not 0: 
            # This means we had some characters matched (j > 0), but a mismatch occurred. Instead of starting j from 0 (like brute force), we use the lps array to jump j to lps[j - 1]. This effectively shifts the pattern while maintaining the longest already-matched prefix. The i pointer does not move back.
        # If j is 0: 
            # This means the very first character of the pattern didn't match the current character in the text. We simply move to the next character in the text (i increments). The j remains 0.