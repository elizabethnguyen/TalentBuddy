def nth_number(v, n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    counter = [0] * (max(v)+1)
    for i in v:
        counter[i] += 1
    j = 0
    
    for i in xrange(max(v)+1):
        if counter[i] != 0:
            if j == len(v) - n: 
                print i
            j += 1
