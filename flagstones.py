n,m,a=map(int,input().split())
N=n//a
M=m//a
x=N*M 
if n%a!=0 and m%a!=0:
    x=((N+1)*(M+1))
if n%a!=0:
    x=((N1+)*M)
elif m%a!=0:
    x=((M+1)*N)
print(x)
