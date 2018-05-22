import time

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

    L[x_p][y_p] = 2
    L[x_k][y_k] = 3

    if b:
        L[x_m][y_m] = 4

    return L

