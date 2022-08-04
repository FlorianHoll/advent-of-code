"""Day 5, part 2. Implementation in numpy.

Unfortunately, considering only horizontal and vertical lines
doesn't give you the full picture; you need to also consider
diagonal lines.

Because of the limits of the hydrothermal vent mapping system,
the lines in your list will only ever be horizontal, vertical,
or a diagonal line at exactly 45 degrees. In other words:

    An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

Considering all lines from the above example would now produce
the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two
lines overlap. In the above example, this is still anywhere in the
diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines.
At how many points do at least two lines overlap?
"""
from day5.part1.read_data import read_day5_data
from day5.part1.vent_map import VentMap

if __name__ == "__main__":
    vent_locations = read_day5_data("day5_input.txt")
    vent_map = VentMap(vent_locations)
    for positions in vent_locations:
        vent_map.update_vent_locations(positions, allow_diagonals=True)
    result = vent_map.count_nr_of_overlaps()
    print(f"Number of overlapping hydrothermal vents: {result}")
