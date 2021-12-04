# Part 1
# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position.
# The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used.
# The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

def determine_power_consumption(filename):
    # open file for reading (with is a better way to do this apparently!)
    # also read().splitlines() gets rid of the \n character
    with open(filename, 'r') as file:
        lines = file.read().splitlines()


    #initialize a zeroed running total list to the size of the input
    list_len = len(lines[0])  # referenced a few places, so made its own variable
    totals_list = [0]*list_len
    total_size = len(lines)

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # for each element in the file, split the values into a list
        # e.g. 010110 becomes [0,1,0,1,1,0]
        # iterate down this new list and add up each individual element to a running total for all the lines in the file
        for j, elem in enumerate(list(line)):
            if int(elem) == 1:
                totals_list[j]+=1

    # now we have a totlized list from each position
    # if the total is > the total input size /2, then mark the most common bit for gamma rate
    # NOTE: it doesn't specify what to do if there's an even number and it's exactly half, so assuming that goes to least common bit
    # epsilon rate is just the inverse, so we'll create that list at the same time, just... opposite values

    gamma_rate_list = [0]*list_len
    epsilon_rate_list = [0]*list_len

    for i, elem in enumerate(totals_list):
        if int(elem) > total_size / 2:
            gamma_rate_list[i] = 1
            epsilon_rate_list[i] = 0
        else:
            gamma_rate_list[i] = 0
            epsilon_rate_list[i] = 1
    
    # squish the list together into a binary string and convert to an integer in decimal
    s = [str(i) for i in gamma_rate_list]
    gamma_rate = int("".join(s),2)
    s = [str(i) for i in epsilon_rate_list]
    epsilon_rate = int("".join(s),2)

    return gamma_rate, epsilon_rate, gamma_rate*epsilon_rate

# Part 2
# To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, 
# and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
# To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in 
# that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
# The life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating

def determine_life_support_rating(filename):
    # open file for reading
    # also read().splitlines() gets rid of the \n character
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    oxygen_generator_rating = determine_oxygen_generator_rating(lines)
    CO2_scrubber_rating = determine_CO2_scrubber_rating(lines)

    return oxygen_generator_rating, CO2_scrubber_rating, oxygen_generator_rating*CO2_scrubber_rating, 

def determine_oxygen_generator_rating(list):
    # determine oxygen generator rating
    for i in range(len(list[0])):
        list = filter_list(list, i, "most")
        if len(list)==1:
            break
    return int(list[0],2)

def determine_CO2_scrubber_rating(list):
    # determine oxygen generator rating
    for i in range(len(list[0])):
        list = filter_list(list, i, "least")
        if len(list)==1:
            break
    return int(list[0],2)

# given a list of binary numbers and a position, return list with only values according to type ("most/least") common
def filter_list(list, pos, type):
    # count number of 1s at given position
    count = 0
    # determine total list size
    total_size = len(list)
    # create return list
    return_list = []

    # enumerate() will return an index and element
    for i, l in enumerate(list):
        if int(l[pos])==1:
            count+=1
    
    # determine if 1/0 is most common value found
    # for most common: If 0 and 1 are equally common, keep values with a 1 in the position being considered.
    # for least common: If 0 and 1 are equally common, keep values with a 0 in the position being considered.
    if count > total_size / 2:
        most_common = 1
    elif count < total_size / 2:
        most_common = 0
    elif count == total_size / 2:
        most_common = 1
    # iterate through and add elements in the return list based on type
    for i, l in enumerate(list):
        if type=="most" and int(l[pos]) == most_common:
            return_list.append(l)
        elif type=="least" and int(l[pos]) != most_common:
            return_list.append(l)
    
    return return_list

output = determine_power_consumption('input.txt')
output2 = determine_life_support_rating('input.txt')
print("Part 1: Gamma Rate: ", output[0], " Epsilon Rate: ", output[1], " Multiplied: ", output[2])
print("Part 2: Oxygen Generator Rating: ", output2[0], " CO2 Scrubber Rating: ", output2[1], " Multipied: ", output2[2])