import math
import mmh3


class BloomFilter:

    def __init__(self, n: int=1000000, p: float=0.01):
        """"
        n : number of items to be stored in the filter
        p : allowed false positive probability
        """

        if p < 0 or n < 1:
            raise ValueError("Please provide valid inputs for positional arguments n and p")

        if not isinstance(n, int):
            raise ValueError("Positional argument n needs to be an integer. "
                             "Please provide a valid input")

        self._p = p

        # list will be initialised with None to this size
        self._size = self.get_length(n, p)

        # number of hashes to calculate
        self._n_hash = self.num_hashes(self._size, n)

        # initialize empty filter
        self.filter = [0] * self._size

    def insert(self, item):
        """
        Add an item in the filter
        """
        for i in range(self._n_hash):
            location = mmh3.hash(item, i) % self._size

            # set the bit True in bit_array
            self.filter[location] = True

    def is_present(self, item):
        """
        Check if an item is in the filter
        """
        for i in range(self._n_hash):
            loc = mmh3.hash(item, i) % self._size
            if not self.filter[loc]:
                # if any location in the index is false - the item is not in the filter
                return False
        return True

    @classmethod
    def get_length(self, n, p):
        """
        Return the size of bloom-filter required
        """
        size = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(size)

    @classmethod
    def num_hashes(self, size, n):
        """
        Return the number of hash functions required
        """
        n_hash = (size / n) * math.log(2)
        return int(n_hash)

    def get_size_of_filter(self) -> float:
        """
        Return size of bloom filter
        """
        return sys.getsizeof(self.__filter) * 0.000001
