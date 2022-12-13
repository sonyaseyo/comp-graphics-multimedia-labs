import math
import matplotlib.pyplot as plt


# in such way we will get coordinates from file and put them in lists for x-axis and y-axis
def get_coordinates(file_name):
    x, y = [], []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            coord = line.strip().split()
            if len(coord) >= 2:
                x.append(int(coord[0]))
                y.append(int(coord[1]))
    f.close()
    return x, y


# we will use it for creating canvas with the given size
# because plt.figure works with inches, not pixels.
def pixel_to_inch(value):
    return value/96


# this function will print graph due to all demands
def do_graph(x, y):
    plt.subplots(figsize=(pixel_to_inch(960), pixel_to_inch(540)))
    plt.title('The picture for rotated DS7 would be: ')
    plt.scatter(x, y, 0.2)
    plt.show()


def do_transform(x, y, angle):
    new_x, new_y = [], []
    # there we will rotate points for 80 degree and move start point to (480, 480)
    for i in range(len(x)):
        new_x_point = (x[i] * math.cos(angle) - y[i] * math.sin(angle)) - 480
        new_y_point = (x[i] * math.sin(angle) + y[i] * math.cos(angle)) - 480
        new_y.append(new_y_point)
        new_x.append(new_x_point)
    return new_x, new_y


if __name__ == "__main__":
    print("laboratory #3 for 'comp graphics & multimedia'. programming part.")
    print("made by Chumak Sofiia, KM-12.")
    x_point, y_point = get_coordinates("DS7.txt")
    new_x_points, new_y_points = do_transform(x_point, y_point, 1.39626)
    do_graph(new_x_points, new_y_points)
