def longest_improvement(grades):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    counter = 1
    maxStreak = 0
    for i in xrange(len(grades)-1):
        if grades[i] >= grades[i-1]:
            counter += 1
        elif counter > maxStreak:
            maxStreak = counter
            counter = 1
            
    print maxStreak
