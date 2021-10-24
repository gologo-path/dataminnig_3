import math
from Clusterization import Clusterization
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import copy


def mean_sum(points_, center_):
    result = 0

    for k in range(len(center_)):
        for i in range(len(points_[k])):
            result += (points_[k][i]["x"] - center_[k]["x"]) ** 2
            result += (points_[k][i]["y"] - center_[k]["y"]) ** 2

    return result


if __name__ == '__main__':
    Vx = []
    Vy = []

    clusters_count = int(input("clusters_count = "))

    c = Clusterization()
    points = c.read_from_file("birch1.txt", 10000000)
    centers_orig = []

    for i in range(clusters_count):
        centers_orig.append(
            {"x": random.randint(c.limit_x[0], c.limit_x[1]), "y": random.randint(c.limit_y[0], c.limit_y[1])})

    for i in range(clusters_count):
        prev_cent = []
        centers = copy.deepcopy(centers_orig)
        while True:
            prev_cent = centers

            res, centers = c.run_circle(centers[:(i+1)], points)
            if str(centers) == str(prev_cent):
                break

        Vy.append(mean_sum(res, centers))
        Vx.append(i)

    colors = list(mcolors.CSS4_COLORS.values())[10:]

    print(Vx)
    print(Vy)

    _, axs = plt.subplots(1, 2)
    axs[0].plot(Vx, Vy, "b")

    for i in range(clusters_count):
        x, y = c.dict_lists_to_dict(res[i])
        axs[1].scatter(x, y, c=colors[i])

    for point in centers_orig:
        axs[1].scatter(point["x"], point["y"], c="r")

    plt.show()
