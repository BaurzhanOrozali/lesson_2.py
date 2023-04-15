def zadchka1():
    a = int(input('введите число: '))
    r = range( 1, a+1)
    count = 1
    for i in r:
        count=i*count
        print(count, end = ' ')

def zadachka2():
    print(f'x | y | ¬ (X ∧ Y) ∨ Z')
    for x in range(0, 2):
        for y in range(0, 2):    
            for z in range(0, 2): 
                print(f'{x} | {y} | {z} | {int(not (x and y) or z)}')

def zadachka3():
    text = str (input ('Input text: '))
    line = str (input ('Input offer: '))
    lenght_text = len(text)
    lenght_line = len(line)
    for r in range(lenght_text):
        count = 0
        for el in range(lenght_line):
            if line[el] == text[r]:
                count = count + 1
                print (line[el], end=' ' )
        print ( '=', count ,  end = ' ' )

def zadachka4():
    num = abs(
        int(
            input('введите свое число: ')
            )
    )
    i = -num
    u = []
    while i < num+1:
        print(i , end = "  ")
        u.append(i)
        i+=1
    u = u[-2:] + u[:-2]
    print('\n',u)