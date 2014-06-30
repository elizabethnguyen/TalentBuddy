def sort_students(numbers):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    isSorted = False
    while(not isSorted):
        isSorted = True
        for i in range(1, len(numbers)):
            if numbers[i-1] > numbers[i]:
                temp = numbers[i-1]
                numbers[i-1] = numbers[i]
                numbers[i] = temp
                isSorted = False
    for i in numbers:
        print i
