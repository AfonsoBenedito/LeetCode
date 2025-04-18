def submitted(nums, target):
    '''
    Time complexity:
    Space complexity:
    '''
    count = {}
    buckets = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = count.get(n, 0) + 1
    for key, value in count.items():
        buckets[value].append(key)

    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == target:
                return result


nums1 = [1,1,1,2,2,3]
k1 = 2

nums2 = [1]
k2 = 1

print(f"Nums1: {submitted(nums1, k1)}")
print(f"Nums2: {submitted(nums2, k2)}")