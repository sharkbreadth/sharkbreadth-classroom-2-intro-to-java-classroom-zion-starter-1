import random
import curses

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)  # Hide the cursor
sh, sw = stdscr.getmaxyx()  # Get screen dimensions
w = curses.newwin(sh, sw, 0, 0)  # Create a new window
w.keypad(1)  # Enable keypad mode
w.timeout(100)  # Set refresh rate

# Initial snake position and food
snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

food = [sh // 2, sw // 2]
w.addch(food[0], food[1], curses.ACS_PI)  # Display food symbol

# Initial snake movement direction
key = curses.KEY_RIGHT

# Game loop
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Check if snake hits the wall or itself
    if (snake[0][0] in [0, sh]) or (snake[0][1] in [0, sw]) or (snake[0] in snake[1:]):
        curses.endwin()
        quit()

    # Calculate new head position
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    # Check if snake eats the food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # Display snake
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

curses.endwin()
