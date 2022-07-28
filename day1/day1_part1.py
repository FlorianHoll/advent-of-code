"""Day 1 of Advent of Code without help of packages.

To do this, count the number of times a depth measurement increases from the
previous measurement. (There is no measurement before the first measurement.)
In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)

In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?
"""


def read_data():
    """Read the data."""
    with open("../data/day1_input.txt", "r") as txt:
        data = txt.read().replace("\n", ",").split(",")
    data = [int(s) for s in data[:-1]]
    return data


def find_nr_ascending(data: list[int]) -> int:
    """Find the number of bigger numbers than the previous."""
    counter = 0
    for index, number in enumerate(data):
        if index > 0:
            previous_number = data[index - 1]
            if number > previous_number:
                counter += 1
    return counter


if __name__ == "__main__":
    numbers = read_data()
    nr_ascending = find_nr_ascending(numbers)
    print(f"Number of measurements larger than previous measurement: {nr_ascending}")
