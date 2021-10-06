from json import *
import matplotlib.pyplot as plt

file = open("results.json")
data = loads(file.read())

# The dictionary helps to make the legend while generating graphs
graph_order = {"random_time": ["Time for random array", "Randomly generated Array | Time"],
               "random_comparisons": ["Comparisons for random array", "Randomly generated Array | Swaps"],
               "sorted_time": ["Time for sorted array", "Sorted Array | Time"],
               "sorted_comparisons": ["Comparisons for sorted array", "Sorted Array | Swaps"],
               "reversed_time": ["Time for reversed array", "Reversed Array | Time"],
               "reversed_comparisons": ["Comparisons for reversed array", "Reversed Array | Swaps"],
               "repeated_time": ["Time for repeated array", "{1, 2, 3} set Array | Time"],
               "repeated_comparisons": ["Comparisons for repeated array", "{1, 2, 3} set Array | Time"]}


def create_graph():
    """
    Generates graphs out of given data.
    """
    array_types = list(graph_order.keys())
    experiment = 1

    for array_type in array_types:

        fig, ax = plt.subplots()
        ax.set_yscale('log')

        for sorting_type in list(data[array_type].keys()):

            # Collected data
            x = data[array_type][sorting_type]
            # Sizes of arrays
            y = ["2^7", "2^8", "2^9", "2^10",
                 "2^11", "2^12", "2^13", "2^14", "2^15"]

            plt.plot(y, x, label=sorting_type.replace("_sort", ""))

        ax.set(xlabel='Length of array',
               ylabel=graph_order[array_type][0], title=graph_order[array_type][1])
        ax.grid()
        ax.legend()
        plt.show()
        experiment += 1


if __name__ == '__main__':
    create_graph()
