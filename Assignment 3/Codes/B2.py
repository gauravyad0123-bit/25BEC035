import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
original[0][0] = 99
print(shallow)  # [[99, 2], [3, 4]]
print(deep)     # [[1, 2], [3, 4]]