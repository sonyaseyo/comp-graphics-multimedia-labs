# we will use matplotlib library for working with graphs
import matplotlib.pyplot as plt


# in such way we will get coordinates from file and put them in lists for x-axis and y-axis
def get_coordinates(file_name):
    x, y = [], []
    with open(file_name, 'r') as f:
        for line in f:
            row = line.split()
            x.append(row[0])
            y.append(row[1])
    return x, y


# we will use it for creating canvas with the given size
# because plt.figure works with inches, not pixels.
def pixel_to_inch(value):
    return value/96


# this function will print graph due to all demands
def print_graph(x, y):
    plt.figure(figsize=(pixel_to_inch(960), pixel_to_inch(540)))
    plt.plot(y, x, 'o')
    plt.xlabel('y - axis')
    plt.ylabel('x - axis')
    plt.title('The graph for DS7 coordinates would be: ')
    plt.show()


if __name__ == "__main__":
    print("laboratory #2 for 'comp graphics & multimedia'. programming part.")
    print("made by Chumak Sofiia, KM-12.")
    x_point, y_point = get_coordinates("DS7.txt")
    print_graph(x_point, y_point)


