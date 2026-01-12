def collatz(number):
    if  number%2==0:
        n=number//2
        return n
    elif number%2==1:
         n=3*number+1
         return n    

print("Enter an integer")
try:
   number=int(input())
   while True:
      if number!=1:
         print(collatz(number))
         number=collatz(number)
      else:
       break
   print(' Yaay, the number is 1 now')

except ValueError:
   print("Please enter a valid Integer")
