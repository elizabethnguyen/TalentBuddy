def sort_names(names):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    def getKey(item):
        return item[1]
    
    nameList = []
    
    for name in names:
        nameList.append(name.split(' '))
        
    nameList = sorted(nameList, key=getKey)
    
    for name in nameList:
        print str(name).translate(None, "'[],")
