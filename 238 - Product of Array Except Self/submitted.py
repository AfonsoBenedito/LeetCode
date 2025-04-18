def get_prefix(input_list: list[int]) -> list[int]:
    result = [1] * len(input_list)

    prefix = 1
    for i in range(len(input_list)):
        result[i] = input_list[i] * prefix
        prefix *= input_list[i]

    return result

def get_postfix(input_list: list[int]) -> list[int]:
    result = [1] * len(input_list)

    postfix = 1
    for i in range(len(input_list) - 1, -1, -1):  # Reverse loop
        result[i] = input_list[i] * postfix
        postfix *= input_list[i]

    return result


def submitted(input_list: list[int]) -> list[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    prefix_list = get_prefix(input_list)
    postfix_list = get_postfix(input_list)

    result = []

    for i in range(len(input_list)):
        if i == 0:
            result.append(postfix_list[i + 1])
        elif i == len(input_list) - 1:
            result.append(prefix_list[i - 1])
        else:
            result.append(prefix_list[i - 1] * postfix_list[i + 1])

    return result


nums1 = [1,2,3,4]  # [24,12,8,6]
nums2 = [-1,1,0,-3,3]  # [0,0,9,0,0]

print(f"Input 1: {submitted(nums1)}")
print(f"Input 2: {submitted(nums2)}")