def submitted(input_string: str) -> bool:
    '''
    Time complexity: O(n)
    Space complexity: O(n)
    '''

    stack = []

    parentheses = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in input_string:
        if char in parentheses:
            if len(stack) == 0:
                return False
            if parentheses[char] != stack[-1]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0

s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"

print(f"Input1: {submitted(s1)}")  # True
print(f"Input2: {submitted(s2)}")  # True
print(f"Input3: {submitted(s3)}")  # False
print(f"Input4: {submitted(s4)}")  # True