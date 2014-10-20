from datetime import datetime
now = datetime.now()

user_age = raw_input("Please, enter your age in dd/mm/yyyy format!: ")

user_y = int(user_age[6:10])
user_m = int(user_age[3:5])
user_d = int(user_age[0:2])

curr_y = now.year
curr_m = now.month
curr_d = now.day

calc_y = int(curr_y) - user_y
calc_m = int(curr_m) - user_m
calc_d = int(curr_d) - user_d

act_age = "You are '%s' years old, '%s' months old, '%s' days old." % (calc_y, calc_m, calc_d)

print act_age
