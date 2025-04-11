def encode(strs: list[str]) -> str:
		"""
		Time Complexity: O(n)
		Space Complexity: O(n)
		"""
		result = ""

		for str in strs:
			result += f"{len(str)}#{str}"

		return result

def decode(s: str) -> list[str]:
	"""
	Time Complexity: O(n)
	Space Complexity: O(n)
	"""
	i = 0
	result = []

	while i < len(s):
		j = i
		while s[j] != "#":
			j += 1

		length = s[i:j]
		i = j + 1
		j = i + int(length)

		result.append(s[i:j])
		i=j

	return result



input1 = ["nnneeetttee","code","love","you"]
input2 = ["we","say",":","yes"]

print(f"Is 1 okay: {input1 == decode(encode(input1))}")
print(f"Is 2 okay: {input2 == decode(encode(input2))}")