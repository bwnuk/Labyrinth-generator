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

    while L[i][j] != 3:
        try:
            if side == 0:
                # dol
                if L[i + 1][j] == 1 or L[i + 1][j] == 3 or L[i + 1][j] == 4:
                    i = i + 1
                # lewo
                elif L[i][j - 1] == 1 or L[i][j - 1] == 3 or L[i][j - 1] == 4:
                    j = j - 1
                # prawo
                elif L[i][j + 1] == 1 or L[i][j + 1] == 3 or L[i][j + 1] == 4:
                    side = 1
                # gora
                elif L[i - 1][j] == 1 or L[i - 1][j] == 3 or L[i - 1][j] == 4:
                    i = i - 1
            elif side == 1:
                if L[i][j + 1] == 1 or L[i][j + 1] == 3 or L[i][j + 1] == 4:
                    j = j + 1
                elif L[i + 1][j] == 1 or L[i + 1][j] == 3 or L[i + 1][j] == 4:
                    side = 0
                elif L[i - 1][j] == 1 or L[i - 1][j] == 3 or L[i - 1][j] == 4:
                    side = 2
                elif L[i][j - 1] == 1 or L[i][j - 1] == 3 or L[i][j - 1] == 4:
                    j = j - 1
            elif side == 2:
                if L[i - 1][j] == 1 or L[i - 1][j] == 3 or L[i - 1][j] == 4:
                    i = i - 1
                elif L[i][j + 1] == 1 or L[i][j + 1] == 3 or L[i][j + 1] == 4:
                    j = j + 1
                    side = 1
                elif L[i][j - 1] == 1 or L[i][j - 1] == 3 or L[i][j - 1] == 4:
                    j = j - 1
        except:
            if side != 2:
                side = side + 1
            else:
                side = 0

        counter = counter + 1
        if counter >= 100000:
            print("ZA DUZO")
            return False
    return True


# *** Generator ***
# List comprehension, algorithm
# Hunt and Kill

def generator(x_p, y_p, x_k, y_k, r_y, r_x, L, dx=1189099):
    """
    Function responsible for generating labyrinth
    Hunt and Kill algorithm

    :param x_p: x start
    :param y_p: y start
    :param x_k: x end
    :param y_k: y end
    :param r_y: columns
    :param r_x: rows
    :param dx: itterators
    :return: Labyrinth as a list
    """

    List = []

    print(" ")
    remaining = r_y * r_x

    t_x = x_p
    t_y = y_p

    L[t_x][t_y] = 1

    List_counter = 0
    it = 0
    r = 0
    change = 0

    o_x, o_y = t_x, t_y
    d = r_x //3

    endo = False

    if d ==0:
        d = 1

    dp = d // 2

    if dp == 0:
        dp = 144
    while remaining > 0:
        # walk
        direction = random_direction()

        if direction == 0:
            if check_boundaries(t_y - 1, r_y):
                if L[t_x][t_y - 1] == 8:
                    change = change + 1
                    t_y = t_y - 1
                    remaining = remaining - 1
                    L[t_x][t_y] = 1
                    List.append([t_x, t_y])
                    List_counter = List_counter + 1
                else:
                    if change > 5:
                        if r < t_y:
                            huntR(L, r, t_y)
                            r = r + 1
                        change = 0
                        t_x = o_x
                        t_y = o_y
        elif direction == 1:
            if check_boundaries(t_x + 1, r_y):
                if L[t_x + 1][t_y] == 8:
                    change = change + 1
                    t_x = t_x + 1
                    remaining = remaining - 1
                    L[t_x][t_y] = 1
                    List.append([t_x, t_y])
                    List_counter = List_counter + 1
                else:
                    if change > 5:
                        if r < t_y:
                            huntR(L, r, t_y)
                            r = r + 1
                        change = 0
                        t_x = o_x
                        t_y = o_y
        elif direction == 2:
            if check_boundaries(t_x - 1, r_y):
                if L[t_x - 1][t_y] == 8:
                    change = change + 1
                    t_x = t_x - 1
                    remaining = remaining - 1
                    L[t_x][t_y] = 1
                    List.append([t_x, t_y])
                    List_counter = List_counter + 1
                else:
                    if change > 5:
                        if r < t_y:
                            r = r + 1
                            huntR(L, r, t_y)
                        change = 0
                        t_x = o_x
                        t_y = o_y
        elif direction == 3:
            if check_boundaries(t_y + 1, r_y):
                if L[t_x][t_y + 1] == 8:
                    change = change + 1
                    t_y = t_y + 1
                    remaining = remaining - 1
                    L[t_x][t_y] = 1
                    List.append([t_x, t_y])
                    List_counter = List_counter + 1
                else:
                    if change > 5:
                        if r < t_y:
                            r = r + 1
                            huntR(L, r, t_y)
                        change = 0
                        t_x = o_x
                        t_y = o_y

        if L[x_k][y_k] == 1:
            #print(t_x, t_y)
            print("KONIEC")
            print(it, "-")
            xx, yy = List[randint(1, List_counter-5)]
            L = koniec(L, xx, yy, remaining, r_x, r_y, change, o_x, o_y, r, x_k, y_k, r_x)
            print(" - ")
            pisz(L, r_x, r_y)
            #print(t_x, t_y)
            hunt(L, r_x, r_y)

            return L

        it = it + 1
        if change > 3:
            o_x = t_x
            o_y = t_y

        if it > dx:
            print("ITERR")
            print(it, "-")
            #print(t_x, t_y)
            hunt(L, r_x, r_y)
            #print(t_x, t_y)

            return L

        if remaining < 2:
            hunt(L, r_x, r_y)
            return L

    return L


