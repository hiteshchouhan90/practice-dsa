def  is_anagram(s: str, t: str) -> bool:
        count_dict: dict[str, int] = {}
        if len(s) != len(t):
            return False
        for char in t:
            count_dict[char] = count_dict.get(char, 0) + 1
        for char in s:
            if char not in count_dict or count_dict[char] == 0:
                return False
            count_dict[char] -= 1
        return True

print(is_anagram("aab", "aba"))
print(is_anagram("aweab", "agbba"))
print(is_anagram("acddf", "acddf"))


# Better approach - based on frequency map but it only works for fixed type of inputs
def is_anagram(s: str, t: str) -> bool:
    
    if (len(s) != len(t)):
         return False
    count_array = 26 * [0]
    for i in range(len(s)):
         count_array[ord(s[i]) - ord('a')] += 1
         count_array[ord(t[i]) - ord('a')] -= 1
    for i in count_array:
         if i != 0:
              return False
    return True
    
print(is_anagram("aab", "aba"))
print(is_anagram("aweab", "agbba"))
print(is_anagram("acddf", "acddf"))

