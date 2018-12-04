
def substitution(color1, color2, number, d):
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