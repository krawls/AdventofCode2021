#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg
#
# 0 - 6 segments
# 1 - 2 segments*
# 2 - 5 segments
# 3 - 5 segments
# 4 - 4 segments*
# 5 - 5 segments
# 6 - 6 segments
# 7 - 3 segments*
# 8 - 7 segments*
# 9 - 6 segments
# * = unique

import logging

def decode_segments(filename, part):
    # open file for reading
    # also read().splitlines() gets rid of the \n character
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    
    # each line in the input is split into unique signal patterns
    # delimited by a | character
    unique_patterns = []
    output_values = [] 
    for i, elem in enumerate(lines):
        # pull unique patterns from each line
        up = elem.split('|')[0].strip().split(' ')
        unique_patterns.append(up)
        # pull output values from each line
        ov = elem.split('|')[1].strip().split(' ')
        output_values.append(ov)

    # Part 1:
    if part == 1:
        count = 0
        for i, elem in enumerate(output_values):
            for j, elem2 in enumerate(elem):
                #print(elem2, len(elem2))
                match len(elem2):
                    case 2:
                        # 1 = 1 segment
                        count += 1
                    case 3:
                        # 7 = 3 segments
                        count += 1
                    case 4:
                        # 4 = 4 segments
                        count += 1
                    case 7:
                        # 8 = 7 segments
                        count += 1
        return count
    
    # Part 2
    if part == 2:
        knowns_list = []
        for i, elem in enumerate(unique_patterns):
            # create list to store known values
            knowns = ['', '', '', '', '', '', '', '', '', '']
            # list of unknown 5s
            unknown5 = []
            # list of unknown 6s
            unknown6 = []
            # determine knowns
            for j, elem2 in enumerate(elem):
                match len(elem2):
                    case 2:
                        # 1 = 1 segment
                        knowns[1] = elem2
                    case 3:
                        # 7 = 3 segments
                        knowns[7] = elem2
                    case 4:
                        # 4 = 4 segments
                        knowns[4] = elem2
                    case 7:
                        # 8 = 7 segments
                        knowns[8] = elem2
                    case 5:
                        # 2,3,5
                        unknown5.append(elem2)
                    case 6:
                        # 0,6,9
                        unknown6.append(elem2)
            # make sets of known values for 1 and 4
            # used to determine other values
            s_1 = set([char for char in knowns[1]])
            s_4 = set([char for char in knowns[4]])
            # make a list of sets for each of the 6-lengths
            un6 = []
            for k, elem3 in enumerate(unknown6):
                un6.append(set([char for char in elem3]))
            for k2, elem32 in enumerate(un6):
                #print(elem32, s_1, elem32 & s_1, len(elem32 & s_1))
                # 0 has 2 intersections with 1
                if len(s_1 & elem32) == 2 and len(s_4 & elem32) != 4:
                    knowns[0] = ''.join(elem32)
                # 9 has 4 intersections with 4
                elif len(s_4 & elem32) == 4:
                    knowns[9] = ''.join(elem32)
                # else it is 6
                else:
                    knowns[6] = ''.join(elem32)
                    
            # make a list of sets for each of the 5-lengths
            un5 = []
            for l, elem4 in enumerate(unknown5):
                un5.append(set([char for char in elem4]))
            for l2, elem42 in enumerate(un5):
                # 3 has 2 intersections with 1
                if len(s_1 & elem42) == 2:
                    knowns[3] = ''.join(elem42)
                # 9 has 3 intersections with 4
                elif len(s_4 & elem42) == 3:
                    knowns[5] = ''.join(elem42)
                # else it is 2
                else:
                    knowns[2] = ''.join(elem42)
            knowns_list.append(knowns)

        # iterate through output values and compare to knowns
        count = 0
        for i, elem in enumerate(output_values):
            value = ''
            for j, elem2 in enumerate(elem):
                for k, elem3 in enumerate(knowns_list[i]):
                    if sorted(elem2) == sorted(elem3):
                        # build value as a string, to convert to int later
                        value = value + str(k)
                        break
            count = count + int(value)
        return count

o = decode_segments('input.txt', 1)
print("Part 1: Count: ", o)
o2 = decode_segments('input.txt', 2)
print("Part 2: Count: ", o2)