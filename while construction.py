num=int(input("enter the limit:"))
x,y=0,1
print(x,y,end='  ')
i=0
#while loop runs for num-2 times as
#the first two digit are defined already
while(i<num-2):
       z=x+y
       print(z,end=' ')
       x=y
       y=z
       i=i+1
    
