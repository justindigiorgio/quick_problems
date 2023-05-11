import time

def pi_estimation(t, run_time):
    pi = 3
    n = 0
    series = 0
    while(time.time() - t < run_time):
        series += ((-1) ** n) / ((2*n+3)**3 - (2 * n + 3))
        n += 1
    pi += series * 4
    return(str(pi))

def pi():
    return "3.1415926535897932384"

def hamming(a,b):
    lst = zip(a,b)
    lst = [1 if i[0]==i[1] else 0 for i in lst]
    return lst

def main():
    i = 0
    while(i < 5):
        start = time.time()
        est = pi_estimation(start, .995)
        end = time.time()
        if end - start < 1:
            print("Good Time")
            print(est)
            print(pi())
            lst = hamming(pi(), est)
            print("Number of correct digits", lst.index(0)-1)
            return
        else:
            print("Bad Time: Retrying")
        i += 1

if __name__ == "__main__":
    main()

