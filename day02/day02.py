# Part 1
# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

def determine_position(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    horizontal_position = 0
    depth = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # each line will have the form <command> <number>
        # split these and evaluate using match/case
        l = line.split(' ')
        match str(l[0]):
            case "forward":
                horizontal_position += int(l[1])
            case "down":
                depth += int(l[1])
            case "up":
                depth -= int(l[1])
    file.close()
    return horizontal_position, depth, horizontal_position*depth


# Part 2
# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
    # It increases your horizontal position by X units.
    # It increases your depth by your aim multiplied by X.

def determine_position2(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    horizontal_position = 0
    depth = 0
    aim = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # each line will have the form <command> <number>
        # split these and evaluate using match/case
        l = line.split(' ')
        match str(l[0]):
            case "forward":
                horizontal_position += int(l[1])
                depth += aim*int(l[1])
            case "down":
                aim += int(l[1])
            case "up":
                aim -= int(l[1])
    file.close()
    return horizontal_position, depth, horizontal_position*depth

output = determine_position('input.txt')
output2 = determine_position2('input.txt')
print("Part 1: Horizontal Position : ", output[0], " Depth: ", output[1], " Multipied: ", output[2])
print("Part 2: Horizontal Position : ", output2[0], " Depth: ", output2[1], " Multipied: ", output2[2])