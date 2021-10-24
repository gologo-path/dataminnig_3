import math
import copy


class Clusterization:
    clusters = []

    limit_x = tuple()
    limit_y = tuple()

    def read_from_file(self, path, number):
        with open(path, "r") as file:
            tmp_x = []
            tmp_y = []
            iters = 0
            for line in file:
                if iters >= number:
                    break

                raw = line.strip().split(" ")
                tmp_x.append(float(raw[0]))
                tmp_y.append(float(raw[-1]))

                iters += 1

            self.limit_x = (min(tmp_x), max(tmp_x))
            self.limit_y = (min(tmp_y), max(tmp_y))

            return [{"x": tmp_x[i], "y": tmp_y[i]} for i in range(len(tmp_x))]

    def evclid(self, point1, point2):
        result = 0
        result += (point1["x"] - point2["x"]) ** 2
        result += (point1["y"] - point2["y"]) ** 2

        return math.sqrt(result)

    def mean(self, ls: list):
        return round(sum(ls) / max(len(ls), 1), 2)

    def dict_lists_to_dict(self, d: list):
        x = []
        y = []
        for point in d:
            x.append(point["x"])
            y.append(point["y"])
        return x, y

    def add_point(self, point, centers):
        tmp = []
        for center in centers:
            tmp.append(self.evclid(center, point))
        return tmp

    def run_circle(self, cluster_centers, points):
        result = [[] for _ in range(len(cluster_centers))]
        centers = copy.deepcopy(cluster_centers)
        for point in points:
            tmp = self.add_point(point, centers)
            cluster_index = tmp.index(min(tmp))
            result[cluster_index].append(point)

            x, y = self.dict_lists_to_dict(result[cluster_index])
            centers[cluster_index] = ({"x": self.mean(x), "y": self.mean(y)})

        return result, centers
