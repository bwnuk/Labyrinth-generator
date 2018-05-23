import time
from random import *


# algorithm


def Bot(L, x, y, x_p, y_p):
    """
    Function responsible for the transition of Labyrinth

    0-left, 1-down, 2-right, 3-up

    :param L: object Labyrinth
    :param x: size of x of Labyrinth
    :param y: size of y of Labyrinth
    :param x_p: X Start
    :param y_p: Y Start
    :return: Is true when passed
    """
    i = x_p
    j = y_p

    # secure

    counter = 0

    side = 0

    while L.get_value(i, j) != 3:
        print(L.get_value(i, j), i, j, side)
        try:
            if side == 0:
                # dol
                if L.get_value(i + 1, j) == 1 or L.get_value(i + 1, j) == 3 or L.get_value(i + 1, j) == 4:
                    i = i + 1
                # lewo
                elif L.get_value(i, j - 1) == 1 or L.get_value(i, j - 1) == 3 or L.get_value(i, j - 1) == 4:
                    j = j - 1
                # prawo
                elif L.get_value(i, j + 1) == 1 or L.get_value(i, j + 1) == 3 or L.get_value(i, j + 1) == 4:
                    side = 1
                # gora
                elif L.get_value(i - 1, j) == 1 or L.get_value(i - 1, j) == 3 or L.get_value(i - 1, j) == 4:
                    i = i - 1
            elif side == 1:
                if L.get_value(i, j + 1) == 1 or L.get_value(i, j + 1) == 3 or L.get_value(i, j + 1) == 4:
                    j = j + 1
                elif L.get_value(i + 1, j) == 1 or L.get_value(i + 1, j) == 3 or L.get_value(i + 1, j) == 4:
                    side = 0
                elif L.get_value(i - 1, j) == 1 or L.get_value(i - 1, j) == 3 or L.get_value(i - 1, j) == 4:
                    side = 2
                elif L.get_value(i, j - 1) == 1 or L.get_value(i, j - 1) == 3 or L.get_value(i, j - 1) == 4:
                    j = j - 1
            elif side == 2:
                if L.get_value(i - 1, j) == 1 or L.get_value(i - 1, j) == 3 or L.get_value(i - 1, j) == 4:
                    i = i - 1
                elif L.get_value(i, j + 1) == 1 or L.get_value(i, j + 1) == 3 or L.get_value(i, j + 1) == 4:
                    j = j + 1
                    side = 1
                elif L.get_value(i, j - 1) == 1 == 1 or L.get_value(i, j - 1) == 3 or L.get_value(i, j - 1) == 4:
                    j = j - 1
        except:
            if side != 2:
                side = side + 1
            else:
                side = 0

        counter = counter + 1
        if counter >= 10000:
            return False
    return True


# *** Generator ***
# List comprehension, algorithm

def generator(x_p, y_p, x_k, y_k, r_y, r_x, b, x_m=0, y_m=0):
    """
    Function responsible for generating labyrinth
    Hunt and Kill algorithm

    :param x_p: x start
    :param y_p: y start
    :param x_k: x end
    :param y_k: y end
    :param r_y: columns
    :param r_x: rows
    :param b: boolean about middle point
    :param x_m: x mid
    :param y_m: y mid
    :return: Labyrinth as a list
    """
    L = [[0 for i in range(r_x)] for j in range(r_y)]

    remaining = r_y * r_x

    k = 0
    w = 0
    mid = True

    t_x = x_p
    t_y = y_p

    direction = 0

    L[x_p][y_p] = 2
    L[x_k][y_k] = 3

    if b:
        L[x_m][y_m] = 4
    else:
        l_x = randint(0, r_x - 1)
        l_y = randint(0, r_y - 1)

        while l_x == x_p or x_k == l_x or y_k == l_y or y_p == l_y:
            l_x = randint(0, r_x - 1)
            l_y = randint(0, r_y - 1)

        x_m = l_x
        y_m = l_y

    # Gdzie obecnie dazymy
    s_x = x_m
    s_y = y_m

    # pozostalo nie odwiedzonych
    remaining = remaining - 1

    while remaining > 0:

        # Sprawdzamy czy juz dotarlismy do szukanego pkt
        if t_x == s_x and t_y == s_y and mid:
            s_x = x_k
            s_y = y_k
            mid = False

        direction = random_direction()

        # idziemy w prawo, albo w lewo
        #if s_x - t_x < (r_x // 2):
         #   while direction == 3:
         #       direction = random_direction()
        #elif s_x - t_x < 0:
         #   while direction==2:
          #      direction = random_direction()

        # losujemy kierunek

        if direction == 0:
            if check_boundaries(t_y-1, r_y):
                remaining = remaining - 1
        elif direction == 1:
            if check_boundaries(t_x+1, r_y):
                remaining = remaining - 1
        elif direction == 2:
            if check_boundaries(t_x-1, r_y):
                remaining = remaining - 1
        elif direction == 3:
            if check_boundaries(t_y+1, r_y):
                remaining = remaining - 1

    return L


def reset_lab(x_p, y_p, x_k, y_k, r_y, r_x,):
    """
    If something goes wrong
    :return: Reseted Labyrinth
    """
    L = [[0 for i in range(r_x)] for j in range(r_y)]
    L[x_p][y_p] = 2
    L[x_k][y_k] = 3
    return L


def random_direction():
    """
    :return: 0 - N, 1 - E, 2 - W, 3 - S
    """
    return randint(0, 3)


def check_boundaries(x, r):
    """
    :return:
    """
    if x >= r or x < 0:
        return False
    return True

# Values 0-wall, 1-road, 2-entrance, 3-exit, 4-middle
