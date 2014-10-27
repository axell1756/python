speed = int(input("How fast you were driving?: "))
birthday = raw_input("Do you have a birthday today?: ")

if speed >= 81:
        x = 2
elif speed >= 61 or speed == 80:
        x = 1
elif speed <= 60:
        x = 0
if speed >= 86 and birthday == "yes":
        x = 2
elif speed >= 66 and birthday == "yes":
        x = 1
elif speed <= 65:
        x = 0
        
if x == 2:
        print "Oy, Sonic the Hedgehoge, here is your prize! Big ticket!"
elif x == 1:
        print "Well, thanks for not flying by a car! Small ticket!"
elif x == 0:
        print "Fear enought, no ticket!"
