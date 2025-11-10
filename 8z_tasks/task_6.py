def TRC_sort(trc: list[int]) -> list[int]:
    dct = {0: [], 1: [], 2: []}
    for i in trc:
        dct[i].append(i)
    ans = []
    for i in dct.keys():
        ans.extend(dct[i])
    return ans
