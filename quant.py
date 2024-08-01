import sys
import numpy as np
min_value = int(input("Enter a Integer which will be your minimum value: "))
max_value = int(input("Enter a Integer which will be your maximum value: "))
value = float(input(("Choose a value between " + str(min_value) + " and " + str(max_value) + ": " )))
if value > max_value:
   print("The value is greater than your range.")
   sys.exit()
elif value < min_value:
   print("The value is less than your range.")
   sys.exit()
levels = float(input(("Choose the number of Bits: ")))
sf = ((max_value - min_value))/(2**(levels)-1)
n =  (value)/sf
zero_point = np.round((min_value*-1)/sf)
qn =  np.round((value - min_value)/sf  + zero_point)
print("The Quantized Value is:")
if qn > (2**(levels)-1) :
   print(2**(levels)-1)
elif qn < (2**(levels)-1) :
   print(qn)
elif qn < 0:
   print(0)



