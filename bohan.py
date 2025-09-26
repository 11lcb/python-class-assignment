RED = '\u001[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END ='\u001d[0m'

line=' '* 4
length = 10
height = length

for i in range(height):
    if i < height // 2:
        print(f'{BLUE}{line*(i+1)}{WHITE}{line*(lenght-1)}{END}')
    else:
        print(f'{BLUE}{line*(length - i)}{RED}{line*(i+1)}{END}')
def loading():
    for i in range(100):
        time.sleep(0.1)
        print(f'\u001b[100D{i+1}%',end='',flush=True)
    print('Done!')
def loading_multiple(num_tasks):
    bar_width = 25
    for k in range():
        for p in range(bar_width):
            bar = "#" * P  +"-"*(bar_width -p)
            print(f'{BEGIN}{ERASE}Task {k}/{num_tasks}[{bar}]{p*4}%'
                end='',flush=True)
loading_multiple(3)

