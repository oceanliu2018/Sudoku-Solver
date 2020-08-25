
def print_puzzle(puzzle):
    for i in range(9):
        print(puzzle[i])
    print()

class column:
    def __init__(self, puzzle, column_number):
        column_list = []
        for x in range(9):
            column_list.append(puzzle[x][column_number])
        self.column_list = column_list
class row:
    def __init__(self, puzzle, row_number):
        self.row_list = puzzle[row_number]
class box:
    def __init__(self, puzzle, box_number):
        box_list = []
        if box_number == 1:
            for x in range(0,3):
                box_list = box_list + puzzle[x][0:3]
        elif box_number == 2:
            for x in range(3,6):
                box_list = box_list + puzzle[x][0:3]
        elif box_number == 3:
            for x in range(6,9):
                box_list = box_list + puzzle[x][0:3]
        elif box_number == 4:
            for x in range(0,2):
                box_list = box_list + puzzle[x][3:6]
        elif box_number == 5:
            for x in range(3,6):
                box_list = box_list + puzzle[x][3:6]
        elif box_number == 6:
            for x in range(6,9):
                box_list = box_list + puzzle[x][3:6]
        elif box_number == 7:
            for x in range(0,3):
                box_list = box_list + puzzle[x][6:9]
        elif box_number == 8:
            for x in range(3,6):
                box_list = box_list + puzzle[x][6:9]
        elif box_number == 9:
            for x in range(6,9):
                box_list = box_list + puzzle[x][6:9]
        else:
            raise "incorrect box number"
        self.box_list = box_list

def get_box_number(x,y):
    if (0 <= x <= 2) and (0 <= y <= 2):
        return 1
    elif (3 <= x <= 5) and (0 <= y <= 2):
        return 2
    elif (6 <= x <= 8) and (0 <= y <= 2):
        return 3
    elif (0 <= x <= 2) and (3 <= y <= 5):
        return 4
    elif (3 <= x <= 5) and (3 <= y <= 5):
        return 5
    elif (6 <= x <= 8) and (3 <= y <= 5):
        return 6
    elif (0 <= x <= 2) and (6 <= y <= 8):
        return 7
    elif (3 <= x <= 5) and (6 <= y <= 8):
        return 8
    elif (6 <= x <= 8) and (6 <= y <= 8):
        return 9
def get_possible_numbers(puzzle,x,y):
    if puzzle[x][y] != 0:
        return []
    narrowed_numbers = row(puzzle, x).row_list + column(puzzle, y).column_list + box(puzzle, get_box_number(x,y)).box_list
    possible_numbers = set([1,2,3,4,5,6,7,8,9])
    return list(possible_numbers - set(narrowed_numbers))
def change_cell(puzzle,x,y,value):
    puzzle[x][y] = value
class cell:
    def __init__(self, puzzle, x, y):
        self.possible_numbers = get_possible_numbers(puzzle, x, y)
def check_row(puzzle, row_number):
    values = [cell(puzzle, row_number, y).possible_numbers for y in range(9)]
    all_values = []
    for list_ in values:
        all_values += list_
    for number in range(1,10):
        try:
            first_index = all_values.index(number)
        except:
            continue
        try:
            all_values.index(number,first_index + 1)
        except:
            for y in range(9):
                if number in values[y]:
                    change_cell(puzzle,row_number, y, number)
                    print('row' + ' {},{}'.format(row_number+1, y+1))
                    print_puzzle(puzzle)
                    break
def check_column(puzzle, col_number):
    values = [cell(puzzle, x, col_number).possible_numbers for x in range(9)]
    all_values = []
    for list_ in values:
        all_values += list_
    for number in range(1,10):
        try:
            first_index = all_values.index(number)
        except:
            continue
        try:
            all_values.index(number,first_index + 1)
        except:
            for x in range(9):
                if number in values[x]:
                    change_cell(puzzle, x, col_number, number)
                    print('column' + ' {},{}'.format(x+1, col_number+1))
                    print_puzzle(puzzle)
                    break
