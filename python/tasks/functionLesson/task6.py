with open('hello.txt','w',encoding='utf-8') as f:
    f.write('Hello\nPython\nFiles\n')
with open('hello.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line,end = '')
with open('hello.txt','a',encoding='utf-8') as f:
    f.write('Done\n')
with open('hello.txt','r',encoding='utf-8') as f:
    for num,line in enumerate(f):
        print(num + 1,line,end = '')
    print(f'Counted lines: {num + 1}')
with open('hello.txt','r',encoding='utf-8') as f:
    a = 1
    for line in f:
        print(a,line,end = '')
        a += 1
    print(f'Counted lines: {a - 1}')
#.............They are identic,I guess.......................
with open('hello.txt','r',encoding='utf-8') as f:
    print(f.readline(),end='')
with open('hello.txt','r',encoding='utf-8') as f:
    print(next(f),end='')
#............................................................
with open('hello.txt','r',encoding = 'utf-8') as f:
    lines = f.readlines()
with open('upper.txt','w+',encoding = 'utf-8') as f:
    f.writelines(line.upper() for line in lines)
    f.seek(0)
    for line in f:
        print(line,end='')
