from turtle import *


def get_num_hexagons():
    """ Finding side length of hexagons. """
    try:
        n = int(input("Пожалуйста, введите количество шестиугольников, располагаемых в ряд: "))
        if 3 < n < 21:
            return n
        else:
            print("Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ")
            return get_num_hexagons()
    except ValueError:
        print("Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ")
        return get_num_hexagons()


def get_color_choice():
    """ Fill color choice. """
    list_of_colors = ['красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'пурпурный', 'розовый']
    try:
        color = str(input("Пожалуйста, введите цвет: ")).lower()
        if color in list_of_colors:
            if color == 'красный':
                color = 'red'
            if color == 'синий':
                color = 'blue'
            if color == 'зеленый':
                color = 'green'
            if color == 'желтый':
                color = 'yellow'
            if color == 'оранжевый':
                color = 'orange'
            if color == 'пурпурный':
                color = 'purple'
            if color == 'розовый':
                color = 'pink'
            return color
        else:
            print("'", color, "'", "не является верным значением. Пожалуйста, повторите попытку: ")
            return get_color_choice()
    except ValueError:
        print("'", color, "'", "не является верным значением. Пожалуйста, повторите попытку: ")
        return get_color_choice()


def main():
    list_of_colors = ['красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'пурпурный', 'розовый']
    print("Допустимые цвета заливки: ")
    for i in list_of_colors:
        print('', i)
    color1 = get_color_choice()
    color2 = get_color_choice()
    n = get_num_hexagons()


if __name__ == '__main__':
    main()
