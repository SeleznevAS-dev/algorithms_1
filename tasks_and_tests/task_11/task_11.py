class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_arr = ["0"] * f_len
        self.num_hash1 = 17
        self.num_hash2 = 223

    def _number_to_mask(self, num):
        b = ""
        while num != 1:
            b += str(num % 2)
            num //= 2
        b += "1"
        return b

    def _add_mask_to_arr(self, mask):
        for i in range(-1, -len(mask) - 1, -1):
            self.bit_arr[i] = str(int(self.bit_arr[i]) | int(mask[i]))

    def _if_mask_in_arr(self, mask):
        for i in range(-1, -len(mask) - 1, -1):
            num = int(mask[i])
            if num == 1 and not int(self.bit_arr[i]) & num:
                return False

        return True

    def hash1(self, str1):
        # 17
        res = 0
        for c in str1:
            code = ord(c)
            res *= self.num_hash1
            res += code
            res %= self.filter_len

        res = self._number_to_mask(res)
        return res

    def hash2(self, str1):
        # 223
        res = 0
        for c in str1:
            code = ord(c)
            res *= self.num_hash2
            res += code
            res %= self.filter_len

        res = self._number_to_mask(res)
        return res

    def add(self, str1):
        mask1 = self.hash1(str1)
        self._add_mask_to_arr(mask1)
        mask2 = self.hash2(str1)
        self._add_mask_to_arr(mask2)

    def is_value(self, str1):
        mask1 = self.hash1(str1)
        mask1_res = self._if_mask_in_arr(mask1)
        mask2 = self.hash2(str1)
        mask2_res = self._if_mask_in_arr(mask2)

        if mask1_res and mask2_res:
            return True

        return False
