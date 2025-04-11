def submitted(firstWord, secondWord):
    '''
    Time complexity: O(nlogn)
    Space complexity: O(1)
    '''

    return sorted(firstWord) == sorted(secondWord) # O(nlogn)


firstWord = "anagram"
secondWord = "nagaram"
print(f"Are Anagrams: {submited(firstWord, secondWord)}")