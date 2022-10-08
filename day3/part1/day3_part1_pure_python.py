"""Day 3, part 1.

The submarine has been making some odd creaking noises,
so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a
list of binary numbers which, when decoded properly, can
tell you many useful things about the conditions of the
submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic
report to generate two new binary numbers (called the
gamma rate and the epsilon rate). The power consumption
can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding
the most common bit in the corresponding position of all
numbers in the diagnostic report.
For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are
five 0 bits and seven 1 bits. Since the most common bit
is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic
report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are
1, 1, and 0, respectively, and so the final three bits of
the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use
the most common bit, the least common bit from each position is
used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying
the gamma rate (22) by the epsilon rate (9) produces the power
consumption, 198.

Use the binary numbers in your diagnostic report to calculate the
gamma rate and epsilon rate, then multiply them together. What is
the power consumption of the submarine?
(Be sure to represent your answer in decimal, not binary.)
"""
from typing import Union


def read_data():
    """Read the data."""
    with open("../../data/day3_input.txt", "r") as txt:
        instructions = txt.read().replace("\n", ",").split(",")
    return instructions[:-1]


def binary_to_decimal(binary_number: str) -> int:
    """Convert a binary number to a decimal number.

    There is a built-in function in pyton (int(binary, 2)),
    but we will implement the function just for fun.

    :param binary_number: The binary number (as a string).
    :return: The corresponding decimal number.
    """
    decimal_value = 0
    for index, number in enumerate(binary_number[::-1]):
        decimal_value += int(number) * 2 ** index
    return decimal_value


def index_vertically(input_data: list[str]) -> list[list[int]]:
    """Index the data vertically (see instructions).

    :param input_data: A list of strings. If represented
        as a matrix, it has the size N x M.
    :return: The vertically indexed data with size M x N (as integers).
    """
    lengths = [len(s) for s in input_data]
    if len(set(lengths)) > 1:
        raise ValueError(
            "The individual strings are of different length. "
            "They all have to be of equal length."
        )
    vertically_indexed_data = []
    for index in range(lengths[0]):
        vertically_indexed_data.append(
            [int(bit_string[index]) for bit_string in input_data]
        )
    return vertically_indexed_data


def find_most_common_bit(input_data: list[list[int]]) -> list[int]:
    """Find the most common bit for each vertical position in a list.

    Since there are only ones and zeros in the lists, one
    can calculate the mean. If the mean is > .5, there are
    more 1s than 0s; therefore, the most common bit is 1.
    When representing the boolean value of the comparison
    (mean > .5) as an integer, we therefore have the solution.

    :param input_data: The data as vertically indexed data.
    :return: The most common bit of each vertical position.
        The resulting list therefore same the same length as the
        individual strings.
    """
    most_common_bits = []
    for number_list in input_data:
        most_common_bits.append(int(sum(number_list) / len(number_list) > 0.5))

    return most_common_bits


def list_to_binary_string(integer_list: list[int]) -> str:
    """Convert a list of integers to a string representing a binary."""
    bin_str = ""
    for integer in integer_list:
        bin_str += str(integer)
    return bin_str


def invert_integers(integers: list[int]) -> list[int]:
    """Invert integers.

    This means that each 0 becomes a 1 and vice versa.
    This is done for all integers in the given list.

    :param integers: A list of integers (0s and 1s).
    :return: The inverted list of integers.
    """
    inverted_integers = [int(not number) for number in integers]
    return inverted_integers


if __name__ == "__main__":
    data = read_data()
    vertical_data = index_vertically(data)

    # Get the most common bit.
    gamma_rate = find_most_common_bit(vertical_data)
    epsilon_rate = invert_integers(gamma_rate)

    # Convert the lists back to a (binary) string and then to a decimal.
    gamma, epsilon = [
        binary_to_decimal(list_to_binary_string(rate))
        for rate in [gamma_rate, epsilon_rate]
    ]

    print(f"Solution: {gamma * epsilon}")
