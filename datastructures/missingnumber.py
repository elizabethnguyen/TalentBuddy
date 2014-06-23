def find_missing_number(v):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    dict = {}
    dict[0] = "true"
    for i in xrange(1, len(v)+1):
        dict[i] = "false"
    for i in v:
        dict[i] = "true"
    for i in dict:
        if dict[i] == "false":
            print i
