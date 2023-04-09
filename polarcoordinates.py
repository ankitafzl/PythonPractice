import cmath
x=complex(input().strip())
res=cmath.polar(x)
for i in range (0,2):
   print(res[i])


######################## FIND ANGLE MBC ######################

import math
AB=int(input())
BC=int(input())
print(round(math.degrees(math.atan(AB/BC))),chr(176),sep='')
