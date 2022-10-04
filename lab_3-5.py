import math 
import time 

x = math.pow(2, 2) 
print (x)
# prints 2 ^ 2 and gives the answer 4.0 

y = 2 ** 2 
print (y)
# prints 2 ^ 2 and gives the answer 4 

a = time.process_time()
print (a) 
# time for a = 0.046537
# time changes before and after the statement is printed, this time giving me 0.030476

b = time.perf_counter()
print (b)
# after running this statement it gave me a larger number = 2123963.717506054