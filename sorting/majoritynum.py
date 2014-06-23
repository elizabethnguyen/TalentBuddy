def majority(v):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    counter = [0] * (max(v) + 1)
    majorityNum = False
    
    for num in v:
        counter[num] += 1
        
    for idx in xrange(max(v)+1):
        if counter[idx] > (len(v)/2):
            print idx
            majorityNum = True

    if majorityNum == False:
        print "None"
