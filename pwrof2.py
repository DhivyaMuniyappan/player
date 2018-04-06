def is_power(vol):
  vol=vol/2
  if(vol==2):
    print("Yes")
  elif(vol>2):
    return is_power(vol)
  else:
    print("No")
    
vol=int(input("Enter vvollue:"))
is_power(vol)
