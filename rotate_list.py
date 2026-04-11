class Solution:
    #helper function to reverse list
    def reverse_list(self, input_list: list, start: int, end: int):
        while start < end:
            input_list[start], input_list[end] = input_list[end], input_list[start]
            start += 1
            end -= 1

    def rotate_list(self, input_list: list, k: int) -> list:
        """
        Left-rotate input_list by k positions in-place (no slicing).
        Works for k > n and negative k (negative treated via modulo).
        Time: O(n), Space: O(1)
        
        right rotate - (n-k)(k)
        left rotate - (k)(n-k)
        
        rotate by 2: 
            right rotate
                1,2,3,4,5,6,7 
                5,4,3,2,1,7,6

                6,7,1,2,3,4,5

            left rotate:
                1,2,3,4,5,6,7
                2,1,7,6,5,4,3

                3,4,5,6,7,1,2
        """
        n = len(input_list)

        if n <= 1:
            return input_list
        k = k % n
        if k == 0:
            return input_list

        #reverse the first k and n-k elements
        
        self.reverse_list(input_list, 0, k - 1)
        self.reverse_list(input_list, k , n - 1)
        self.reverse_list(input_list, 0, n - 1)

        return input_list


sample_list = [1,2,3,4,5,6,7,8,9]
sample_list_negative_numbers = [1,2,-3,4,-5,6,-7,8,9]

sol = Solution()
print(sol.rotate_list(sample_list.copy(), 3))   # left rotate by 3
print(sol.rotate_list(sample_list.copy(), 12))  # k > n
print(sol.rotate_list(sample_list.copy(), 0))   # k == 0 (no-op)
print(sol.rotate_list(sample_list.copy(), -2))  # negative k handled
print(sol.rotate_list(sample_list_negative_numbers.copy(), 2))