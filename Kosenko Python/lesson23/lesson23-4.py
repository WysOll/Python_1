def gen(n):
    a,b=1,1
    for i in range(n):
        a,b=b,a+b
        yield a
        
n=int(input('n='))
t=gen(n)
for i in t:
    print(i)
