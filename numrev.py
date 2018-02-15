u=int(input("enter your lucky num: "))

rev=0

while(u>0):

  b=u%10

  rev=rev*10+b

  u=u//10

print("Reverse of the num is:",rev)
