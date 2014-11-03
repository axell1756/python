myWords = ["cat", "dog", "spider", "tiger", "puma", "panther", "rhino"]
enter = raw_input("Enter any animal comes to your mind: ")

for word in myWords:
    while enter != word:
        print "There is no such word in lib!"
        print raw_input("Enter any animal comes to your mind: ")
        
print "There is %s in lib!" % (enter)    


0
