#Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm
from collections.abc import Iterable

lst = ['A', 'B', ['C','D', ['E', 'F']], 'G', 'H', ['I',['J', ['K', 'L', "M"]]]]
# items is an array object
def flatten_list(items, ignore_types=(str, bytes)):
  for v in items:
    if isinstance(v, Iterable) and not isinstance(v, ignore_types):
      yield from flatten_list(v)
    else:
      yield v

print(list(flatten_list(lst)))