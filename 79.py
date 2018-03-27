n=int(input("Enter limit:"))
a=[]
for i in range(0,n):
  b=int(input('Ur value:'))
  a.append(b)
print(a)
print(max(a) - min(a))
