import time


def e2():
    fib = [ 1, 2 ]
    while fib[-1] < 4 * 10**6:
        fib.append( fib[-1] + fib[-2] )
    fib.pop()
    return sum( filter( lambda n: n%2==0, fib )) 

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 2 solution is:",  e2()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
