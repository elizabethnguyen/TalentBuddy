def count_occurrences(v, k):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    occurrences = [0] * (max(v) + 1)
    
    for num in v:
        occurrences[num] += 1
        
    print occurrences[k]
