def two_sum(input_list: list, target_sum: int) -> list[tuple[int, int]]:
    """
    Return all non-overlapping pairs from a list of integers that sum to a target value
    second_solution : extra space, O(n) time
    """
    if not input_list:
        return []
    target_dict = {}
    final_list : list[tuple[int,int]] = []
    for i, num in enumerate(input_list):
        complement: int = target_sum - num
        if complement in target_dict:
            final_list.append((complement, num))
            target_dict.pop(complement)
        else:
            target_dict[num] = i
    return final_list


sample_list = [1,-2,-3,4,1,2]
print(two_sum(sample_list, 7))
print(two_sum(sample_list, 3))
print(two_sum(sample_list, 0))
print(two_sum(sample_list, -5))
