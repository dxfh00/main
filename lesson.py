def calculate_structure_sum(data_structure):
    result = 0
    if isinstance(data_structure, int):
        result += data_structure
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            # result += calculate_structure_sum(i)
            calculate_structure_sum(i)
    elif isinstance(data_structure, str):
        result += len(data_structure)

    return result


data_structure = ['55555', [1, 3, 2, 4], '666666']


print(calculate_structure_sum(data_structure))
