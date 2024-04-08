# %%
import numpy as np
from numpy import array
import itertools

class VectorCombinator:
    @staticmethod
    def non_empty_value(arr, empty):
        for element in arr:
            if np.any(element != empty):
                return element
        return None

    @staticmethod
    def group_non_empties(arr, empty):
        arr = [array(list(e)) for k, e in itertools.groupby(arr)]
        output_array = []
        for e in arr:
            if empty in e:
                output_array.extend(e)
            else:
                output_array.append(e)

        return np.array(output_array).tolist()

    @staticmethod
    def concatenate_arrays(arr):
        return np.concatenate([e.ravel() for e in arr])

    @staticmethod
    def combinations(row, max_move, ones, empty):
        print("Combinations", row, max_move, ones, empty)
        solutions = []
        ones_positions = [i for i, x in enumerate(row) if np.array_equal(x, ones)]
        none_positions = [i for i, x in enumerate(row) if np.array_equal(x, empty)]

        def backtrack(current_row, ones_index, moves):
            if ones_index == len(ones_positions):
                current_row = array(current_row)
                solutions.append(np.concatenate([e.ravel() for e in current_row]))
                return
            for move in range(1, max_move + 1):
                if ones_positions[ones_index] + move in none_positions:
                    new_row = current_row.copy()
                    new_row[ones_positions[ones_index]] = empty
                    new_row[ones_positions[ones_index] + move] = ones
                    backtrack(new_row, ones_index + 1, 0)
            backtrack(current_row, ones_index + 1, 0)

        backtrack(row, 0, 0)
        return solutions