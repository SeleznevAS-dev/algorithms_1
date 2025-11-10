def matrix(m: int, n: int, matrix: list[list[int]]) -> list[int]:
    ans = []
    n_cur = 0
    for m_cur in range(m):
        ans.append(matrix[n_cur][m_cur])
    n_cur += 1

    m_cycle = m - 1
    n_cycle = n - 1

    while len(ans) < m * n:
        for n_cur in range(n_cur, n_cur + n_cycle):
            ans.append(matrix[n_cur][m_cur])
        m_cur -= 1
        n_cycle -= 1

        for m_cur in range(m_cur, m_cur - m_cycle, -1):
            ans.append(matrix[n_cur][m_cur])
        n_cur -= 1
        m_cycle -= 1

        for n_cur in range(n_cur, n_cur - n_cycle, -1):
            ans.append(matrix[n_cur][m_cur])
        m_cur += 1
        n_cycle -= 1

        for m_cur in range(m_cur, m_cur + m_cycle):
            ans.append(matrix[n_cur][m_cur])
        n_cur += 1
        m_cycle -= 1

    return ans
