hexstore = {

    "A": {(1, "C"), (3, "Z")},
    "Z": {(0, "A"), (2, "Y"), (3, "X")},
    "X": {(0, "Z"), (1, "Y"), (2, "V")}
}

newhex = []

sidesmap = {3: 0, 4: 1, 5: 2, 0: 3, 1: 4, 2: 5}


def getprev(num):
    return num - 1


def getnext(num):
    return num + 1


def update_list(x, border, side):
    print("x is : ======>>", x)
    if x[0] == getnext(border):
        if side == 0:
            # newhex.__setitem__((5, x[1]))
            newhex.append((5, x[1]))
        else:
            # newhex.__setitem__(side - 1, x[1]))

            newhex.append(((side - 1), x[1]))

    if x[0] == getprev(border):
        if side == 5:
            newhex.append((0, x[1]))
        else:
            newhex.append(((side + 1), x[1]))


def set_neighbours(hexname, border, side):
    
    #fetch neighbors of this hexagon
    neighbors = hexstore.get(hexname)
    if neighbors is not None:

        for x in neighbors:
            update_list(x, border, side)
            # if x[0] == getnext(border):
            #     if side == 0:
            #         newhex.append((5, x[1]))
            #     else:
            #         newhex.append(((side - 1), x[1]))
            #
            # if x[0] == getprev(border):
            #     if side == 5:
            #         newhex.append((0, x[1]))
            #     else:
            #         newhex.append(((side + 1), x[1]))



def add_hex(name, hexname, border):
    side = sidesmap.get(border)

    set_neighbours(hexname, border, side)




                  # for n in neighbors:
                        # print("border",thisBorder)
                        # print("side",thisSide)

    hexstore[name] = newhex

    print(hexstore)


if __name__ == '__main__':
    print("main")

    ne = []

    add_hex("W", "A", 2)
    # if len(newhex) < 6:

    #get neighbors of existing neihbours
    for item in newhex:
            print("this")
            #fetch neighbors of this hex
            # hexname = item[1]
            # thisSide = item[0]
            # # neighbors = hexstore.get(item[1])
            # thisBorder = sidesmap.get(item[0])
            # neighbors = hexstore.get(hexname)
            # print(neighbors)
            # print(ne)
            ne.append(item[1])




    print(ne, hexstore.get("W")[0][0])



    # set_neighbours(hexname, thisBorder, thisSide)