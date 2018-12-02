from turtle import *

def get_num_hexagons():
    """ Finding side lenght of hexagons. """
    number = int(input())
    d = 500 / number
    return d

def draw_hexagon(side_len, color_input, x=0, y=0):
    """ Drawing hexagon. """
    side = (side_len / 2) * 3 ** .5
    penup()
    pendown()
    goto(x, y)
    color(color_input)
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


def main():
    """ Main function. """
    d = get_num_hexagons()
    right(90)
    penup()
    color_input = input()
    draw_hexagon(d, color_input)
    done()


if __name__ == "__main__":
    main()
