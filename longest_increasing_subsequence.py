def longest_inc_subseq(input_list: list) -> tuple:
    """
    Find the length of the longest increasing subsequence in a list of integers
    [20,30,1,5,4,3,2,3,4,5,6,7]
    """
    LIS = [1] * len(input_list)
    for i in range(len(input_list) - 1, -1, -1):
        for j in range(i+1, len(input_list)):
            if input_list[i] < input_list[j]:
                LIS[i] = max(LIS[i], 1+ LIS[j])
    return max(LIS)


sample_list = [20,30,1,5,4,3,2,3,4,5,6,7]
sample_list_negative_numbers = [1,2,-3,4,-5,6,-7,8,9]

print(longest_inc_subseq(sample_list))
print(longest_inc_subseq(sample_list_negative_numbers))
