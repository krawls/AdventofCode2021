def max_height(filename):
    # open file for reading
    # also read().splitlines() gets rid of the \n character
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    l = lines[0].split(' ')
    target_min_x = int(l[2][l[2].find("=")+1:l[2].find("..")])
    target_max_x = int(l[2][l[2].find("..")+2:l[2].find(",")])
    target_min_y = int(l[3][l[3].find("=")+1:l[3].find("..")])
    target_max_y = int(l[3][l[3].find("..")+2:])

    overall_max_height = -9999999999999999
    count = 0

    # brute force x_vel and y_vel to see what makes largest value
    # set these range limits based on possible values from the 
    # given input (ie won't be larger than max target x/y)
    for starting_x_vel in range(0,300,1):
        for starting_y_vel in range(-200,999,1):
            # start the projectile at the origin
            cur_x_pos = 0
            cur_y_pos = 0
            cur_x_vel = starting_x_vel
            cur_y_vel = starting_y_vel
            iteration_max_height = -9999999999999999
            # for the given x_vel and y_vel simulate each step 
            increment = True
            in_target = False
            while increment:
                # continuously record max heigh in this iteration
                if cur_y_pos > iteration_max_height:
                    iteration_max_height = cur_y_pos
                r = in_target_area(cur_x_pos, cur_y_pos, target_min_x, target_max_x, target_min_y, target_max_y)
                if r[0]:
                    in_target = True
                    break
                # we can no longer reach target
                if r[0] == False and r[1] == False:
                    break
                
                # increment the position for the next loop
                i = increment_position(cur_x_pos, cur_y_pos, cur_x_vel, cur_y_vel)
                cur_x_pos = i[0]
                cur_y_pos = i[1]
                cur_x_vel = i[2]
                cur_y_vel = i[3]

            if in_target == False:
                # we did not reach our target
                pass
            else:
                # we did reach our target
                # check the max heigh of the iteration vs the overall
                if iteration_max_height > overall_max_height:
                    overall_max_height = iteration_max_height
                # Part 2: increment counter when we find a valid initial velocity value
                count += 1
    return overall_max_height, count

def increment_position(x, y, x_v, y_v):
    # increment the current position with the following rules:
    # x position increases by x velocity
    # y position increases by y velocity
    # x velocity changes by 1 toward 0
    # y velocity decreases by 1
    if x_v > 0:
        new_x_v = x_v - 1
    elif x_v < 0:
        new_x_v = x_v + 1
    else:
        new_x_v = 0
    return x+x_v, y+y_v, new_x_v, y_v-1

def in_target_area(x, y, target_min_x, target_max_x, target_min_y, target_max_y):
    # return true or false if the given x, y is within the target area
    # also return true if the given x,y can still reach on another iteration
    
    # position is within target
    if x >= target_min_x and x <= target_max_x and y>=target_min_y and y<=target_max_y:
        return True, True
    # position is too far to right of target
    elif x > target_max_x:
        return False, False
    # position is too far below target
    elif y < target_min_y:
        return False, False
    # otherwise position must be above or left of target
    else:
        return False, True

o = max_height('input.txt')
print("Part 1: Max Height: ", o[0])
print("Part 2: Distict Initial Velocities: ", o[1])