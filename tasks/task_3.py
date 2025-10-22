def EEC_help(arr1: list[int], arr2: list[int]) -> bool:
    if len(arr1) != len(arr2):
        return False
    dct = {}
    for i in arr1:
        if not dct.get(i):
            dct[i] = 1
        else:
            dct[i] += 1

    for i in arr2:
        if dct.get(i):
            dct[i] -= 1

    for _, value in dct.items():
        if value != 0:
            return False

    return True
