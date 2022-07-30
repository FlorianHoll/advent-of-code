"""Day 4, part 1. Implementation in numpy.

On the other hand, it might be wise to try a different strategy:
let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once,
so rather than waste time counting its arms, the safe thing to do is to
figure out which board will win last and choose that one. That way, no
matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens
after 13 is eventually called and its middle column is completely marked.
If you were to keep playing until this point, the second board would have
a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins,
what would its final score be?
"""
from day4.part1._read_data import read_day4_data
from day4.part1.bingo_game import LastOneWinsBingoGame

if __name__ == "__main__":
    boards, numbers_to_draw = read_day4_data()
    game = LastOneWinsBingoGame(boards, numbers_to_draw)
    winner, last_number = game.play()
    sum_non_called = winner.get_sum_of_all_non_called_numbers()
    print(f"The result is {sum_non_called * last_number}.")
