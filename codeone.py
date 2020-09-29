import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np

thisdict = {}


def plothex():
    coord = [[0, 0, 0], [0, 1, -1], [-1, 1, 0], [-1, 0, 1], [0, -1, 1], [1, -1, 0], [1, 0, -1]]
    colors = [["Green"], ["Blue"], ["Green"], ["Green"], ["Red"], ["Green"], ["Green"]]
    labels = [['zerocenter'], ['one'], ['two'], ['three'], ['four'], ['five'], ['six']]

    # Horizontal cartesian coords
    hcoord = [c[0] for c in coord]

    # Vertical cartersian coords
    vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) / 3. for c in coord]

    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')

    # Add some coloured hexagons
    for x, y, c, l in zip(hcoord, vcoord, colors, labels):
        print("X:", x, "Y:", y)
        color = c[0].lower()

        # matplotlib understands lower case words for colours
        hex = RegularPolygon((x, y), numVertices=6, radius=2. / 3.,
                             orientation=np.radians(30),
                             facecolor=color, alpha=0.2, edgecolor='k')
        ax.add_patch(hex)
        # Also add a text label
        print("l", l[0])

        ax.text(x, y + 0.2, l[0], ha='center', va='center', size=20)

        hexinfo = (x,y)

        thisdict[l[0]] = hexinfo

    # Also add scatter points in hexagon centres
    ax.scatter(hcoord, vcoord, c=[c[0].lower() for c in colors], alpha=0.5)

    plt.savefig("mygraph.png")

    print(thisdict)


def getcoords(label):
    val = thisdict.get(label)
    print("val: ====", val)
    x = val[0]
    y = val[1]
  
if __name__ == '__main__':
    plothex()
    getcoords('one')
