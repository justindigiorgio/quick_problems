"""
Collection of Project Euler Problems 1-19
"""


def p1(k):
    "Find all multiples of 3 or 5 below k. Small enough to brute force"
    lst = list(range(1, k))
    return sum(list(filter(p1_helper, lst)))


def p1_helper(n):
    "returns if n is a multiple of 3 or 5"
    # 3 goes first because short circuit. 3 < 5 => more multiples of 3
    return n % 3 == 0 or n % 5 == 0


def p2(k):
    "finds the sum of the even Fibbonacci terms less than k"
    # log(4e6)/log(phi) ~= 31 -> 35 terms
    lst = fib(35)
    assert(lst[-1] > k)
    def criteria(i):
        "even and less than k"
        return i % 2 == 0 and i < k
    lst = list(filter(criteria, lst))
    return sum(lst)


def fib(n):
    "gives Fibonacci first n fibbonacci numbers starting with 1,2"
    assert(n >= 0)
    if n == 0:
        return []
    if n == 1:
        return [1]
    return fib_helper([1,2], n-2)

def fib_helper(lst,n):
    if n == 0:
        return lst
    lst.append(lst[-1] + lst[-2])
    return fib_helper(lst, n-1)

def sieve(k):
    "Finds primes up to k"
    lst = list(range(0,k+1))
    m = 0
    for i in range(2, round(k ** 0.5)+1): # possible primes
        print("index: ",i, "value: ",lst[i])
        if lst[i] == 0:
            print("continuing")
            continue
        else:
            # not sure if faster to do for loop here with fixed k / lst[i] or while is better?

    return lst

def main():
    assert p1(1000) == 233168
    assert p2(4000000) == 4613732
    print(sieve(100))


if __name__ == "__main__":
    main()

