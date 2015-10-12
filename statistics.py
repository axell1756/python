import statistics

ran = [1,2,3,3,3,4,4,5,6,7,8,9,10]

print (statistics.mean(ran))
print (statistics.median(ran))
print (statistics.mode(ran))
print (round(statistics.stdev(ran), 1))

print (" ")

ran = [1,2,3,3,3,4,4,5,6,7,8,9,10,28]

print (statistics.mean(ran))
print (statistics.median(ran))
print (statistics.mode(ran))
print (round(statistics.stdev(ran), 1))
