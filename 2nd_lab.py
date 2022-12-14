# we will use matplotlib library for working with graphs
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
def print_graph(x, y):
    plt.subplots(figsize=(pixel_to_inch(960), pixel_to_inch(540)))
    plt.title('The picture for DS7 would be: ')
    plt.scatter(x, y, 0.2)
    plt.show()


if __name__ == "__main__":
    print("laboratory #2 for 'comp graphics & multimedia'. programming part.")
    print("made by Chumak Sofiia, KM-12.")
    x_point, y_point = get_coordinates("DS7.txt")
    print_graph(x_point, y_point)


