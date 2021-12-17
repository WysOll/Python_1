def gen(n):
    print('first perebor')
    yield n
    print('vtoroy perebor')
    yield n+1
    print('tretiy perebor')
    yield n*3
n=int(input('n='))
t=gen(n)
#print(next(t))
#print(next(t))    
#print(next(t))
for i in t:
    print(i)
