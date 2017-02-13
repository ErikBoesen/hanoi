#!/usr/bin/env python3

import curses
import time

stdscr = curses.initscr()

# Hide cursor
curses.curs_set(0)

# Number of disks
DISKS = 15
# Delay in between renders
DELAY = .1
CHAR = '▇'

# Define starting stacks
A = list(range(DISKS, 0, -1))
B = []
C = []


def move(n, src, end, aux):
    if n > 0:
        # Move n-1 disk out of the way
        move(n-1, src, aux, end)

        # Move n disk from src to end
        end.append(src.pop())

        stdscr.clear()
        stdscr.border(0)

        for i in reversed(A):
            stdscr.addstr(30-A.index(i), 10, (' '*(DISKS-i)) + (CHAR*2*i))

        for i in reversed(B):
            stdscr.addstr(30-B.index(i), 60, (' '*(DISKS-i)) + (CHAR*2*i))

        for i in reversed(C):
            stdscr.addstr(30-C.index(i), 110, (' '*(DISKS-i)) + (CHAR*2*i))

        for i in range(0, 3):
            stdscr.addstr(32, 10+50*i-2+DISKS, '-#%s-' % (i+1))

        stdscr.refresh()

        time.sleep(DELAY)

        # move the n-1 disks that we left on aux onto end
        move(n-1, aux, end, src)


# initiate call from src A to end C with aux B
move(len(A), A, C, B)

x = 0
x = stdscr.getch()

curses.endwin()
