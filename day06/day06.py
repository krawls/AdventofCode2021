# Each lanternfish has an internal timer
# New lanternfish starts with an internal timer of 8 from existing lanternfish with timer of 0
# A lanternfish that creates a new fish resets its timer to 6

import logging

def count_lanternfish(filename, days):
    # given a file input, returns the number of lanternfish after a given number of days
    # input is a list of existing lanternfish and their internal timers

    # open file for reading
    # also read().splitlines() gets rid of the \n character
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    
    # only the first line of the file is used and is a comma-seperated list.
    input = lines[0].split(',')
    
    # instead of modeling each fish individually as an object, we'll just keep track of the number of fish at
    # each stage of their lifecycle and update a 9-element list each day
    fish_counts = []
    for i in range(9):
        fish_counts.append(0)
    
    # get initial state from input
    for i, elem in enumerate(input):
        fish_counts[int(elem)] += 1

    for i in range(days):
        # create a (non-reference) list copy that will be the previous days' values
        tmp_fishcounts = fish_counts.copy()
        # shift everyone's timer by 1 space left
        fish_counts[0] = tmp_fishcounts[1]
        fish_counts[1] = tmp_fishcounts[2]
        fish_counts[2] = tmp_fishcounts[3]
        fish_counts[3] = tmp_fishcounts[4]
        fish_counts[4] = tmp_fishcounts[5]
        fish_counts[5] = tmp_fishcounts[6]
        fish_counts[6] = tmp_fishcounts[7]
        fish_counts[7] = tmp_fishcounts[8]
        # spawn new fish at 8
        fish_counts[8] = tmp_fishcounts[0]
        # fish at 0 get added to 6
        fish_counts[6] += tmp_fishcounts[0]

    count = 0
    for i, elem in enumerate(fish_counts):
        count += int(elem)
    return count
        
logging.basicConfig(level=logging.DEBUG)
o = count_lanternfish('input.txt', 80)
print("Part 1: Count: ", o)
o2 = count_lanternfish('input.txt', 256)
print("Part 2: Count: ", o2)