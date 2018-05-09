import time


# *** Bot ***
# Function responsible for the transition of Labyrinth
# @param1 object Labyrinth, @param2 size of x of Labyrinth, @param3 size of y of Labyrinth

def Bot(L, x, y, x_p, y_p):
    i = x_p
    j = y_p

    # secure

    counter = 0

    # 0-left, 1-down, 2-right, 3-up

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
# Function responsible for generating labyrinth
# @param1 x start, @param2 y start, @param3 x end, @param4 y end, @param5 rows, @param6 columns, @param7 boolean about middle point
# @return labyrinth as a list

def generator(x_p, y_p, x_k, y_k, r_x, r_y, b):
    L = [[0 for i in range(r_y)] for j in range(r_x)]

    L[x_p][y_p] = 2
    L[x_k][y_k] = 3

    if b:
        pass

    return L
