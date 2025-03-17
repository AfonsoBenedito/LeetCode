def submited(nums, target):
    '''
    Time complexity: O(n)
    Space complexity: O(n)
    '''

    numsDict = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in numsDict:
            return [numsDict[diff], i]
        numsDict[num] = i

nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

print(f"Nums1: {submited(nums1, target1)}")
print(f"Nums2: {submited(nums2, target2)}")
print(f"Nums3: {submited(nums3, target3)}")