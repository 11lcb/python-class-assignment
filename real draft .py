def draw_function():
    height,length =  11,11
    x = length//2
    y =  height//2

    for screen_y in range(height):
        for screen_x in range(length):
            math_x = screen_x - x
            math_y = y - screen_y
            if math_y >0:
                if math_x  != 0 :
                    print(" ")
                else :
                    print("|")
            else :
                print(f'{"-"*length}')
                  
draw_function()                     




