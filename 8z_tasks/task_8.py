def army_communication_matrix(n: int, matrix: list[list[int]]) -> str:
    possible_matrix = []
    for i in range(2, n):
        possible_matrix.append(i)

    prefix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prefix[i][j] = (
                prefix[i - 1][j]
                + prefix[i][j - 1]
                - prefix[i - 1][j - 1]
                + matrix[i - 1][j - 1]
            )

    indexes = {}
    for m in possible_matrix:
        for i in range(n - m + 1):
            for j in range(n - m + 1):
                sub_sum = (
                    prefix[i + m][j + m]
                    - prefix[i + m][j]
                    - prefix[i][j + m]
                    + prefix[i][j]
                )
                indexes[(j, i, m)] = sub_sum

    last_item = indexes.popitem()
    ans = last_item[0]
    mx = last_item[1]
    for item, value in indexes.items():
        if value >= mx:
            ans = item
            mx = value
    return " ".join(str(i) for i in ans)
