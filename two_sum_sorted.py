def two_sum(input_list: list, target_sum: int) -> list[tuple[int, int]]:
    """
    Return all non-overlapping pairs from a list of integers that sum to a target value
    third_solution : two pointer approach, O(n log n) time and O(1) space
    """
    if not input_list:
        return []
    final_list: list[tuple[int, int]] = []
    sorted_input = sorted(input_list)
    i, j = 0, len(sorted_input) - 1
    while( i < j ):
        sum = sorted_input[i] + sorted_input[j]
        if sum == target_sum:
            final_list.append((sorted_input[i], sorted_input[j]))
            i += 1
            j -= 1
        elif sum < target_sum:
            i += 1
        elif sum > target_sum:
            j -= 1
    return final_list

 
sample_list = [1,-2,-3,4,1,2]
print(two_sum(sample_list, 7))
print(two_sum(sample_list, 3))
print(two_sum(sample_list, 0))
print(two_sum(sample_list, -5))
