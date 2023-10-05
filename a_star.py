import heapq

import numpy as np

def array_reverse(input):
    temp=[]

    for i in range(len(input)-1,-1,-1):
        temp.append(input[i])
    return temp

def path_lenth(paths,key,p_w_pt):

    x=paths.get(key)
    if(x!=None):
        p_w_pt[key]=len(x)
    else:
        p_w_pt[key] = 1000
    return p_w_pt
def get_neighbours(x,y,n,m):
    neighbours=[]
    for i in range(0,len(dir)):
        temp=dir[i]
        if((x+temp[0]>=0 and x+temp[0]<n) and (y+temp[1]>=0 and y+temp[1]<m)):
            neighbours.append((x+temp[0],y+temp[1]))
    return neighbours

def find_player(mat):
    for i in range(0,mat.shape[0]):
        for j in range(0,mat.shape[1]):
            if(mat[i][j]=='p'):
                return (i,j)
def find_ai(mat):
    for i in range(0, mat.shape[0]):
        for j in range(0, mat.shape[1]):
            if (mat[i][j] == 'a'):
                return (i, j)
def find_w1(mat):
    points=[(-1,-1),(-1,-1)]
    k=0
    for i in range(0, mat.shape[0]):
        for j in range(0, mat.shape[1]):
            if (mat[i][j] == 'w1'):
                points[k]=(i,j)
                k+=1
    return points

def find_w2(mat):
    points = [(-1, -1), (-1, -1)]
    k = 0
    for i in range(0, mat.shape[0]):
        for j in range(0, mat.shape[1]):
            if (mat[i][j] == 'w2'):
                points[k] = (i, j)
                k += 1
    return points
def find_w3(mat):
    points = [(-1, -1), (-1, -1)]
    k = 0
    for i in range(0, mat.shape[0]):
        for j in range(0, mat.shape[1]):
            if (mat[i][j] == 'w3'):
                points[k] = (i, j)
                k += 1
    return points

def find_s1(mat):
    for i in range(0, mat.shape[0]):
        for j in range(0, mat.shape[1]):
            if (mat[i][j] == 's1'):
                return (i, j)
    return (-1,-1)
def find_s2(mat):
    for i in range(0, mat.shape[0]):
        for j in range(0, mat.shape[1]):
            if (mat[i][j] == 's2'):
                return (i, j)
    return (-1,-1)
def find_s3(mat):
    for i in range(0, mat.shape[0]):
        for j in range(0, mat.shape[1]):
            if (mat[i][j] == 's3'):
                return (i, j)
    return (-1,-1)
def heuristic(src, des):
    return np.sqrt((des[0] - src[0]) ** 2 + (des[1] - src[1]) ** 2)
def a_star(mat,src,des,n,m):
    if(des==(-1,-1)):
        return -1000
    close_set=set()
    parent={src:src}
    gscore={src:0}
    fscore={src:heuristic(src,des)}
    oheap=[]
    heapq.heappush(oheap,(fscore[src],src))

    while(oheap):
        current=heapq.heappop(oheap)[1]
        if current==des:
            path=[]
            temp=des
            while(temp!=parent[temp]):
                path.append(temp)
                temp=parent[temp]
            return array_reverse(path)
        close_set.add(current)
        neighbours=get_neighbours(current[0],current[1],n,m)
        for i,j in neighbours:
            neighbour=(i,j)
            g_temp=gscore[current]+heuristic(current,(i,j))
            if(neighbour in close_set) and (g_temp>=gscore.get(neighbour,0)):
                continue
            if(g_temp<gscore.get(neighbour,0) or (neighbour not in [i[1] for i in oheap])):
                parent[neighbour]=current
                gscore[neighbour]=g_temp
                fscore[neighbour]=g_temp+heuristic(neighbour,des)
                heapq.heappush(oheap,(fscore[neighbour],neighbour))

def min_key(pt,keys):
    len=1000
    k=''
    for key in keys:
       if(pt[key]<=len):
            k=key
            len=pt[key]
    return k



