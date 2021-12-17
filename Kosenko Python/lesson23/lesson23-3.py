def gen(language):
    for i in language:
       yield i  
language=['python','c++','java','c','c#']
t=gen(language)
for i in t:
    print(i)
