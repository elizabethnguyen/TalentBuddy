def compute_sqrt(n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    # Using Newton's Method!
    xVal = 1
    
    for i in xrange(10):
        xVal = .5 * (xVal + n//xVal)
        
    print int(xVal / 1)
