import time


def e6():
    sum_squares = sum( map(lambda n: n*n, range(1, 101) ))
    square_sum = sum( range(1, 101) )**2
    return square_sum - sum_squares

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 6 solution is:",  e6()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