def hunt(L, r_x, r_y):
    #print("HUNT")
    #pisz(L, r_x, r_y)
    #print(" - ")
    for i in range(0, r_y):
        for j in range(0, r_x):
            if L[j][i] == 8:
                L[j][i] = 0


def huntR(L, r, r_y, r_x=8):
    #print(" ---- ")
    #pisz(L, 8, 8)
    #print(" ---- ")
    try:
        #print("HR")
        for i in range(0, r_y):
            if L[r][i] == 8:
                L[r][i] = 0
    except:
        print(r)

def reset_lab(x_p, y_p, x_k, y_k, r_y, r_x, ):
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


def pisz(L, r, k):
    for i in range(int(r)):
        for j in range(int(k)):
            print(L[i][j], end=" ")
        print(" ")
    print(" ")


def koniec(L, t_x, t_y, remaining, r_x, r_y, change, o_x, o_y, r, x_k, y_k, dx):
    print(" ~~ ")
    pisz(L, r_x, r_y)
    it = 0
    while remaining > 0:
        # walk
        direction = random_direction()

        if direction == 0:
            if check_boundaries(t_y - 1, r_y):
                if L[t_x][t_y - 1] == 0 or L[t_x][t_y - 1] == 8:
                    change = change + 1
                    t_y = t_y - 1
                    remaining = remaining - 1
                    L[t_x][t_y] = 4
                else:
                    if change > 5:
                        if r < t_y:
                            huntR(L, r, t_y)
                            r = r + 1
                        change = 0
                        t_x = o_x
                        t_y = o_y
        elif direction == 1:
            if check_boundaries(t_x + 1, r_y):
                if L[t_x + 1][t_y] == 0 or L[t_x + 1][t_y] == 8:
                    change = change + 1
                    t_x = t_x + 1
                    remaining = remaining - 1
                    L[t_x][t_y] = 4
                else:
                    if change > 5:
                        if r < t_y:
                            huntR(L, r, t_y)
                            r = r + 1
                        change = 0
                        t_x = o_x
                        t_y = o_y
        elif direction == 2:
            if check_boundaries(t_x - 1, r_y):
                if L[t_x - 1][t_y] == 0 or L[t_x - 1][t_y] == 8:
                    change = change + 1
                    t_x = t_x - 1
                    remaining = remaining - 1
                    L[t_x][t_y] = 4
                else:
                    if change > 5:
                        if r < t_y:
                            r = r + 1
                            huntR(L, r, t_y)
                        change = 0
                        t_x = o_x
                        t_y = o_y
        elif direction == 3:
            if check_boundaries(t_y + 1, r_y):
                if L[t_x][t_y + 1] == 0 or L[t_x][t_y + 1] == 8:
                    change = change + 1
                    t_y = t_y + 1
                    remaining = remaining - 1
                    L[t_x][t_y] = 4
                else:
                    if change > 5:
                        if r < t_y:
                            r = r + 1
                            huntR(L, r, t_y)
                        change = 0
                        t_x = o_x
                        t_y = o_y

        it = it + 1
        if change > 3:
            o_x = t_x
            o_y = t_y

        if it > dx:
            print("ITERR")
            print(it, "- -")
            #print(t_x, t_y)
            hunt(L, r_x, r_y)
            #print(t_x, t_y)

            return L

# Values 0-wall, 1-road, 2-entrance, 3-exit, 4-middle
