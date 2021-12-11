
import logging

# Part 1:
# Determine min fuel using constant fuel consumption per move
def determine_min_fuel_part1(filename):
    # open file for reading
    # also read().splitlines() gets rid of the \n character
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    
    # only the first line of the file is used and is a comma-seperated list.
    positions = [int(x) for x in lines[0].split(',')]

    # set the starting fuel to something high, so it can be compared against
    current_lowest_fuel = 9999999999
    current_lowest_pos = 1

    # iterate to the maximum horizontal position
    for i in range(max(positions)):
        current_fuel_test = 0
        break_loop = False
        for j, elem in enumerate(positions):
            current_fuel_test += abs(elem-i)
            # break out of loop early if we see this position is using more fuel than current best
            if current_fuel_test > current_lowest_fuel:
                break_loop = True
                break
        if break_loop:
            continue
        else:
            current_lowest_fuel = current_fuel_test
            current_lowest_pos = i
    return current_lowest_pos, current_lowest_fuel

# Part 2:
# Determine min fuel using increasing fuel consumption per move
def determine_min_fuel_part2(filename):
    # open file for reading
    # also read().splitlines() gets rid of the \n character
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    
    # only the first line of the file is used and is a comma-seperated list.
    positions = [int(x) for x in lines[0].split(',')]

    # set the starting fuel to something high, so it can be compared against
    current_lowest_fuel = 9999999999
    current_lowest_pos = 1

    # iterate to the maximum horizontal position
    for i in range(max(positions)):
        current_fuel_test = 0
        break_loop = False
        for j, elem in enumerate(positions):
            # increasing fuel consumption values can be modeled as (n^2+n)/2
            current_fuel_test += int((abs(elem-i)**2+abs(elem-i))/2)
            # break out of loop early if we see this position is using more fuel than current best
            if current_fuel_test > current_lowest_fuel:
                break_loop = True
                break
        if break_loop:
            continue
        else:
            current_lowest_fuel = current_fuel_test
            current_lowest_pos = i
    return current_lowest_pos, current_lowest_fuel

logging.basicConfig(level=logging.DEBUG)
o = determine_min_fuel_part1('input.txt')
print("Part 1: Position: ", o[0], " Fuel: ", o[1])
o2 = determine_min_fuel_part2('input.txt')
print("Part 2: Position: ", o2[0], " Fuel: ", o2[1])