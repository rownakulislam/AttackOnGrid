import math
import numpy as np

mat=[['', '', '', '', 'w2', 'p'], ['', '', '', '', '', ''], ['s3', 'w2', '', 'w1', '', ''], ['', '', '', 's2', '', ''], ['', 'w1', '', 'w3', '', ''], ['', '', '', '', 's1', ''], ['', '', '', '', 'w3', ''], ['a', '', '', '', '', '']]
dir=[(1,0),(0,-1),(-1,0),(0,1)]
iteration=0
n=8
m=6

def get_cells(mat,x,y,n,m,bx,by):
    cells=[]
    for i in range(len(dir)):
        temp=dir[i]
        if((x+temp[0]>=0 and x+temp[0]<n) and (y+temp[1]>=0 and y+temp[1]<m) ):
            if(mat[x+temp[0]][y+temp[1]]!='a' and mat[x+temp[0]][y+temp[1]]!='p'):
                if (x+temp[0],y+temp[1])!=(bx,by):
                    cells.append((x+temp[0],y+temp[1]))
    return cells

def winner(player_health,ai_health,mat1,n,m):
    if(ai_health<=0):
        return -1
    elif(player_health<=0):
        return 1
    flag=True
    for i in range (0,n):
        for j in range(0,m):
            if(mat1[i][j]=='w1' or mat1[i][j]=='w2' or mat1[i][j]=='w3'):
                flag=False
                break
        if(flag==False):
            break
    if(flag):
        if(ai_health>player_health):
            return 1
        elif(player_health>ai_health):
            return -1
        else:
            return 0
    return -100
def get_cell(mat,n,m,c):
    for i in range(0,n):
        for j in range(0,m):
            if(mat[i][j]==c):
                return (i,j)

mat_freq_p=np.zeros((n,m))
mat_freq_a=np.zeros((n,m))
def min_max(iteration,mat,turn,n,m,player_health,ai_health,ai_s,player_s,pbx,pby,abx,aby):
    print(mat)

    player_cell=get_cell(mat,n,m,'p')
    ai_cell = get_cell(mat, n, m, 'a')
    print(player_cell)
    print(ai_cell)
    print(player_health)
    print(ai_health)
    print(player_s)
    print(ai_s)
    available_cells=[]
    # print("block", pbx, pby)
    if(turn=='p'):
        available_cells=get_cells(mat,player_cell[0],player_cell[1],n,m,pbx,pby)
        pbx=player_cell[0]
        pby=player_cell[1]

    if (turn == 'a'):
        available_cells = get_cells(mat,ai_cell[0], ai_cell[1], n, m,abx,aby)
        abx=ai_cell[0]
        aby=ai_cell[1]
    temp=winner(player_health,ai_health,mat,n,m)
    if(temp!=-100):
        return temp
    mat2=np.copy(mat)
    for i in range(0,len(available_cells)):
        present_cell_x = available_cells[i][0]
        present_cell_y = available_cells[i][1]
        iteration+=1
        p_h = player_health
        a_h = ai_health
        p_s=player_s
        a_s=ai_s
        mat1=mat
        present_cell_content=mat[present_cell_x][present_cell_y]
        if(turn=='a'):
            # print(mat1)
            damage=0
            # print("itera_a:", iteration, mat_freq_a[present_cell_x][present_cell_y])
            if ((iteration - mat_freq_a[present_cell_x][present_cell_y])>=7 and mat_freq_a[present_cell_x][present_cell_y]!=0):
                return
            mat_freq_a[present_cell_x][present_cell_y] = iteration
            # print("itera_a:", iteration, mat_freq_a[present_cell_x][present_cell_y])
            if(mat1[present_cell_x][present_cell_y]=='w1'):
                if(p_s=='s1'):
                    damage=0
                elif p_s=='s2':
                    damage=60
                elif p_s=='s3':
                    damage=70
                else:
                    damage=100
                p_s='0'
            if (mat1[present_cell_x][present_cell_y] == 'w2'):
                if (p_s == 's1'):
                    damage = 260
                elif p_s == 's2':
                    damage = 0
                elif p_s == 's3':
                    damage = 200
                else:
                    damage = 300
                p_s='0'
            if (mat1[present_cell_x][present_cell_y] == 'w3'):
                if (p_s == 's1'):
                    damage = 650
                elif p_s == 's2':
                    damage = 600
                elif p_s == 's3':
                    damage = 0
                else:
                    damage = 700
                p_s = '0'
            p_h-=damage
            if (mat1[present_cell_x][present_cell_y] == 's1'):
                a_s='s1'
            if (mat1[present_cell_x][present_cell_y] == 's2'):
                a_s = 's2'
            if (mat1[present_cell_x][present_cell_y] == 's3'):
                a_s = 's3'
            mat1[present_cell_x][present_cell_y] = 'a'
            mat1[ai_cell[0]][ai_cell[1]] = '0'
            result=min_max(iteration,mat1,'p',n,m,p_h,a_h,a_s,p_s,pbx,pby,abx,aby)
        elif (turn == 'p'):
            player_cell = get_cell(mat, n, m, 'p')
            damage = 0
            # print("itera_p:", iteration, mat_freq_p[present_cell_x][present_cell_y])
            if ((iteration - mat_freq_p[present_cell_x][present_cell_y]) >= 7 and mat_freq_a[present_cell_x][present_cell_y]!=0):
                return
            mat_freq_p[present_cell_x][present_cell_y] = iteration
            # print("itera_p:", iteration, mat_freq_p[present_cell_x][present_cell_y])
            if (mat1[present_cell_x][present_cell_y] == 'w1'):
                if (a_s == 's1'):
                    damage = 0
                elif a_s == 's2':
                    damage = 60
                elif a_s == 's3':
                    damage = 70
                else:
                    damage = 100
                a_s = '0'
            if (mat1[present_cell_x][present_cell_y] == 'w2'):
                if (a_s == 's1'):
                    damage = 260
                elif a_s == 's2':
                    damage = 0
                elif a_s == 's3':
                    damage = 200
                else:
                    damage = 300
                a_s = '0'
            if (mat1[present_cell_x][present_cell_y] == 'w3'):
                if (a_s == 's1'):
                    damage = 650
                elif a_s == 's2':
                    damage = 600
                elif a_s == 's3':
                    damage = 0
                else:
                    damage = 700
                a_s = '0'
            a_h -= damage
            if (mat1[present_cell_x][present_cell_y] == 's1'):
                p_s='s1'
            if (mat1[present_cell_x][present_cell_y] == 's2'):
                p_s = 's2'
            if (mat1[present_cell_x][present_cell_y] == 's3'):
                p_s = 's3'
            mat1[present_cell_x][present_cell_y] = 'p'
            mat1[player_cell[0]][player_cell[1]] = '0'
            # print(present_cell_x,present_cell_y,player_cell)
            result = min_max(iteration,mat1, 'a', n, m, p_h, a_h, a_s, p_s,pbx,pby,abx,aby)
        # print("last",mat1)
        mat=np.copy(mat2)




min_max(iteration,mat,'a',n,m,1000,1000,'0','0',-1,-1,-1,-1)