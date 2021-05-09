from bloom_filter import BloomFilter
import pytest


def test_n_hash():
    result = BloomFilter.num_hashes(size=10, n=5)
    assert result == 1


def test_get_length():
    value = BloomFilter.get_length(n=10, p=0.25)
    assert value == 28

def test_bloom_filter():

    with pytest.assertRaises(ValueError):
        blf = BloomFilter(n=-1, p=0.1)

    with pytest.assertRaises(ValueError):
        blf = BloomFilter(n=1, p=-0.1)

    with pytest.assertRaises(ValueError):
        blf = BloomFilter(n=1.0, p=0.1)

    # aiming to cause collision
    blf = BloomFilter(n=3, p=0.1)
    blf.insert("Gondor")

    assert blf.is_present("Gondor 1") == True
    assert blf.is_present("Isenguard") == False
