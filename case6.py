from turtle import *

def get_num_hexagons(number):
    """ Finding side lenght of hexagons. """
    d = 500 / number
    return d

def get_color_choice():
    #TODO

def draw_hexagon(d):
    """ Drawing hexagon. """
    side_len = (d / 2) * 3 ** .5
    penup()
    pendown()
    color('black')
    begin_fill()
    for i in range(6):
        forward(side_len)
        left(60)
    end_fill()
    left(120)
    for i in range(2):
        forward(side_len)
        right(60)
    penup()


def main():
    """ Main function. """
    number_of_hexagons = int(input())
    side_len = get_num_hexagons(number_of_hexagons)
    right(90)
    penup()
    for i in range(number_of_hexagons):
        draw_hexagon(side_len)
    done()

if __name__ == "__main__":
    main()
