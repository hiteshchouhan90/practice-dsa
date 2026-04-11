def two_sum(input_list: list, target_sum: int) -> list[tuple]:
    """Question:
    Return all pairs from a list of integers that sum to a target value
    first solution: brute force
    """
    if not input_list:
        return None
    
    complement: int = 0
    final_list: list[tuple] = []
    for i in range(len(input_list)):
        complement = target_sum - input_list[i]
        for j in range(i+1, len(input_list)):
            if input_list[j] == complement:
                final_list.append((input_list[i],input_list[j]))
                break
    return final_list

sample_list = [1,2,3,4]
print(two_sum(sample_list, 7))
print(two_sum(sample_list, 3))
print(two_sum(sample_list, 0))