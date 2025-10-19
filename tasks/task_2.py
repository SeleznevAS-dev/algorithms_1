def digital_rain(col: str) -> str:
    balance = 0
    balances = {0: -1}
    max_len = 0
    start = 0
    for i in range(len(col)):
        if col[i] == "0":
            balance -= 1
        elif col[i] == "1":
            balance += 1

        if balance in balances and i - balances[balance] >= max_len:
            max_len = i - balances[balance]
            start = balances[balance] + 1
        else:
            balances[balance] = i

    if max_len == 0:
        return ""
    return col[start : start + max_len]
