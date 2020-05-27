""""
KorKux Solution Module
"""
from typing import List


class Solution:
    """
    Class representing the challenge solution
    """
    def duplicate_zeros(self, arr: List[int]):
        """
        Given an array number doubles the zeros of the array without modifying the size of the array

        Arguments:
            arr {List[int]} -- [Array of numbers that will duplicate the zeros it contains]
        """
        stack_array_invert = arr[::-1]  # O(n)
        arr_index = 0
        length = len(arr)
        while arr_index < length: # O(n)
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
