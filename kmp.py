def create_lps_array(pattern):
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

    lps = create_lps_array(pattern)

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