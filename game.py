import numpy as np
import random as rnd




def set_rand_cell(field):
    rand_сell = rnd.randint(0, field.shape[0]**2 - 1)
    while field[rand_сell // field.shape[0], rand_сell % field.shape[0]] != 0:
        rand_сell = rnd.randint(0, field.shape[0]**2 - 1)
    field[rand_сell // field.shape[0], rand_сell % field.shape[0]] = 2


def shift_left(field):
    global score
    global mov_fl
    mov_fl = 0
    for i in range(field.shape[0]):

        for j in range(field.shape[0]):
            if field[i, j] != 0:
                j_c = j
                while j_c != 0 and field[i,j_c-1] == 0:
                    field[i,j_c-1] = field[i,j_c]
                    field[i,j_c] = 0
                    j_c -= 1
                    mov_fl = 1

        for j in range(field.shape[0] - 1):
            if field[i,j] == field[i,j+1]:
                field[i,j] *= 2
                field[i,j+1] = 0
                score += field[i,j]

        for j in range(field.shape[0]):
            if field[i,j] != 0:
                j_c = j
                while j_c != 0 and field[i,j_c-1] == 0:
                    field[i,j_c-1] = field[i,j_c]
                    field[i,j_c] = 0
                    j_c -= 1
                    mov_fl = 1
    return mov_fl

def shift_right(field):
    global score
    global mov_fl
    for i in range(field.shape[0]):

        for j in range(field.shape[0]-2,-1,-1):
            if field[i,j] != 0:
                j_c = j
                while j_c != field.shape[0] - 1 and field[i,j_c+1] == 0:
                    field[i,j_c+1] = field[i,j_c]
                    field[i,j_c] = 0
                    j_c += 1
                    mov_fl = 1

        for j in range(field.shape[0] - 1, -1, -1):
            if field[i,j] == field[i,j - 1]:
                field[i,j] *= 2
                field[i,j-1] = 0
                score += field[i, j]


        for j in range(field.shape[0]-2,-1,-1):
            if field[i,j] != 0:
                j_c = j
                while j_c != field.shape[0] - 1  and field[i,j_c+1] == 0:
                    field[i,j_c+1] = field[i,j_c]
                    field[i,j_c] = 0
                    j_c += 1
                    mov_fl = 1

    return mov_fl

def shift_up(field):
    global score
    global mov_fl
    for j in range(field.shape[0]):

        for i in range(field.shape[0]):
            if field[i, j] != 0:
                i_c = i
                while i_c != 0 and field[i_c - 1,j] == 0:
                    field[i_c-1,j] = field[i_c,j]
                    field[i_c,j] = 0
                    i_c -= 1
                    mov_fl = 1

        for i in range(field.shape[0] - 1):
            if field[i,j] == field[i+1,j]:
                field[i,j] *= 2
                field[i+1,j] = 0
                score += field[i, j]

        for i in range(field.shape[0]):
            if field[i, j] != 0:
                i_c = i
                while i_c != 0 and field[i_c - 1, j] == 0:
                    field[i_c - 1, j] = field[i_c, j]
                    field[i_c, j] = 0
                    i_c -= 1
                    mov_fl = 1
    return mov_fl


def shift_down(field):
    global score
    global mov_fl
    for j in range(field.shape[0]):
        for i in range(field.shape[0]-2,-1,-1):
            if field[i,j] != 0:
                i_c = i
                while i_c != field.shape[0] - 1  and field[i_c+1,j] == 0:
                    field[i_c+1,j] = field[i_c,j]
                    field[i_c,j] = 0
                    i_c += 1
                    mov_fl = 1

        for i in range(field.shape[0] - 1, -1, -1):
            if field[i,j] == field[i-1, j]:
                field[i,j] *= 2
                field[i-1,j] = 0
                score += field[i, j]


        for i in range(field.shape[0]-2,-1,-1):
            if field[i,j] != 0:
                i_c = i
                while i_c != field.shape[0] - 1  and field[i_c+1,j] == 0:
                    field[i_c+1,j] = field[i_c,j]
                    field[i_c,j] = 0
                    i_c += 1
                    mov_fl = 1

    return mov_fl

def check_free(field):
    cnt = 0
    for j in range(field.shape[0]):
        for i in range(field.shape[1]):
            if field[i, j] > 0:
                cnt += 1
    if cnt == field.shape[0] ** 2:
        return (False, 0)
    return True,field.shape[0] ** 2 - cnt


def check_if_lose(field):
    cur_field = np.copy(field)
    shift_down(cur_field)
    if check_free(cur_field)[0] == True:
        return False
    shift_right(cur_field)
    if check_free(cur_field)[0] == True:
        return False
    shift_left(cur_field)
    if check_free(cur_field)[0] == True:
        return False
    shift_up(cur_field)
    if check_free(cur_field)[0] == True:
        return False
    return True


def logic(field):
        dir = input()
        if dir == 'a':
            shift_left(field)

        if dir == 's':
            shift_down(field)

        if dir == 'd':
            shift_right(field)

        if dir == 'w':
            shift_up(field)






def ai_gamer(field):
    global mov_fl
    global score
    copy_score = score
    tmp_field = np.copy(field)
    shift_up(tmp_field)
    if mov_fl == 1:
        up_profit = check_free(tmp_field)[1] + score
    else:
        up_profit = -1
    mov_fl = 0
    score = copy_score

    tmp_field = np.copy(field)
    shift_left(tmp_field)
    if mov_fl == 1:
        left_profit = check_free(tmp_field)[1] + score
    else:
        left_profit = -1
    mov_fl = 0
    score = copy_score

    tmp_field = np.copy(field)
    shift_right(tmp_field)

    if mov_fl == 1:
        right_profit = check_free(tmp_field)[1] + score
    else:
        right_profit = -1
    mov_fl = 0
    score = copy_score


    prof_list = [up_profit,left_profit,right_profit]
    m_ind = prof_list.index(max(prof_list))

    if m_ind == 0:
        shift_up(field)
    if m_ind == 1:
        shift_left(field)
    if m_ind == 2:
        shift_right(field)
    if m_ind == 3:
        shift_down(field)





score = 0
mov_fl = 0
step = 0

def game():
    global score
    global mov_fl
    print('Enter field size')
    size = int(input())
    g_field = np.zeros((size, size))
    set_rand_cell(g_field)
    set_rand_cell(g_field)
    print(g_field)
    while True:
        logic(g_field)
        #ai_gamer(g_field)
        if mov_fl == 1:
            set_rand_cell(g_field)
        if check_free(g_field)[0] == False:
            if check_if_lose(g_field) == True:
                print('LOOOSER')
                print(g_field)
                print(score)
                break
        print(g_field)
        mov_fl = 0


game()
