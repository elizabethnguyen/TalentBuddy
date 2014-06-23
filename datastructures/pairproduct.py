def max_prod(v):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    max = 0
    for i in v:
        for j in v[2:]:
            n = i * j
            if n % 3 == 0:
                if n > max:
                    max = n
    print max
