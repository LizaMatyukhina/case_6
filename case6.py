"""Case-study #5 Tessellation
Developers:
Romanenko Alina(45%), Rashidova Aigerim(35%), Matyukhina Liza(40%)"""

from turtle import *
from ru_local import *


def get_num_hexagons():
    """ Finding side length of hexagons. """
    try:
        n = int(input(NUMBER, ))
        if 3 < n < 21:
            d = 500 / n
            return n, d
        else:
            raise ValueError
    except ValueError:
        while True:
            try:
                n = int(input(CORRECT_NUMBER, ))
                if 3 < n < 21:
                    d = 500 / n
                    return n, d
                else:
                    raise ValueError
            except ValueError:
                continue


def get_color_choice(color):
    """ Fill color choice. """
    list_of_colors = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, PINK]
    try:
        if color in list_of_colors:
            if color == RED:
                color = 'red'
            if color == BLUE:
                color = 'blue'
            if color == GREEN:
                color = 'green'
            if color == YELLOW:
                color = 'yellow'
            if color == ORANGE:
                color = 'orange'
            if color == PURPLE:
                color = 'purple'
            if color == PINK:
                color = 'pink'
            return color
        else:
            color = input("'" + color + "'" + CORRECT_VALUE).lower()
            return get_color_choice(color)
    except ValueError:
        color = input("'" + color + "'" + CORRECT_VALUE).lower()
        return get_color_choice(color)


def draw_hexagon(side_len, color_input, x, y):
    """ Drawing hexagon. """
    side = (side_len / 2) * 3 ** .5
    penup()
    goto(x, y)
    pendown()
    color('black', color_input)
    begin_fill()
    for i in range(6):
        forward(side)
        left(60)
    end_fill()
    left(120)
    for i in range(2):
        forward(side)
        right(60)
    penup()


def substitution(color1, color2, number, d):
    """Filling screen with hexagons"""
    y = 300 + 1.5 * d
    for j in range(number):
        y -= 1.3 * d
        if j % 2:
            x = -350 - 2.25 * d
        else:
            color1, color2 = color2, color1
            x = -350 - 1.5 * d
        for i in range(number):
            x += 1.5 * d
            if i % 2:
                draw_hexagon(d, color2, x, y)
            else:
                draw_hexagon(d, color1, x, y)


def main():
    """ Main function. """
    screensize(500, 500)
    speed(0)
    right(90)
    penup()
    number, d = get_num_hexagons()
    list_of_colors = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, PINK]
    print(AVALUABLE)
    for i in list_of_colors:
        print('', i)
    one = str(input(PLEASE, )).lower()
    color1 = get_color_choice(one)
    two = str(input(PLEASE, )).lower()
    color2 = get_color_choice(two)
    substitution(color1, color2, number, d)
    done()


if __name__ == "__main__":
    main()
