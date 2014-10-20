from datetime import datetime
now = datetime.now()

y = input("Please, enter your year of birth: ")
m = input("Please, enter your month of birth: ")
d = input("Please, enter your day of birth: ")

curr_y = now.year
curr_m = now.month
curr_d = now.day

act_y =  int(curr_y)- int(y)
act_m =  int(curr_m)- int(m)
act_d =  int(curr_d)- int(d)

age = "You are '%s' years old, %s months old, %s days old." % (act_y, act_m, act_d)

print age
