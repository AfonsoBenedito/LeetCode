def submitted(strs):
    '''
    Time complexity: O(n)
    Space complexity: O(n)
    '''

    result = {}

    for s in strs:
        alphabet = [0] * 26
        for c in s:
            alphabet[ord(c) - ord("a")] += 1

        if result.get(tuple(alphabet)):
            result[tuple(alphabet)].append(s)
        else:
            result[tuple(alphabet)] = [s]

    return list(result.values())

strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

print(f"Nums1: {submited(strs1)}")
print(f"Nums2: {submited(strs2)}")
print(f"Nums3: {submited(strs3)}")