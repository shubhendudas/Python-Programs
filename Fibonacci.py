# FIBONACCI SERIES
# 0,1,1,2,3,5,8,13,21,34....
# How to print this series in Python?

def Fib(number):
      if number < 0:
            return 0
      elif number == 1:
            return 0
      elif number == 2:
            return 1
      else:
            return Fib(number-1) + Fib(number-2)

maxLimit = int(input("How many terms?\n"))
print("MaxLimit = " + str(maxLimit))

i = 0
while (i <= maxLimit):
      if (i != 0):  # hide the first invalid 0
            print(Fib(i))
      i += 1

     
