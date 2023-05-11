import numpy
# Rick tosses 20 coins, Morty tosses 21. What is the probability Rick tosses more heads?

def factorial(n):
    assert(n >= 0)
    if n == 0:
        return 1
    return n * factorial(n-1)

def choose(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))

def morty_cdf_lst():
    "returns a list of probabilities that morty flips i heads of less, where i is the index"
    lst = [choose(21, i) for i in range(0,22)]
    lst = [i * 0.5 ** 21 for i in lst]
    # following line should equal 1
    # print(sum(lst))
    for i in range(1,22):
        lst[i] += lst[i-1]

    return lst


def rick_pdf_lst():
    lst = [choose(20,k) * 0.5 ** 20 for k in range(0,21)]
    # following line should equal 1
    # print(sum(lst))
    return lst


def run():
    rick = numpy.random.binomial(20, 0.5)
    morty = numpy.random.binomial(21, 0.5)
    if rick > morty:
        return 1
    return 0

def simulation(k):
    rick = 0
    i = 0
    while i < k:
        rick += run()
        i += 1
    return rick

def main():
    m = morty_cdf_lst()
    r = rick_pdf_lst()
    for i in range(1, 21):
        # prob rick rolls i heads and morty rolls i - 1 or less heads
        r[i] = r[i] * m[i-1]
    print("Theoretical Probaility:",sum(r))

    k = 5000000
    results = simulation(k)
    print("Experimental Probability:", results/k)


if __name__ == "__main__":
    main()