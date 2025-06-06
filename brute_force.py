def brute_force_match(text, pattern):
    """
    Performs pattern matching using brute force.
    
    Args: 
        text (str): The main text to search within.
        pattern (str): The pattern to search for.
    Returns:
        list: A list of starting indices where the pattern is found in the text.
    
    To make it case insensitive: 
        text = text.lower()
        pattern = pattern.lower()

    We continue this process (incrementing i and trying to match the Pattern) until i reaches a point where the remaining part of the Text is shorter than the Pattern.
    """
    n = len(text)
    m = len(pattern)
    result = []

    if m == 0: # Empty pattern always matches at every position
        return list(range(n + 1))
    
    if m > n:
        return result

    for i in range(n-m+1):
        match_found = True
        for j in range(m):
            if text[i+j] != pattern[j]:
                match_found = False
                break

        if match_found:
            result.append(i)

    return result


# Time complexity O((n-m+1)*m) = O(n*m)
# Space complexity O(1)


text = "ababcababcabc"
pattern = "abc"

# text = "test this test string with test again"
# pattern = "test"

# text = 'xxxxyzabcdeabtvabcyg'
# pattern = 'abc'

result = brute_force_match(text, pattern)

if result:
    print(f"Pattern found at indices: {result}")
else:
    print("Pattern not found")