# count the number of times a depth measurement increases from the previous measurement
def count_depth_measurements(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    count = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # must cast these to an int, or it won't work....
        if int(lines[i])>int(lines[i-1]):
            count += 1
    file.close()
    return count


# count the number of times the sum of measurements in this 3 period sliding window increases
def count_depth_measurements_three_window(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    count = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # stop when there's not enough left to create a new 3-window
        if i+3 == len(lines): break
        # must cast these to an int, or it won't work....
        if int(lines[i+1])+int(lines[i+2])+int(lines[i+3]) > int(lines[i])+int(lines[i+1])+int(lines[i+2]):
            count += 1
    file.close()
    return count

print("Day 01-1 Output: ", count_depth_measurements('input.txt'))
print("Day 01-2 Output: ", count_depth_measurements_three_window('input.txt'))