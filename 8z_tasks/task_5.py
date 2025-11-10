def massdriver(activate: list[int]) -> int:
    dct = {}
    mn = len(activate)
    for i in range(len(activate)):
        if dct.get(activate[i]) is None:
            dct[activate[i]] = i
        elif dct.get(activate[i]) < mn:
            mn = dct.get(activate[i])
    if mn == len(activate):
        mn = -1
    return mn
