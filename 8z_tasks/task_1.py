def white_walkers(village: str) -> bool:
    digits_indexes = []
    for i in range(len(village)):
        if village[i].isdigit():
            digits_indexes.append(i)
    if len(digits_indexes) < 2:
        return False
    result = False
    for i in range(len(digits_indexes) - 1):
        num1 = int(village[digits_indexes[i]])
        num2 = int(village[digits_indexes[i + 1]])
        if (num1 + num2 == 10) and (
            list(village[digits_indexes[i] : digits_indexes[i + 1]]).count("=") == 3
        ):
            result = True
        elif (num1 + num2 == 10) and (
            list(village[digits_indexes[i] : digits_indexes[i + 1]]).count("=") != 3
        ):
            result = False
            break
    return result
