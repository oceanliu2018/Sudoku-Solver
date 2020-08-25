import random, pygame, sys, time
from pygame.locals import *
import sudoku_solver

square_size = 50
fps = 30
window_height = 700
window_length = 550
WHITE    = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
number_icon_size = 50
box_coord_tuple = tuple(range(square_size, 10*square_size, square_size))
ONE = pygame.image.load(r'Sudoku_Icons\one.png')
TWO = pygame.image.load(r'Sudoku_Icons\two.png')
THREE = pygame.image.load(r'Sudoku_Icons\three.png')
FOUR = pygame.image.load(r'Sudoku_Icons\four.png')
FIVE = pygame.image.load(r'Sudoku_Icons\five.png')
SIX = pygame.image.load(r'Sudoku_Icons\six.png')
SEVEN = pygame.image.load(r'Sudoku_Icons\seven.png')
EIGHT = pygame.image.load(r'Sudoku_Icons\eight.png')
NINE = pygame.image.load(r'Sudoku_Icons\nine.png')
SOLVE = pygame.image.load(r'Sudoku_Icons\solve.png')
DELETE = pygame.image.load(r'Sudoku_icons\delete.png')
delete_icon_location = (square_size,square_size*12)
solve_icon_location = (square_size,square_size*13)
solve_icon_height = 50
solve_icon_length = 150
images = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
icon_rect = [pygame.Rect(square_size * (i), square_size* 11, number_icon_size, number_icon_size)
                for i in range(1,10)]
coordinates_rect = []
for y in range(1,10):
    coordinates_rect.append(
             [pygame.Rect(square_size * x, square_size * y, square_size, square_size) for x in range(1,10)]
        )

def get_box_index(x,y):
    for box_x in box_coord_tuple:
        for box_y in box_coord_tuple:
            box_rectange = pygame.Rect(box_x, box_y, square_size, square_size)
            if box_rectange.collidepoint(x,y):
                return (box_x, box_y)
def draw_grid(display):
    for x in box_coord_tuple:
        for y in box_coord_tuple:
            
            pygame.draw.rect(display, BLACK, (x,y,square_size,square_size),2)
    for index in range(9):
        display.blit(images[index], (box_coord_tuple[index], square_size * 11))
def display_puzzle(display, puzzle, box_coord_tuple, images):
    
    for index_x in range(9):
        for index_y in range(9):
            number = puzzle[index_y][index_x]
            if number == 0:
                pass
            else:
                display.blit(images[number-1], (box_coord_tuple[index_x],box_coord_tuple[index_y]))
    draw_grid(display)



def main(puzzle):
    pygame.init()
    fpsClock = pygame.time.Clock()
    display = pygame.display.set_mode((window_length,window_height))

    pygame.display.set_caption('Sudoku')
    display.fill(WHITE)
 
    display_puzzle(display, puzzle, box_coord_tuple, images)
    display.blit(SOLVE, solve_icon_location)
    display.blit(DELETE, delete_icon_location)
    delete_icon = pygame.Rect(delete_icon_location[0],delete_icon_location[1], solve_icon_length, solve_icon_height)
    solve_icon = pygame.Rect(solve_icon_location[0], solve_icon_location[1], solve_icon_length, solve_icon_height) 
    pygame.display.update()
    time.sleep(1)
    fpsClock.tick(fps)
    
        
    stored_number = None
    stored_position = None
    while True:
        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == MOUSEMOTION:
                mouse_x,mouse_y = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                mouse_clicked = True
        pygame.display.update()
        if mouse_clicked and solve_icon.collidepoint(mouse_x,mouse_y):
            continue_solve = True
            
            while continue_solve:
                previous_iteration = str(puzzle)
                for x in range(9):
                    sudoku_solver.check_row(puzzle, x)
                    display_puzzle(display, puzzle, box_coord_tuple, images)
                    pygame.display.update()
                for y in range(9):
                    sudoku_solver.check_column(puzzle, y)
                    display_puzzle(display, puzzle, box_coord_tuple, images)
                    pygame.display.update()
                for box_number in range(1,10):
                    sudoku_solver.check_box(puzzle, box_number)
                    display_puzzle(display, puzzle, box_coord_tuple, images)
                    pygame.display.update()
                continue_solve = sudoku_solver.victory_check(puzzle)
                if previous_iteration == str(puzzle):
                    print("Stuck")
                    continue_solve = False
        for index in range(9):
            if mouse_clicked and icon_rect[index].collidepoint(mouse_x, mouse_y):
                stored_number = index + 1
             
        for x_index in range(9):
            for y_index in range(9):
                if mouse_clicked and coordinates_rect[x_index][y_index].collidepoint(
                    mouse_x, mouse_y):
                    stored_position = (x_index, y_index)
        if mouse_clicked and delete_icon.collidepoint(mouse_x, mouse_y):
            stored_number = 0
        if stored_position != None and stored_number == 0:
            for x in box_coord_tuple:
                for y in box_coord_tuple:
                    pygame.draw.rect(display, WHITE, (x,y,square_size,square_size))
        if (stored_number != None) and (stored_position != None):
            sudoku_solver.change_cell(puzzle,
                                        stored_position[0],
                                        stored_position [1],
                                        stored_number)
            stored_number = None
            stored_position = None
            display_puzzle(display, puzzle, box_coord_tuple, images)
            pygame.display.update()
                            

puzzle = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

main(puzzle)
