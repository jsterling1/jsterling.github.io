from random import randint
wins = 0

for i in range(10000):
  regions=0
  if randint(1,100) <= 87:
    regions = regions + 1
   if randint(1,100) <= 65:
    regions = regions + 1
   if randint(1,100) <= 17:
    regions = regions + 1
  if regions >= 2:
    print "You win the election!"
  else:
    print "You did not win the election..."
