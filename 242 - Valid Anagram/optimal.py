def optimal(firstWord, secondWord):
    '''
    Time complexity: O(n)
    Space complexity: O(1)
    '''

    if len(firstWord) != len(secondWord):
        return False

    firstWordDict, secondWordDict = {}, {}

    for i in range(len(firstWord)):
        firstWordDict[firstWord[i]] = firstWordDict.get(firstWord[i], 0) + 1
        secondWordDict[secondWord[i]] = secondWordDict.get(secondWord[i], 0) + 1

    return firstWordDict == secondWordDict

firstWord = "anagram"
secondWord = "nagaram"
print(f"Are Anagrams: {optimal(firstWord, secondWord)}")