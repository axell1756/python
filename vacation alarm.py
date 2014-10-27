sun = 0
mon = 1
tue = 2
wed = 3
thu = 4
fri = 5
sat = 6
ww = [mon, tue, wed, thu, fri]
we = [sat, sun]
vac = raw_input("Are you on vacation?: ").lower

if vac == "no" or vac == "n":
    ww = "7:00"
    we = "10:00"
    print "On workday you should wake up in %s" % (ww)
    print "On weekend you should wake up in %s" % (we)
else:
    ww = "10:00"
    we = "Calm down, have a rest. You are on vacation! Who, in a straight mind will wake up earlier than 12:00?"
    print "On workday you should wake up in %s" % (ww)
    print "On weekend you should wake up in %s" % (we)
