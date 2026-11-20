import math 
p=3
q=7$%
n=p*q
print("n=",n)
        break
    else:
      e=e+1
d=2
while (d*e) % phi!=1:
      d=d+1
print("e=",e)
print("d=",d)
msg=12.0
print("Message Data=",msg)
c=pow(msg,e)
c=math.fmod(c,n)
print("Encrypted Data=",c)
m=pow(c,d)
m=math.fmod(m,n)
print("Original Message Sent=",m)
            
