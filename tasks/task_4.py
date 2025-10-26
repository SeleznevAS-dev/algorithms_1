def artificial_muscle_fibers(arr: list[int]) -> int:
    ans = 0
    reserve_arr = bytearray(8002)
    for i in range(len(arr)):
        num_byte = arr[i] // 8
        num_bit = arr[i] % 8

        if ((reserve_arr[num_byte] >> num_bit) & 1) == 0 and (
            (reserve_arr[num_byte + 4001] >> num_bit) & 1
        ) == 0:
            reserve_arr[num_byte] |= 1 << num_bit

        elif ((reserve_arr[num_byte] >> num_bit) & 1) == 1 and (
            (reserve_arr[num_byte + 4001] >> num_bit) & 1
        ) == 0:
            reserve_arr[num_byte + 4001] |= 1 << num_bit
            ans += 1

    return ans
