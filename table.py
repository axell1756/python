you = int(input("How stylish are you today?: "))
date = int(input("How stylish are your date today?: "))

if you >= 8 and date >= 8:
        x = 2
elif you >= 3 and date >= 3:
        x = 1
elif you <= 2 and date <= 2:
        x = 0
        
if x == 2:
        print "You both are way to sexy to not to get a table!"
elif x == 1:
        print "Well, it could be worse, maybe you both will be able to get table in Mc'Donalds!"
elif x == 0:
        print "Guys... Go hide yourself from society for today!"

