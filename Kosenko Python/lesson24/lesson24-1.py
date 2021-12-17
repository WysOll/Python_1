def f_1():
    print('Started loading')
def f_2():
    n=0
    while n<100:
        print('loading')
        n+=5
        r=f"{n}%"
        yield r
y=f_2()
for i in y:
    print(i)
def f_3():
    print('loading ended')
