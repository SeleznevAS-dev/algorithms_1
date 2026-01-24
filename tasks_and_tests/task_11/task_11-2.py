from .task_11 import BloomFilter


# Course task number: 11
# Lesson task number: 11.2
# Short name: MultiBloomFilter
class ModifiedBloomFilter(BloomFilter):
    def __init__(self, f_len, num_hash1=None, num_hash2=None):
        self.filter_len = f_len
        self.bits = int(2 << (f_len - 1))
        self.num_hash1 = num_hash1 or 17
        self.num_hash2 = num_hash2 or 223


class MultiBloomFilter:
    def __init__(self, bloom_filters: list[ModifiedBloomFilter]):
        self.bloom_filters = bloom_filters

    def add(self, str1):
        for bloom_filter in self.bloom_filters:
            bloom_filter.add(str1)

    def is_value(self, str1):
        for bloom_filter in self.bloom_filters:
            if bloom_filter.is_value(str1) is False:
                return False
        return True


def test_MultiBloomFilter():
    bloom1 = ModifiedBloomFilter(32, num_hash1=17, num_hash2=223)
    bloom2 = ModifiedBloomFilter(32, num_hash1=37, num_hash2=251)
    multi_bloom = MultiBloomFilter([bloom1, bloom2])

    str1 = "0123456789"
    multi_bloom.add(str1)
    assert multi_bloom.is_value(str1) is True

    str2 = "1234567890"
    multi_bloom.add(str2)
    assert multi_bloom.is_value(str2) is True


# Вероятность ложного срабатывания должна уменьшаться с увеличение количества фильтров


# Course task number: 11
# Lesson task number: 11.3
# Short name: BloomFilterWithRemove
class BloomFilterWithRemove(BloomFilter):
    def remove(self, str1):
        mask1 = self.hash1(str1)
        self.bits = self.bits & ~mask1
        mask2 = self.hash2(str1)
        self.bits = self.bits & ~mask2


def test_BloomFilterWithRemove():
    bloom = BloomFilterWithRemove(32)
    str1 = "0123456789"
    bloom.add(str1)
    assert bloom.is_value(str1) is True
    bloom.remove(str1)
    assert bloom.is_value(str1) is False


# Course task number: 11
# Lesson task number: 11.4
# Short name: BloomFilterReverse
class BloomFilterReverse(BloomFilter):
    def get_original_num_range(self):
        mn = self.filter_len
        mx = -1

        for i in range(self.filter_len):
            bit_mask = 1 << i
            if (self.bits & bit_mask) != 0:
                if i < mn:
                    mn = i
                if i > mx:
                    mx = i

        return mn, mx


def test_BloomFilterReverse():
    bloom = BloomFilterReverse(32)
    str1 = "0123456789"
    bloom.add(str1)
    mn, mx = bloom.get_original_num_range()
    assert mn >= 0 and mx < bloom.filter_len


# Смог только приблизительно определить возможный диапазон индексов хешей

# Рефлексия
# 5. Словарь с использованием упорядоченного списка по ключу.
# Сделал правильно.
