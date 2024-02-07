print("snake goes here")

#By Jacen Schechter

import random, os, time, keyboard, colorama
from colorama import Fore, Back

appleprint, emptyprint, headprint, bodyprint = Back.RED+Fore.GREEN+'**'+Back.RESET+Fore.RESET, Back.GREEN+'  '+Back.RESET, Back.BLUE+'\'\''+Back.RESET, Back.BLUE+'  '+Back.RESET

print(Back.RESET,Fore.RESET)

def setup_board():
    global numofapls, board, tails, heading, head, score, apples
    apples=list()
    heading='right'
    score=0
    head=(5,3)
    tails=list()
    tails.append((5,2))
    board = list()
    for i in range(0,10):
        board.append(list())
        for j in range(0,10):
            board[i].append(emptyprint)
    board[5][3] = headprint
    board[5][2] = bodyprint
    while True:
        try:
            numofapls=int(input("enter a number of apples to have on the board\n> "))
            break
        except:
            pass

def get_empty_spaces():
    empty_spaces = []
    for i in range(0,10):
        for j in range(0,10):
            if board[i][j]==emptyprint:
                empty_spaces.append((i,j))
    return empty_spaces

def get_apple_spaces(): #to get number of apples, use get_apple_spaces().__len__()
    apple_spaces = []
    for i in range(0,10):
        for j in range(0,10):
            if board[i][j]==appleprint:
                apple_spaces.append((i,j))
    return apple_spaces

def set_apples():
    while (numofapls>get_apple_spaces().__len__()) and get_empty_spaces().__len__()>0:
        coords = random.choice(get_empty_spaces())
        board[coords[0]][coords[1]] = appleprint
        apples.append((coords[0],coords[1]))


def printboard():
    os.system('cls') #-------------------------------------------------------------------------------------------------comment to show steps for debugging
    print("Snake game coded by Jacen Schechter")
    print(" ____________________")
    for i in range(0,10):
        print('|'+Back.GREEN,end='')
        for j in range(0,10):
            print(board[i][j], end='') if j!=9 else print(board[i][j]+Back.RESET+'|')
    print(Back.RESET+" ''''''''''''''''''''") #-----------------------------------------------------------------------------------change ' to an ASCII for _ on top of character

def move():
    global numofapls, board, tails, heading, head, score, apples, running, paused
    if heading=='right':
        space_to_move = (head[0],head[1]+1)
    elif heading=='left':
        space_to_move = (head[0],head[1]-1)
    elif heading=='up':
        space_to_move = (head[0]-1,head[1])
    elif heading=='down':
        space_to_move = (head[0]+1,head[1])
    if space_to_move[0]>9 or space_to_move[0]<0 or space_to_move[1]>9 or space_to_move[1]<0 or space_to_move in tails:
        os.system('cls')
        printboard()
        running = False
        paused = True
        input(f'you lose. your score was {score}. (press [ENTER] to continue)')#------------------------end
    elif space_to_move in apples:
        score+=1
        apples.__delitem__(apples.index(space_to_move))
        board[head[0]][head[1]]=bodyprint
        board[space_to_move[0]][space_to_move[1]]=headprint
        tails.append(head)
        head=space_to_move
    else:
        board[tails[0][0]][tails[0][1]]=emptyprint
        tails.__delitem__(0)
        board[head[0]][head[1]]=bodyprint
        board[space_to_move[0]][space_to_move[1]]=headprint
        tails.append(head)
        head=space_to_move

def check_for_win():
    global running, paused
    if get_empty_spaces().__len__()==0 and get_apple_spaces().__len__()==0:
        os.system('cls')
        printboard()
        input(f'You beat the game! your score was {score}. (press [ENTER] to continue)')#---------------end
        running = False
        paused = True

def moveup():
    global heading
    if heading != 'down':
        heading = 'up'
def moveleft():
    global heading
    if heading != 'right':
        heading = 'left'
def movedown():
    global heading
    if heading != 'up':
        heading = 'down'
def moveright():
    global heading
    if heading != 'left':
        heading = 'right'
paused = False
def pause():
    keyboard.remove_all_hotkeys()
    global paused, running
    paused = True
    while paused:
        try:
            if input('enter \"quit\" to quit, press [ENTER] to continue otherwise\n> ').lower()=='quit':
                quitcode()
            else:
                event_listener()
                paused=False
        except:
            event_listener()
            paused=False

def event_listener():
    keyboard.add_hotkey(hotkey='w',callback=moveup)
    keyboard.add_hotkey(hotkey='a',callback=moveleft)
    keyboard.add_hotkey(hotkey='s',callback=movedown)
    keyboard.add_hotkey(hotkey='d',callback=moveright)
    keyboard.add_hotkey(hotkey='up',callback=moveup)
    keyboard.add_hotkey(hotkey='left',callback=moveleft)
    keyboard.add_hotkey(hotkey='down',callback=movedown)
    keyboard.add_hotkey(hotkey='right',callback=moveright)
    keyboard.add_hotkey(hotkey='escape',callback=pause)

def play():
    global running, heading, speed, paused
    paused = False
    running = True
    setup_board()
    speed = -1
    speeds = [.2,.15,.1]
    while speed not in speeds:
        try:
            speed = int(input("Enter snake speed (1, 2, or 3)\n> "))
        except:
            continue
        speed = speeds[speed-1]
    heading='right'
    event_listener()
    while running:
        while not paused:
            if quitting:
                quitcode()
            set_apples()
            move()
            printboard()
            check_for_win()
            time.sleep(speed)
    keyboard.remove_all_hotkeys()
    print('done')

quitting = False

def quitcode():
    global quitting
    quitting = True
    print('quitting...')
    quit()

#---Run-Code---

while True:
    if quitting:
        quitcode()
    os.system('cls')
    try:
        if str(input('Do you want to play snake? [y/n]\n> ')).strip().lower()=='y':
            play()
        else:
            if str(input('Are you sure you want to quit? [y/n]\n> ')).strip().lower()=='y':
                quitcode()
    except:
        pass