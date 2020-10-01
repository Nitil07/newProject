def FibonacciRecursion(n):  
   if n <= 1:  
       return n  
   else:  
       return(FibonacciRecursion(n-1) + FibonacciRecursion(n-2))  

n = int(input("Enter the Number of terms? "))  
if n<= 0:   
   print("Please enter Postive integer")  
else:  
   print("Fibonacci sequence will be :",end= " ")  
   for i in range(n):  
       print(FibonacciRecursion(i),end=" ")

