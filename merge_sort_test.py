import merge_sort
import random

array = random.sample(range(10000), 100)
print(array)
print("\n")
sorted_array = merge_sort.merge_sort(array)
print(sorted_array)
