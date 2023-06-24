from numpy.random import uniform


class Coin:
    def __init__(self, p):
        self._p =p

    def flip(self, n=1):

        sequence = uniform(low=0,high=1, size=n)
        sequence = [1 if x <= self._p else 0 for x in sequence ]
        return sequence

    def wait_time(self, sub):
        """
        returns the number of flips to reach the subsequence
        :param seq: must be in the form of List[OneOf(0,1)]
        :return: int
        """
        len_seq = len(sub)
        flips = Coin.flip(self, n = 4 * len_seq ** 2) # arbitrary length. doesnt matter
        # print(sub, "in", flips)
        i = 0
        while True: # sliding window
            if flips[i:i+len_seq] == sub: # if we find the subsequence
                return i + len_seq
            if i + len_seq + 1 == len(flips): # amortized doubling flips size
                # print("adding more flips")
                flips += Coin.flip(self, n=len(flips))
            i += 1

    def average_wt(self, seq, iter=10000):
        count = 0
        for i in range(iter):
            count += Coin.wait_time(self, seq)
        return count/iter


if __name__ == "__main__":
    c = Coin(1/2)
    print(c.average_wt([1, 1])) # theoretically 6
    print(c.average_wt([1, 0])) # theoretically 4
    print(c.average_wt([1, 1, 1]))
    print(c.average_wt([1, 0, 0, 1]))
    print(c.average_wt([1, 0, 1, 0]))
    print(c.average_wt([1, 1, 1, 1]))