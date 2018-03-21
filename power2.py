def is_power(a):
  a=a/2
  if(a==2):
    print("Yes")
  elif(a>2):
    return is_power(a)
  else:
    print("No")
    
a=int(input("Enter value:"))
is_power(a)
