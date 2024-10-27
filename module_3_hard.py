data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def sum_all(data_structure):
    summa = 0
    if isinstance(data_structure, (list, set, tuple)):
        for i in data_structure:
            summa += sum_all(i)
    elif isinstance(data_structure, dict):
        for k, v in data_structure.items():
            summa += int(len(k))
            summa += v
    elif isinstance(data_structure, str):
        summa += int(len(data_structure))
    elif isinstance(data_structure, (float, int)):
        summa += data_structure
    return summa


result = sum_all(data_structure)

print(result)
