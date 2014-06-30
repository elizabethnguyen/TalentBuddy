def balanced_brackets(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    counter = 0
    for i in s:
        if i == "(":
            counter += 1
        if i == ")":
            counter -= 1
        if counter < 0:
            print "Unbalanced"
            break
    if counter == 0:
        print "Balanced"
    elif counter > 0:
        print "Unbalanced"
