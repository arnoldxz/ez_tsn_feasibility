# %%
from matrix_gen import FlowProcessor
from flows_parser import FlowParser
from vector_combinations import VectorCombinator
import numpy as np
from numpy import array
import itertools
import matplotlib.pyplot as plt
# %%
flows = FlowParser.parse_flows_from_json("flowsConfig.json")
matrix_resolution = FlowProcessor.resolution(flows)
empty = np.array([0], dtype=object)
matrix = FlowProcessor.process_flows(flows)

def max_range(i):
    return int((flows[i].deadline / matrix_resolution) - 1)


row_combs = []
for i in range(len(matrix)):
    grouped_vector = VectorCombinator.group_non_empties(array(matrix[i]), empty)
    non_empty = VectorCombinator.non_empty_value(grouped_vector, empty)
    combinations = VectorCombinator.combinations(grouped_vector, max_range(i), non_empty, empty)
    row_combs.append(combinations)

# %%
res = itertools.product(*row_combs)

# %%
def overlapping(v):
    return np.any(v > 1)

scheduled = []
i = 0
for r in res:
    column_sums = np.sum(r, axis=0)
    if not overlapping(column_sums):
        scheduled.append(r)
        break
    i = i+1

# %%
if len(scheduled) > 0:
    print(f"\nFeasible! \nIteration: {i}\nSchedules: {scheduled}")
else:
    print("X Infeasible")