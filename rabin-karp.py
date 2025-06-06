def rabin_karp_match(text, pattern):
    """
    Performs pattern matching Rabin-Karp Algorithm.
    
    Args: 
        text (str): The main text to search within.
        pattern (str): The pattern to search for.
    Returns:
        list: A list of starting indices where the pattern is found in the text.

    To make it case insensitive: 
        text = text.lower()
        pattern = pattern.lower()

    Convert the pattern and substrings of the text into hash values.
    Compare hashes first, and only if they match, do a full character check (to avoid hash collisions).
    Use a *rolling hash* to compute the next window hash in constant time instead of recalculating from scratch.
    
    The formula for the rolling hash is:
        hash = (d * previous_hash + new_char - old_char * h) % q
        d = number of characters in the input alphabet (often 256 for ASCII)
        q = a large prime number to avoid collisions (eg-101)
        h = d^(m-1) % q (used to remove the leftmost char)
    """
    n = len(text)
    m = len(pattern)
    d = 256  # ASCII character set
    q = 101  # A prime number
    h = pow(d, m-1, q)  # d^(m-1) % q
    pattern_hash = 0  # Hash of the pattern
    text_window_hash = 0  # Hash of current text window
    result = []

    if m == 0: # Empty pattern always matches at every position
        return list(range(n + 1))
    
    if m > n:
        return result
    
    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_window_hash = (d * text_window_hash + ord(text[i])) % q

    for i in range(n-m+1):
        if pattern_hash == text_window_hash:
            if text[i:i+m] == pattern:
                result.append(i)

        # Calculate hash for next window of text (only if not the last window)
        if i<n-m:
            text_window_hash = (d * (text_window_hash - ord(text[i]) * h) + ord(text[i+m])) % q
            if text_window_hash < 0:
                text_window_hash += q

    return result


# Time complexity O((n-m+1)*m) = O(n*m)


# text = 'xxxxyzabcdeabtvabcyg'
# pattern = 'abc'

text = "ababcababcabc"
pattern = "abc"

result = rabin_karp_match(text, pattern)

if result:
    print(f"Pattern found at indices: {result}")
else:
    print("Pattern not found")