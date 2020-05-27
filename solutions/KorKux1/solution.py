from typing import List


class Solution:

    def duplicate_zeros(self, arr: List[int]):
        stack_array_invert = arr[::-1]  # O(n)
        arr_index = 0
        length = len(arr)        
        while (arr_index < length): # O(n)
            value = stack_array_invert.pop()
            
            if value == 0:
                arr[arr_index] = value

                if arr_index + 1 < length:
                    arr[arr_index + 1] = value
                arr_index += 1        
            else:
                arr[arr_index] = value
            arr_index += 1
        # Complex = O(n) + O(n) = O(2n) = O(n)
