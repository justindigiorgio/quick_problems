import random

"Rick tosses 20 coins, Morty tosses 21. What is the probability Rick tosses more heads?"


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
    # print(sum(lst))
    print(lst)


def run():
    rick = random.choices([0, 1], k=20)
    heads_rick = sum(rick)
    morty = random.choices([0, 1], k=21)
    heads_morty = sum(morty)
    return [heads_rick, heads_morty]


def simulation(k):
    r = 0
    i = 0
    while i < k:
        trial = run()
        if trial[0] > trial[1]:
            r += 1
        i += 1
    return r


def main():
    morty_cdf_lst()
    # k = 100000
    # results = simulation(k)
    # print(results/k)


if __name__ == "__main__":
    main()