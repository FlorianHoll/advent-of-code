"""Test the solution."""
# pylint: skip-file
import numpy as np
import pytest

from day3.day3_part1_numpy import binary_to_decimal
from day3.day3_part1_numpy import find_most_common_bit
from day3.day3_part1_numpy import index_vertically
from day3.day3_part1_numpy import invert_integers
from day3.day3_part1_numpy import list_to_binary_string

DATA_FROM_EXAMPLE = np.array(
    [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
)


# First, test the binary to decimal converter. We will use
# the built-in int(binary, 2) method to validate the results.
@pytest.mark.parametrize(
    "binary",
    [
        "00001",
        "00010",
        "00100",
        "00111",
        "10111",
        "10111",
        "1001010111",
        "100010101010101",
    ],
)
def test_binary_to_decimal_converter(binary):
    """Test if the binary numbers are converted correctly."""
    assert binary_to_decimal(binary) == int(binary, 2)


def test_vertical_indexing():
    """Test if a list of binary strings is correctly vertically indexed."""
    result = index_vertically(DATA_FROM_EXAMPLE)
    assert result.shape == (len(DATA_FROM_EXAMPLE), len(DATA_FROM_EXAMPLE[0]))
    assert np.all(result[:, 0] == np.array([0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0]))


def test_most_common_bit():
    """Test if the calculated most common bit is correct."""
    vertically_indexed_data = index_vertically(DATA_FROM_EXAMPLE)
    result = find_most_common_bit(vertically_indexed_data)
    assert np.all(result == np.array([1, 0, 1, 1, 0]))


@pytest.mark.parametrize(
    "num_list, binary",
    [
        ([1, 0, 1, 0], "1010"),
        ([1, 0, 0, 0], "1000"),
        ([1, 0, 1, 1, 1, 1, 1, 1, 0], "101111110"),
    ],
)
def test_conversion_to_binary_string(num_list, binary):
    """Test if the conversion to a binary strings works."""
    assert list_to_binary_string(num_list) == binary


@pytest.mark.parametrize(
    "original_list, inverted_list",
    [
        (np.array([1, 0, 1, 0]), np.array([0, 1, 0, 1])),
        (np.array([1, 0, 0, 0]), np.array([0, 1, 1, 1])),
        (np.array([1, 0, 1, 1, 1, 1, 1, 1, 0]), np.array([0, 1, 0, 0, 0, 0, 0, 0, 1])),
    ],
)
def test_inversion_of_list(original_list, inverted_list):
    """Test if the inversion of lists works."""
    result = invert_integers(original_list)
    assert np.all(result == inverted_list)
