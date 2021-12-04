class BingoBoard:
    # initialize zero'd 2D 5x5 board
    blank_board = []
    for i in range(5):
        blank_board.append([])
        for j in range(5):
            blank_board[i].append([])
            for k in range(2):
                blank_board[i][j].append(0)

    def __init__(self,b=blank_board):
        self.completed = False

        # initialize a zerod' 2D 5x5x2 list
        self.board = []
        for i in range(5):
            self.board.append([])
            for j in range(5):
                self.board[i].append([])
                for k in range(2):
                    self.board[i][j].append(0)

        # build board based on given input
        # [0] = value
        # [1] = marked or not
        for i in range(0, 5):
            for j in range(0, 5):
                self.board[i][j][0] = int(b[i][j])
                self.board[i][j][1] = 0

    def print(self):
        print(self.board)

    # given value, mark if value on the board, if it exists
    # if value does exist, then check if that value creates a winning board
    def mark(self,val):
        break_loop = False
        for i, elem1 in enumerate(self.board):
            # assume unique values, so we can stop looking when we find our value
            if break_loop:
                break
            for j, elem2 in enumerate(elem1):
                if self.board[i][j][0] == val:
                    self.board[i][j][1] = 1
                    # break out of this loop and outer loop
                    break_loop = True
                    break
        # only return True if it's the first row/col to be completed.
        # Part 2 may have multiples before completing
        if self.check_winner() and self.completed == False:
            self.completed = True
            return True, val
        else:
            return False, None

    # check for a winning board
    # winning board can be horizontal or vertical
    def check_winner(self):
        # for a 5x5 board, assume all verticals and horizontals are 'marked' 
        # one instance of an unmarked will set it false (0)
        v_check=[1,1,1,1,1]
        h_check=[1,1,1,1,1]
        for i, elem1 in enumerate(self.board):
            for j, elem2 in enumerate(elem1):
                if elem2[1] == 0:
                    v_check[j]=0
                    h_check[i]=0
        if v_check.count(1) or h_check.count(1):
            return True
        else:
            return False

    # sum all unmarked elements on the board
    def sum_unmarked(self):
        sum = 0

        # iterate over the board
        for i, elem1 in enumerate(self.board):
            for j, elem2 in enumerate(elem1):
                # [0] = value
                # [1] = marked or not
                if elem2[1] == 0:
                    sum += elem2[0]
        return sum


def parse_file(filename):
    # open file for reading
    # also read().splitlines() gets rid of the \n character
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    # draw numbers are the first line of the input
    draw_numbers = lines[0].split(',')

    # hold parsed boards
    boards = []

    # iterate and find the boards every 5 after a blank line
    for i, elem in enumerate(lines):
        tmp_board = []
        # need to strip spaces/other characters
        elem = elem.strip()
        #find a blank line
        if elem == '':
            for j in range(0,5):
                # iterates the next few lines and create a temp list of those numbers
                # need to strip to get rid of leading spaces, and replace double spaces with single to sanitize the inputs
                # append these to a temp_board to send to the BingoBoard class
                e = lines[i+j+1].strip().replace('  ',' ').split(' ')
                tmp_board.append(e)
            bb = BingoBoard(tmp_board)
            boards.append(bb)

    return draw_numbers, boards

# return the first board that is a winner
def win_first(filename):
    parse_output = parse_file(filename)

    for i, elem in enumerate(parse_output[0]):
        for k, b in enumerate(parse_output[1]):
            m = b.mark(int(elem))
            if m[0] == True:
                val = m[1]
                sum = b.sum_unmarked()
                return sum, val, val*sum
    # if we get here, then we didn't get a result: BAD
    return "bad", "bad", "bad"

# return when the final board has a winner
def win_last(filename):
    parse_output = parse_file(filename)

    # determine total number of boards
    total_board_count = len(parse_output[1])
    print("Total: ",total_board_count)
    count = 0

    for i, elem in enumerate(parse_output[0]):
        for k, b in enumerate(parse_output[1]):
            m = b.mark(int(elem))
            if m[0] == True:
                count += 1
                # when the count reaches the total number of boards, we have found the last one
                if count == total_board_count:
                    val = m[1]
                    sum = b.sum_unmarked()
                    return sum, val, val*sum
    # if we get here, then we didn't get a result: BAD
    return "bad", "bad", "bad"


o = win_first('input.txt')
print("Part 1: Unmarked Sum: ", o[0], " Winning Value: ", o[1], " Multiplied: ", o[2])
o2 = win_last('input.txt')
print("Part 2: Unmarked Sum: ", o2[0], " Winning Value: ", o2[1], " Multiplied: ", o2[2])