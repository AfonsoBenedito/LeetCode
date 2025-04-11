def submitted(nums):
    '''
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    numsSet = set(nums) # O(n)
    if len(nums) == len(numsSet): # O(1)
        return False
    return True

nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

print(f"Nums1: {submited(nums1)}")
print(f"Nums2: {submited(nums2)}")
print(f"Nums3: {submited(nums3)}")