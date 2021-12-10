def parse_file(filename, part):
    max_x_dim = 999
    max_y_dim = 999

    # open file for reading
    # also read().splitlines() gets rid of the \n character
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    chart = []

    # initialize chart as 2D 999x999 board (based on max input size)
    for i in range(max_y_dim):
        chart.append([])
        for j in range(max_x_dim):
            chart[i].append(0)

    # iterate through each set of points and extract the start and end
    # formateed like: x1,y1 -> x2,y2
    for i, elem in enumerate(lines):
        e = elem.split(" ")
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0
        for j, elem2 in enumerate(e):
            if j == 0:
                pos = elem2.split(',')
                x1 = int(pos[0])
                y1 = int(pos[1])
            elif j == 2:
                pos = elem2.split(',')
                x2 = int(pos[0])
                y2 = int(pos[1])
        
        # now that we have our two points, we need to figure out how to mark them on the board
        # they could be either: 
        # horizontal (y1 == y2)
        # vertical (x1 == x2)
        # slope = +1 ((y2 > y1) and (x2 > x1)) OR ((y1 > y2) and (x1 > x2))
        # slope = -1 ((y2 > y1) and (x2 < x1)) OR ((y1 > y2) and (x2 > x1))
        if y1 == y2:
            # find the start and stop of the range, since it could be either
            # also assume no single point line segments
            if x1 < x2:
                start = x1
                stop = x2
            else:
                start = x2
                stop = x1
            for i in range(start, stop+1):
                chart[y1][i] += 1
        if x1 == x2:
            # find the start and stop of the range, since it could be either
            # also assumes no single point line segments
            if y1 < y2:
                start = y1
                stop = y2
            else:
                start = y2
                stop = y1
            for i in range(start,stop+1):
                chart[i][x1] +=1
        # only consider diagonals for part==2
        if part == 2:
            # slope = +1
            if ((y2 > y1) and (x2 > x1)):
                # lower-left point is (x1,y1)
                for i in range(x2-x1+1):
                    chart[y1+i][x1+i] += 1
            elif ((y1 > y2) and (x1 > x2)):
                # lower-left point is (x2,y2)
                for i in range(x1-x2+1):
                    chart[y1-i][x1-i] += 1
            # slope = -1
            elif ((y2 > y1) and (x2 < x1)):
                # upper-left point is (x1,y1)
                for i in range(x1-x2+1):
                    chart[y1+i][x1-i] += 1
            elif ((y1 > y2) and (x2 > x1)):
                # upper-left point is (x2,y2)
                for i in range(x2-x1+1):
                    chart[y1-i][x1+i] += 1

    # iterate over final board and return number of spaces with values >= 2
    count = 0
    for i, e1 in enumerate(chart):
        for j, e2 in enumerate(e1):
            if int(e2) >= 2:
                count += 1
    return count

o = parse_file('input.txt',1)
print("Part 1: Count: ", o)
o2 = parse_file('input.txt',2)
print("Part 2: Count: ", o2)