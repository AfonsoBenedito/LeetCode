# 49. Group Anagrams

## Meta Information
- **Difficulty:** *Medium*
- **Tags:** *Array, Hash Table, String, Sorting*

## Problem Description
Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

```
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
```

```
Example 2:
Input: strs = [""]

Output: [[""]]
```

```
Example 3:
Input: strs = ["a"]

Output: [["a"]]
```


**Constraints:**
- ```2 <= nums.length <= 10^4```
- ```0 <= strs[i].length <= 100```
- ```strs[i] consists of lowercase English letters.```


## Performance
The table below shows the performance of my solution on LeetCode:

| Metric   | Screenshot                                                                                 |
|----------|--------------------------------------------------------------------------------------------|
| Runtime  |<img src="./img/runtime.png" alt="Runtime" width="300">                                    |
| Memory   |<img src="./img/memory.png" alt="Runtime" width="300">                                     |

