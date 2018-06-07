import time
from random import *


# algorithm


def Bot(L, x_p, y_p, R):
    """
    Function responsible for the transition of Labyrinth

    i - rows
    j - columns

    Directions:
    0-down, 1-right, 2-up, 3-left

    :param L: object Labyrinth
    :param x_p: X Start
    :param y_p: Y Start
    :param R: road
    :return: Is true when passed
    """
    i = x_p
    j = y_p

    ni = x_p
    nj = y_p

    d = 0
    pisz(L, 6, 5)
    # secure
    counter = 0
    cross = 0

    side = 0

    while L[i][j] != 3:
        try:
            s = 0

            # dol - 0
            print(L[i + 1][j])
            if L[i + 1][j] == 1:
                # jezeli bylismy u dolu
                if d == 2:
                    d = -1
                else:
                    d = 0
                    s = s + 1
                    ni = i + 1
            else:
                if s == 0:
                    d = -1

            # prawo - 1
            if L[i][j + 1] == 1:
                if d == 3:
                    d = -1
                elif d == -1:
                    d = 1
                    nj = j + 1
                s = s + 1
            else:
                if s == 0:
                    d = -1

            # gora - 2
            if L[i - 1][j] == 1:
                if d == 0:
                    pass
                if d == -1:
                    d = 2
                    ni = i - 1
                s = s + 1
            else:
                if s == 0:
                    d = -1

            # lewo
            if L[i][j - 1] == 1:
                if d == 1:
                    pass
                elif d == -1:
                    d = 3
                    nj = j - 1
                s = s + 1

            print( i, j, d)
            z = int(input("A: "))

            if s == 0:
                i = R[cross][0][0]
                j = R[cross][0][1]
                d = R[cross][1]
            elif s == 1:
                i = ni
                j = nj
            else:
                R.append([[i, j], d])
                cross = cross + 1
                i = ni
                j = nj

            counter = counter + 1

            if counter > 1000000:
                print("HEHE ZA DUZO")
                return False
        except:
            print("COS NIE TAK")
            if cross != 0:
                return False
    return True



# *** Generator ***
# List comprehension, algorith

def generator(my, mx):
    """
    Function responsible for generating labyrinth
    Hunt and Kill algorithm

    :param my: columns
    :param mx: rows
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
            if 0 <= nx < mx and 0 <= ny < my:
                if maze[ny][nx] == 0:
                    # of occupied neighbors must be 1
                    ctr = 0
                    for j in range(4):
                        ex = nx + dx[j]
                        ey = ny + dy[j]
                        if 0 <= ex < mx and 0 <= ey < my:
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
