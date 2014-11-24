list1 = []
list2 = []

for x in range(10):
    list1.append(x+1)
    list2.append(x+1)

    
print "1st list"
print list1
print "2st list"
print list2
print "list.extend"
list1.extend(list2)
print list1
print "list.pop(x)"
list1.pop(4)
print list1
print "list.pop"
list1.pop
print list1
print "list.remove(x)"
list1.remove(5)
print list1
print ""
print len(list1)
print ""
print list1.count(1)
