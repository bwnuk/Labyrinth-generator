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
        if counter >= 1000000:
            print("ZA DUZO")
            return False
    return True


# *** Generator ***
# List comprehension, algorithm
# Hunt and Kill

def generator(my, mx):
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

    maze = [[0 for x in range(mx)] for y in range(my)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]  # 4 directions to move in the maze
    # start the maze from a random cell
    stack = [(randint(0, mx - 1), randint(0, my - 1))]

    while len(stack) > 0:
        (cx, cy) = stack[-1]
        maze[cy][cx] = 1
        # find a new cell to add
        nlst = []  # list of available neighbors
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= 0 and nx < mx and 0 <= ny < my:
                if maze[ny][nx] == 0:
                    # of occupied neighbors must be 1
                    ctr = 0
                    for j in range(4):
                        ex = nx + dx[j]
                        ey = ny + dy[j]
                        if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                            if maze[ey][ex] == 1: ctr += 1
                    if ctr == 1:
                        nlst.append(i)
        # if 1 or more neighbors available then randomly select one and move
        if len(nlst) > 0:
            ir = nlst[randint(0, len(nlst) - 1)]
            cx += dx[ir]
            cy += dy[ir]
            stack.append((cx, cy))
        else:
            stack.pop()
    return maze


def pisz(L, r, k):
    for i in range(int(r)):
        for j in range(int(k)):
            print(L[i][j], end=" ")
        print(" ")
    print(" ")

# Values 0-wall, 1-road, 2-entrance, 3-exit, 4-middle
