def _build_bad_character_table(pattern):
    """
    Build the bad character table for Boyer-Moore algorithm.
    
    Args:
        pattern (str): The pattern string 
    Returns:
        dict: Dictionary mapping characters to their rightmost position in pattern
    """
    bad_char = {}
    for i, c in enumerate(pattern):
        bad_char[c] = i  # last occurrence of char in pattern
    return bad_char



def boyer_moore_search(text, pattern):
    """
    Performs pattern matching using Boyer-Moore.
    
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

    bad_char = _build_bad_character_table(pattern)
    s = 0  # shift of the pattern with respect to text

    while s <= n - m:
        j = m - 1

        # Compare from end of pattern to beginning
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            result.append(s)  # Match found
            s += m if s + m < n else 1  # Shift entire pattern if no more text left
        else:
            # Mismatch: shift pattern using bad character rule
            bad_char_index = bad_char.get(text[s + j], -1)
            shift = max(1, j - bad_char_index)
            s += shift

    return result


text = "ababcababcabc"
pattern = "abc"

result = boyer_moore_search(text, pattern)
if result:
    print(f"Pattern found at indices: {result}")
else:
    print("Pattern not found")


# Key Idea: We have two shift rules for this algorithm
    # 1. Bad Character Rule (or Last Occurrence Rule): simple (we implemented this one)
    # 2. Good Suffix rule is mathematically more complex
