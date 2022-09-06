import curses                                                                  
from curses import wrapper
from pickle import REDUCE
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "O", "#", "#", "#",],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#",],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#",],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#",],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#",],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#",],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#",],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#",],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#",],
]

def print_maze(maze, stdscr, path=[]):
    BlUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            stdscr.addstr(i, j*2, value, BlUE)
        
        



def main(stdscr):                                                               # MainFunk (Standard output screen)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)                  # Coloring (ID, the Color, back Color)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # blue_and_black = curses.color_pair(1)                                     # Argument what call the ID

    stdscr.clear()                                                              # Clear screen if run.
    print_maze(maze, stdscr)
    # stdscr.addstr(5, 10, "hell world!", blue_and_black)                       # str (row, column, "str", Argument)
    stdscr.refresh()                                                            
    stdscr.getch()                                                              # getCharacter (to refresh in this case)

wrapper(main)                                                                   # Call the Funk, pass the (stdscr)Object, to us and control the output



