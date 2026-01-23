from .task_11 import BloomFilter


def test_BloomFilter():
    bloom = BloomFilter(32)
    str1 = "0123456789"
    bloom.add(str1)
    assert bloom.is_value(str1) is True
    
    bloom = BloomFilter(32)
    str1 = "1234567890"
    bloom.add(str1)
    assert bloom.is_value(str1) is True

    bloom = BloomFilter(32)
    str1 = "2345678901"
    bloom.add(str1)
    assert bloom.is_value(str1) is True
    
    bloom = BloomFilter(32)
    str1 = "3456789012"
    bloom.add(str1)
    assert bloom.is_value(str1) is True

    bloom = BloomFilter(32)
    str1 = "4567890123"
    bloom.add(str1)
    assert bloom.is_value(str1) is True

    bloom = BloomFilter(32)
    str1 = "5678901234"
    bloom.add(str1)
    assert bloom.is_value(str1) is True

    bloom = BloomFilter(32)
    str1 = "6789012345"
    bloom.add(str1)
    assert bloom.is_value(str1) is True

    bloom = BloomFilter(32)
    str1 = "7890123456"
    bloom.add(str1)
    assert bloom.is_value(str1) is True

    bloom = BloomFilter(32)
    str1 = "8901234567"
    bloom.add(str1)
    assert bloom.is_value(str1) is True

    bloom = BloomFilter(32)
    str1 = "9012345678"
    bloom.add(str1)
    assert bloom.is_value(str1) is True