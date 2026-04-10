from typing import Iterator, Any

def flat_nested_list(nested_list: list) -> Iterator[Any]:
    if not nested_list:
        return None
    for element in nested_list:
        if isinstance(element, list):
            yield from flat_nested_list(element)
        else:
            yield element


sample_list_1 = []
sample_list_2 = [1,2,[],3,[]]
sample_list_3 = [1,2,3,4]
sample_list_4 = [1,2,3,[4,5,6],[7,8,9]]

print(list(flat_nested_list(sample_list_1)))
print(list(flat_nested_list(sample_list_2)))
print(list(flat_nested_list(sample_list_3)))
print(list(flat_nested_list(sample_list_4)))

