def two_numbers_sum(v, sum):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    isPaired = False
    
    for idxI in xrange(len(v)):
        for idxJ in xrange(len(v)):
            if (v[idxI] + v[idxJ] == 0 or v[idxI] + v[idxJ] == sum) and idxI < idxJ and not isPaired:
                print 1
                isPaired = True
                
    if isPaired == False:
        print 0