def ai(mat,player_sheild):
    mat=np.array(mat)
    # mat=np.flip(mat)
    # print(mat)
    n=mat.shape[0]
    m=mat.shape[1]
    ai_coordinates=find_ai(mat)
    player_coordinates=find_player(mat)
    # print(ai_coordinates,player_coordinates)
    w1_cordinates=find_w1(mat)
    w11_cordinates=w1_cordinates[0]
    w12_cordinates=w1_cordinates[1]
    w2_cordinates = find_w2(mat)
    w21_cordinates = w2_cordinates[0]
    w22_cordinates = w2_cordinates[1]
    w3_cordinates = find_w3(mat)
    w31_cordinates = w3_cordinates[0]
    w32_cordinates = w3_cordinates[1]
    s1_cordinates=find_s1(mat)
    s2_cordinates=find_s2(mat)
    s3_cordinates=find_s3(mat)


    player_w_paths={}
    player_s_paths={}
    if(a_star(mat,player_coordinates,w11_cordinates,n,m)!=-1000):
        player_w_paths['w11']=a_star(mat,player_coordinates,w11_cordinates,n,m)
    if (a_star(mat, player_coordinates, w12_cordinates, n, m) != -1000):
        player_w_paths['w12'] = a_star(mat, player_coordinates, w12_cordinates, n, m)
    if (a_star(mat, player_coordinates, w21_cordinates, n, m) != -1000):
        player_w_paths['w21'] = a_star(mat, player_coordinates, w21_cordinates, n, m)
    if (a_star(mat, player_coordinates, w22_cordinates, n, m) != -1000):
        player_w_paths['w22'] = a_star(mat, player_coordinates, w22_cordinates, n, m)
    if (a_star(mat, player_coordinates, w31_cordinates, n, m) != -1000):
        player_w_paths['w31'] = a_star(mat, player_coordinates, w31_cordinates, n, m)
    if (a_star(mat, player_coordinates, w32_cordinates, n, m) != -1000):
        player_w_paths['w32'] = a_star(mat, player_coordinates, w32_cordinates, n, m)
    print(player_w_paths)
    if (a_star(mat, player_coordinates, s1_cordinates, n, m) != -1000):
        player_s_paths['s1'] = a_star(mat, player_coordinates, s1_cordinates, n, m)
    if (a_star(mat, player_coordinates, s2_cordinates, n, m) != -1000):
        player_s_paths['s2'] = a_star(mat, player_coordinates, s2_cordinates, n, m)
    if (a_star(mat, player_coordinates, s3_cordinates, n, m) != -1000):
        player_s_paths['s3'] = a_star(mat, player_coordinates, s3_cordinates, n, m)
    print(player_s_paths)

    ai_w_paths = {}
    ai_s_paths = {}
    if (a_star(mat, ai_coordinates, w11_cordinates, n, m) != -1000):
        ai_w_paths['w11'] = a_star(mat, ai_coordinates, w11_cordinates, n, m)
    if (a_star(mat, ai_coordinates, w12_cordinates, n, m) != -1000):
        ai_w_paths['w12'] = a_star(mat, ai_coordinates, w12_cordinates, n, m)
    if (a_star(mat, ai_coordinates, w21_cordinates, n, m) != -1000):
        ai_w_paths['w21'] = a_star(mat, ai_coordinates, w21_cordinates, n, m)
    if (a_star(mat, ai_coordinates, w22_cordinates, n, m) != -1000):
        ai_w_paths['w22'] = a_star(mat, ai_coordinates, w22_cordinates, n, m)
    if (a_star(mat, ai_coordinates, w31_cordinates, n, m) != -1000):
        ai_w_paths['w31'] = a_star(mat, ai_coordinates, w31_cordinates, n, m)
    if (a_star(mat, ai_coordinates, w32_cordinates, n, m) != -1000):
       ai_w_paths['w32'] = a_star(mat, ai_coordinates, w32_cordinates, n, m)
    # print(ai_w_paths)
    if (a_star(mat, ai_coordinates, s1_cordinates, n, m) != -1000):
        ai_s_paths['s1'] = a_star(mat, ai_coordinates, s1_cordinates, n, m)
    if (a_star(mat, ai_coordinates, s2_cordinates, n, m) != -1000):
        ai_s_paths['s2'] = a_star(mat, ai_coordinates, s2_cordinates, n, m)
    if (a_star(mat, ai_coordinates, s3_cordinates, n, m) != -1000):
        ai_s_paths['s3'] = a_star(mat, ai_coordinates, s3_cordinates, n, m)
    print(ai_s_paths)

    p_w_pt={}
    p_w_pt=path_lenth(player_w_paths,'w11',p_w_pt)
    p_w_pt= path_lenth(player_w_paths, 'w12',p_w_pt)
    p_w_pt= path_lenth(player_w_paths, 'w21',p_w_pt)
    p_w_pt= path_lenth(player_w_paths, 'w22',p_w_pt)
    p_w_pt= path_lenth(player_w_paths, 'w31',p_w_pt)
    p_w_pt= path_lenth(player_w_paths, 'w32',p_w_pt)
    print(p_w_pt)

    p_s_pt = {}
    p_s_pt = path_lenth(player_s_paths, 's1', p_s_pt)
    p_s_pt = path_lenth(player_s_paths, 's2', p_s_pt)
    p_s_pt = path_lenth(player_s_paths, 's3', p_s_pt)
    print(p_s_pt)

    ai_w_pt = {}
    ai_w_pt = path_lenth(ai_w_paths, 'w11', ai_w_pt)
    ai_w_pt = path_lenth(ai_w_paths, 'w12', ai_w_pt)
    ai_w_pt = path_lenth(ai_w_paths, 'w21', ai_w_pt)
    ai_w_pt = path_lenth(ai_w_paths, 'w22', ai_w_pt)
    ai_w_pt = path_lenth(ai_w_paths, 'w31', ai_w_pt)
    ai_w_pt = path_lenth(ai_w_paths, 'w32', ai_w_pt)
    print(ai_w_pt)

    ai_s_pt = {}
    ai_s_pt = path_lenth(ai_s_paths, 's1', ai_s_pt)
    ai_s_pt = path_lenth(ai_s_paths, 's2', ai_s_pt)
    ai_s_pt = path_lenth(ai_s_paths, 's3', ai_s_pt)
    print(ai_s_pt)

    player_min_w=min_key(p_w_pt,[key for key in p_w_pt])
    print(player_min_w)
    player_min_s = min_key(p_s_pt,[key for key in p_s_pt])
    print(player_min_s)
    ai_min_w = min_key(ai_w_pt,[key for key in ai_w_pt])
    print(ai_min_w)
    ai_min_s = min_key(ai_s_pt,[key for key in ai_s_pt])
    print(ai_min_s)

    result=(0,0)
    if(p_w_pt[player_min_w]<=p_s_pt[player_min_s]):

        if(ai_s_pt[ai_min_s]<=p_w_pt[player_min_w]):

            if(player_min_w=='w11' or player_min_w=='w12'):
                if(ai_s_pt['s1']<=p_w_pt[player_min_w]):
                    result=ai_s_paths['s1'][0]
                    # print(result)
                elif (ai_s_pt['s3']<=p_w_pt[player_min_w]):
                    result=ai_s_paths['s3'][0]
                    # print(result)
                elif (ai_s_pt['s2']<=p_w_pt[player_min_w]):
                    result=ai_s_paths['s2'][0]
                    # print(result)
            if (player_min_w == 'w21' or player_min_w == 'w22'):
                if (ai_s_pt['s2'] <= p_w_pt[player_min_w]):
                    result = ai_s_paths['s2'][0]
                    # print(result)
                elif (ai_s_pt['s3'] <= p_w_pt[player_min_w]):
                    result = ai_s_paths['s3'][0]
                    # print(result)
                elif (ai_s_pt['s1'] <= p_w_pt[player_min_w]):
                    result = ai_s_paths['s1'][0]
                    # print(result)
            if (player_min_w == 'w31' or player_min_w == 'w32'):
                if (ai_s_pt['s3'] <= p_w_pt[player_min_w]):
                    result = ai_s_paths['s3'][0]
                    # print(result)
                elif (ai_s_pt['s2'] <= p_w_pt[player_min_w]) :
                    result = ai_s_paths['s2'][0]
                    # print(result)
                elif (ai_s_pt['s1'] <= p_w_pt[player_min_w]):
                    result = ai_s_paths['s1'][0]
                    # print(result)

        elif (ai_w_pt[ai_min_w]<=p_w_pt[player_min_w]):
            if((ai_w_pt['w31']<=p_w_pt[player_min_w] or ai_w_pt['w32']<=p_w_pt[player_min_w]) and player_sheild!='s3'):
                temp=min(ai_w_pt['w31'],ai_w_pt['w32'])
                if(ai_w_pt['w31']==temp):
                    result=ai_w_paths['w31'][0]
                else:
                    result = ai_w_paths['w32'][0]
                # print(result)
            elif((ai_w_pt['w21']<=p_w_pt[player_min_w] or ai_w_pt['w22']<=p_w_pt[player_min_w]) and player_sheild!='s2'):
                temp = min(ai_w_pt['w21'], ai_w_pt['w22'])
                if (ai_w_pt['w21'] == temp):
                    result = ai_w_paths['w21'][0]
                else:
                    result = ai_w_paths['w22'][0]
                print(result)
            elif ((ai_w_pt['w11'] <= p_w_pt[player_min_w] or ai_w_pt['w12'] <= p_w_pt[player_min_w]) and player_sheild!='s1'):
                temp = min(ai_w_pt['w11'], ai_w_pt['w12'])
                if (ai_w_pt['w11'] == temp):
                    result = ai_w_paths['w11'][0]
                else:
                    result = ai_w_paths['w12'][0]
                print(result)
            else:
                if(player_sheild=='s1'):
                    key=min_key(ai_w_pt,['w21','w22','w31','w32'])
                    result=ai_w_paths[key][0]
                    print(result)
                elif(player_sheild=='s2'):
                    key = min_key(ai_w_pt, ['w11', 'w12', 'w31', 'w32'])
                    result = ai_w_paths[key][0]
                    print(result)
                elif(player_sheild=='s3'):
                    key = min_key(ai_w_pt, ['w21', 'w22', 'w11', 'w12'])
                    result = ai_w_paths[key][0]
                    print(ai_w_paths[key])
                    print(result)
        else:
            result=ai_w_paths[ai_min_w][0]
            print(result)

    else:

        if(ai_w_pt[ai_min_w]<=p_s_pt[player_min_s]):
            if((ai_w_pt['w31']<=p_s_pt[player_min_s] or ai_w_pt['w32']<=p_s_pt[player_min_s]) and player_sheild!='s3'):
                temp = min(ai_w_pt['w31'], ai_w_pt['w32'])
                if (ai_w_pt['w31'] == temp):
                    result = ai_w_paths['w31'][0]
                else:
                    result = ai_w_paths['w32'][0]
                print(result)
            elif ((ai_w_pt['w21'] <= p_s_pt[player_min_s] or ai_w_pt['w22'] <= p_s_pt[player_min_s]) and player_sheild!='s2'):
                temp = min(ai_w_pt['w21'], ai_w_pt['w22'])
                if (ai_w_pt['w21'] == temp):
                    result = ai_w_paths['w21'][0]
                else:
                    result = ai_w_paths['w22'][0]
                print(result)
            elif ((ai_w_pt['w11'] <= p_s_pt[player_min_s] or ai_w_pt['w12'] <= p_s_pt[player_min_s]) and player_sheild!='s1'):
                temp = min(ai_w_pt['w11'], ai_w_pt['w12'])
                if (ai_w_pt['w11'] == temp):
                    result = ai_w_paths['w11'][0]
                else:
                    result = ai_w_paths['w12'][0]
                print(result)
            else:
                if (player_sheild == 's1'):
                    key = min_key(ai_w_pt, ['w21', 'w22', 'w31', 'w32'])
                    result = ai_w_paths[key][0]
                    print(result)
                elif (player_sheild == 's2'):
                    key = min_key(ai_w_pt, ['w11', 'w12', 'w31', 'w32'])
                    result = ai_w_paths[key][0]
                    print(result)
                elif (player_sheild == 's3'):
                    key = min_key(ai_w_pt, ['w21', 'w22', 'w11', 'w12'])
                    result = ai_w_paths[key][0]
                    print(ai_w_paths[key])
                    print(result)
        elif(ai_w_pt[ai_min_w]>p_s_pt[player_min_s]):
            if(player_min_s=='s1'):
                key = min_key(ai_w_pt, ['w21', 'w22', 'w31', 'w32'])
                result = ai_w_paths[key][0]
                print(result)
            elif (player_min_s == 's2'):
                key = min_key(ai_w_pt, ['w11', 'w12', 'w31', 'w32'])
                result = ai_w_paths[key][0]
                print(result)
            elif (player_min_s == 's3'):
                key = min_key(ai_w_pt, ['w21', 'w22', 'w11', 'w12'])
                result = ai_w_paths[key][0]
                print(ai_w_paths[key])
                print(result)
    if(result==(0,0)):
        print("here")
    return result


mat=np.array([['0', '0', '0', '0', 'w1', '0', '0', '0', '0', '0', '0', 'p'], ['0', '0', '0', '0', '0', '0', 's3', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', 's2', '0', '0', '0', 'w3'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', 'w2', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['w1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', 'w3', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', 'w2', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['a', '0', '0', 's1', '0', '0', '0', '0', '0', '0', '0', '0']])
dir=[(1,0),(-1,0),(0,1),(0,-1)]
player_sehild=''
ai(mat,player_sehild)