def check_box(puzzle, box_number):
    coord_list = []
    if box_number == 1:
        for x in range(0,3):
            for y in range(0,3):
                coord_list += [(x,y)]
    elif box_number == 2:
        for x in range(3,6):
            for y in range(0,3):
                coord_list += [(x,y)]
    elif box_number == 3:
        for x in range(6,9):
            for y in range(0,3):
                coord_list += [(x,y)]
    elif box_number == 4:
        for x in range(0,3):
            for y in range(3,6):
                coord_list += [(x,y)]
    elif box_number == 5:
        for x in range(3,6):
            for y in range(3,6):
                coord_list += [(x,y)]
    elif box_number == 6:
        for x in range(6,9):
           for y in range(3,6):
                coord_list += [(x,y)]
    elif box_number == 7:
        for x in range(0,3):
            for y in range(6,9):
                coord_list += [(x,y)]
    elif box_number == 8:
        for x in range(3,6):
            for y in range(6,9):
                coord_list += [(x,y)]
    elif box_number == 9:
        for x in range(6,9):
            for y in range(6,9):
                coord_list += [(x,y)]

    values = [cell(puzzle, x, y).possible_numbers for (x,y) in coord_list]
    all_values = []
    for list_ in values:
        all_values += list_
    for number in range(1,10):
        try:
            first_index = all_values.index(number)
        except:
            break
        try:
            all_values.index(number,first_index + 1)
        except:
            for index in range(9):
                if number in values[index]:
                    (x,y) = coord_list[index]
                    change_cell(puzzle, x, y, number)
                    print('box' + ' {},{}'.format(x+1,y+1))
                    print_puzzle(puzzle)
                    break


def solver(puzzle):
    for x in range(9):
        check_row(puzzle, x)
    for y in range(9):
        check_column(puzzle, y)
    for box_number in range(1,10):
        check_box(puzzle, box_number)
    
        

def victory_check(puzzle):
    for x in range(9):
        if 0 in puzzle[x]:
            return True
    
    print_puzzle(puzzle)
    print('Complete')

def main(puzzle):
    print('start')
    print_puzzle(puzzle)
    continue_solve = True
    while continue_solve:
        
        previous_iteration = str(puzzle)
        
        solver(puzzle)
        
        
        continue_solve = victory_check(puzzle)
        if previous_iteration == str(puzzle):
            print("Stuck")
            print_puzzle(puzzle)
            continue_solve = False
if __name__ == "__main__":
# Edit puzzle here:
    # puzzle = [[0,6,0,3,2,0,7,0,0],
    #           [0,2,0,0,0,0,0,0,4],
    #           [0,0,0,0,1,7,0,0,0],
    #           [0,5,7,0,0,0,0,6,0],
    #           [0,0,0,5,0,6,0,0,0],
    #           [0,8,0,0,0,0,5,2,0],
    #           [0,0,0,1,4,0,0,0,0],
    #           [5,0,0,0,0,0,0,8,0],
    #           [0,0,3,0,7,2,0,9,0] ]
    # puzzle = [[4,0,0,1,0,0,0,0,0],
    #           [0,0,9,8,7,0,0,0,1],
    #           [3,0,0,0,0,0,0,9,0],
    #           [0,0,0,0,0,7,0,3,0],
    #           [0,4,3,0,0,0,1,6,0],
    #           [0,8,0,2,0,0,0,0,0],
    #           [0,6,0,0,0,0,0,0,2],
    #           [7,0,0,0,5,8,6,0,0],
    #           [0,0,0,0,0,4,0,0,9] ]
    # puzzle = [[0,9,0,0,0,0,8,4,0],
    #           [4,0,0,0,0,8,0,0,5],
    #           [0,0,0,6,7,0,3,0,0],
    #           [0,4,0,7,0,0,0,0,0],
    #           [6,0,0,0,0,0,0,0,9],
    #           [0,0,0,0,0,5,0,7,0],
    #           [0,0,7,0,3,1,0,0,0],
    #           [2,0,0,0,0,0,0,0,1],
    #           [0,3,9,0,0,0,0,5,0] ]
    puzzle = [[7,0,6,0,0,0,0,1,0],
              [0,9,0,0,4,0,5,0,0],
              [0,2,0,0,0,9,6,0,0],
              [6,0,0,0,3,0,0,0,7],
              [0,0,0,0,0,0,0,0,0],
              [1,0,0,0,5,0,0,0,8],
              [0,0,9,1,0,0,0,5,0],
              [0,0,5,0,7,0,0,4,0],
              [0,1,0,0,0,0,2,0,3] ]
              
    main(puzzle)
    

    


