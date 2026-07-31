def sortByFrequency(arr):
    freq = {}
    first = {}

    # Count frequency and store first occurrence
    for i, num in enumerate(arr):
        freq[num] = freq.get(num, 0) + 1
        if num not in first:
            first[num] = i

    # Sort by frequency (descending), then first occurrence (ascending)
    arr.sort(key=lambda x: (-freq[x], first[x]))

    return arr