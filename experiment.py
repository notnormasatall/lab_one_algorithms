from random import *
from sorting import *
import time
from pprint import pprint
from copy import deepcopy
from json import *

results = {
    # Results will be saved in json file
    "random_time":
        {
            "selection_sort": [],
            "insertion_sort": [],
            "merge_sort": [],
            "shell_sort": [],
        },

    "random_comparisons":
        {
            "selection_sort": [],
            "insertion_sort": [],
            "merge_sort": [],
            "shell_sort": [],
        },

    "sorted_time":
        {
            "selection_sort": [],
            "insertion_sort": [],
            "merge_sort": [],
            "shell_sort": [],
        },

    "sorted_comparisons":
        {
            "selection_sort": [],
            "insertion_sort": [],
            "merge_sort": [],
            "shell_sort": [],
        },

    "reversed_time":
        {
            "selection_sort": [],
            "insertion_sort": [],
            "merge_sort": [],
            "shell_sort": [],
        },

    "reversed_comparisons":
        {
            "selection_sort": [],
            "insertion_sort": [],
            "merge_sort": [],
            "shell_sort": [],
        },

    "repeated_time":
        {
            "selection_sort": [],
            "insertion_sort": [],
            "merge_sort": [],
            "shell_sort": [],
        },

    "repeated_comparisons":
        {
            "selection_sort": [],
            "insertion_sort": [],
            "merge_sort": [],
            "shell_sort": [],
        }
}

sorting_methods = {
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "shell": shell_sort
}


class Generator:
    # Following class will help to call the
    # methods for generating 4 array types

    def rand(n):
        return [randint(0, n) for _ in range(n)]

    def sorted_rand(n):
        return sorted(Generator.rand(n))

    def reversed_rand(n):
        return list(reversed(Generator.sorted_rand(n)))

    def repeated_rand(n):
        options = [1, 2, 3]
        return [choice(options) for _ in range(n)]


def experiment_one():
    # Experiment for a randomly generated array
    for n in range(7, 16):

        array = Generator.rand(2**n)
        test_sorting("selection", array, 5, "random")
        test_sorting("insertion", array, 5, "random")
        test_sorting("merge", array, 5, "random")
        test_sorting("shell", array, 5, "random")

    print("--- end of experiment one ---")


def experiment_two():
    # Experiment for a sorted array
    for n in range(7, 16):

        array = Generator.sorted_rand(2**n)

        test_sorting("selection", array, 1, "sorted")
        test_sorting("insertion", array, 1, "sorted")
        test_sorting("merge", array, 1, "sorted")
        test_sorting("shell", array, 1, "sorted")

    print("--- end of experiment two ---")


def experiment_three():
    # Experiment for a reversed array
    for n in range(7, 16):

        array = Generator.reversed_rand(2**n)

        test_sorting("selection", array, 1, "reversed")
        test_sorting("insertion", array, 1, "reversed")
        test_sorting("merge", array, 1, "reversed")
        test_sorting("shell", array, 1, "reversed")

    print("--- end of experiment three ---")


def experiment_four():
    # Experiment for {1,2,3} set array
    for n in range(7, 16):

        array = Generator.repeated_rand(2**n)

        test_sorting("selection", array, 3, "repeated")
        test_sorting("insertion", array, 3, "repeated")
        test_sorting("merge", array, 3, "repeated")
        test_sorting("shell", array, 3, "repeated")

    print("--- end of experiment four ---")


def test_sorting(func: str, array: list, rep_time: int, array_type=""):
    """
    Function receives array type (out 4 experiments),
    function that needs to be tested and number of
    repetitions (for experiment one and four)
    """
    work_time = 0
    comp_num = 0

    for _ in range(rep_time):

        test_array = deepcopy(array)
        start = time.time()
        result = sorting_methods[func](test_array)[1]
        comp_num += result
        work_time += (time.time()-start)

    # saves results into a dictionary
    results[array_type+"_time"][func + "_sort"].append(work_time / rep_time)
    results[array_type+"_comparisons"][func +
                                       "_sort"].append(comp_num / rep_time)


def test_experiments():
    """
    Calls each experiment one by one.
    """
    experiment_one()
    experiment_two()
    experiment_three()
    experiment_four()


if __name__ == '__main__':
    test_experiments()
    with open("results.json", "w") as f:
        f.write(dumps(results, indent=4))
    pprint(results)
