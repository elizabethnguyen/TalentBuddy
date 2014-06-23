def relative_sort(v):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    sortedList = []
    for num in v:
        if num < 0:
         sortedList.append(num)
            
    for num in v:
        if num >= 0:
            sortedList.append(num)
            
    for num in sortedList:
        print num
