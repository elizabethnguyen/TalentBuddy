def fizzbuzz(n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    for i in xrange(1,n+1):
        if i % 15 == 0:
            print 'FizzBuzz'
        elif i % 3 == 0:
            print 'Fizz'
        elif i % 5 == 0:
            print'Buzz'
        else:
            print i
