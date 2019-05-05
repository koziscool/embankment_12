import time


def e4():

    def is_pal( n ):
        return n == int( str(n)[::-1] )

    max_pal = -999999
    for a in xrange(100, 1000):
        for b in xrange(a, 1000):
            if a*b > max_pal and is_pal( a*b ):
                max_pal = a*b
    return max_pal

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 4 solution is:",  e4()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
