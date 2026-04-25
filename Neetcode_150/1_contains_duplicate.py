class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        freq_dict :dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
                return True
            else:
                freq_dict[num] = 1
        return False