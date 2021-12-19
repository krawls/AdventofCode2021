# global grid
grid = []
# global variable
current_area = 0

def risk_level(filename):
    # open file for reading
    # also read().splitlines() gets rid of the \n character
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    # build our grid from input
    for i, elem in enumerate(lines):
        # convert to list of ints
        l = [int(x) for x in elem]
        grid.append(l)

    low_points = []
    basin_areas = []

    # use these to check for edge cases (literally)
    y_max = len(grid)-1
    x_max = len(grid[0])-1
    # iterate across every point and check adjacents
    for i, e in enumerate(grid):
        for j, e2 in enumerate(e):
            # 9 cannot be the lowest, so continue on when we see it
            if e2 == 9:
                continue
            # check value before
            # if we are on the left edge, don't eval
            if j == 0:
                pass
            else:
                # value before is less, so continue to next
                if e2 > e[j-1]:
                    continue
            # check value after
            # if we are on the right edge, don't eval
            if j == x_max:
                pass
            else:
                # value after is less, so continue to next
                if e2 > e[j+1]:
                    continue
            # check value above
            # if we are on the top edge, don't eval
            if i == 0:
                pass
            else:
                # value above is less, so continue to next
                if e2 > grid[i-1][j]:
                    continue
            # check value below
            # if we are on the bottom edge, don't eval
            if i == y_max:
                pass
            else:
                # value above is less, so continue to next
                if e2 > grid[i+1][j]:
                    continue
            # if we make it all the way down here, we are 
            # the lowest point of all 4 neighbors, yay!
            low_points.append(e2)

            # Part 2: find the area of the basin that includes this
            global current_area
            current_area = 0
            flood_fill(j,i)
            basin_areas.append(current_area)
            # sort list values large -> small
            basin_areas.sort(reverse=True)

    # add 1, then sum all the risk levels from low points list
    # Part 2: multiple 3 largest basin areas
    return sum([x+1 for x in low_points]), basin_areas[0]*basin_areas[1]*basin_areas[2]

def flood_fill(x, y):
    # use flood fill algorithm
    # https://en.wikipedia.org/wiki/Flood_fill
    # Stack-based recursive (four-way)
    # if node is not inside, return
    if grid[y][x] == 9:
        return
    # set the node
    grid[y][x] = 9
    # increment value for this basin
    global current_area
    current_area += 1
    # perform flood fill one step to the south of node
    if y < len(grid) - 1:
        flood_fill(x, y+1)
    # perform flood fill one step to the north of node
    if y > 0:
        flood_fill(x, y-1)
    # perform flood fill one step to the west of node
    if x > 0:
        flood_fill(x-1, y)
    # perform flood fill one step to the east of node
    if x < len(grid[0]) - 1:
        flood_fill(x+1, y)

o = risk_level('input.txt')
print("Part 1: Risk Level: ", o[0])
print("Part 2: 3 Largest Basin Sizes: ", o[1])