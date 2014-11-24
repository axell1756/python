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
print "len(list)"
print len(list1)
print "list.count(x)"
print list1.count(1)
del list1[:]
print "del list[:]"
print list1
