n=int(input())
for x in range(2,n + 1):
       for i in range(2,x):
           if (x % i) == 0:
               break
       else:
           if(n%x==0):
             print(x)
        
