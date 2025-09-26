a='\u001b[47m'
b='\u001b[41m'
END='\u001b[0m'


line=' '*3
length=4
height=length


for i in range(height):
    if i<height//2:
        if i==1:
            print(f'{a}{line*(length)}')
        else:
            print(f'{a}{line*((length-i)//2)}{b}{line*i}{a}{line*(length-i)}{END}')
    else :           
        if i==8:
            print(f'{a}{line*(length)}')
        else:
            print(f'{a}{line*((length-i)//2)}{b}{line*i}{a}{line*(length-i)}{END}')


