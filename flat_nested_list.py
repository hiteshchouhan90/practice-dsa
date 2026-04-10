def flat_nested_list(nested_list: list) -> list:
    final_list: list = []
    for element in nested_list:
        if isinstance(element, list) and len(element) > 0:
            final_list.extend(flat_nested_list(element))
        else:
            final_list.append(element)
    return final_list

sample_list_1 = []
sample_list_2 = [1,2,[],3,[]]
sample_list_3 = [1,2,3,4]
sample_list_4 = [1,2,3,[4,5,6],[7,8,9]]

print(flat_nested_list(sample_list_1))
print(flat_nested_list(sample_list_2))
print(flat_nested_list(sample_list_3))
print(flat_nested_list(sample_list_4))