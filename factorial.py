x=int(input("enter your value:"))

fact=1
if(x<0):

  print("Invalid value")

else:

  for i in range(1,x+1):

    fact=fact*i

  print("factorial of a given num is :",fact)
