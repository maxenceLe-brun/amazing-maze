import random
import time

def backtrack(obj, must:int = 0):
    """
    Parameters
    ----------
    obj  : object created with the class maze in the 
           "generate.py" file
    must : int
           if upper than 0, will start to print every move of the
           solving system
    Description
    -----------
    L : for the list that contain the walls in the actual case in (x,y)
    l : for all the cases that our player was and will be
    lway : the final path for the player to directly go from the entrance
           to the exit without any wrong turn
    """
    x = 0
    y = 0
    L = []
    l = []
    lway = []
    l.append((x,y))
    lway.append((x,y))
    while (x,y) != (obj.n-1,)*2:
        """
        Lbis is for the directions that were already checked, so it doesn't
             have to check the same direction twice
        "X" and "Y" are here to check if the player has at least moved
        """
        L = [obj.map[y][x].u,obj.map[y][x].d,obj.map[y][x].l,obj.map[y][x].r]
        Lbis = []
        X = x
        Y = y
        
        for _ in range(len(L)):# "_" still stand for nothing to use
            a = random.randrange(4)
            while a in Lbis:# if the number is in Lbis, reselect!
                a = random.randrange(4)
            if L[a] == 0:# check if it can goes by a broken wall
                if a == 0 and y > 0 and (x,y-1) not in l:
                    #check if it can go up
                    y -= 1
                    l.append((x,y))
                    lway.append((x,y))
                    break
                elif a == 1 and y < obj.n-1 and (x,y+1) not in l:
                    #check if it can go down
                    y += 1
                    l.append((x,y))
                    lway.append((x,y))
                    break
                elif a == 2 and x > 0 and (x-1,y) not in l:
                    #check if it can go left
                    x -= 1
                    l.append((x,y))
                    lway.append((x,y))
                    break
                elif a == 3 and x < obj.n-1 and (x+1,y) not in l:
                    #check if it can go right
                    x += 1
                    l.append((x,y))
                    lway.append((x,y))
                    break
                else:
                    #else put it in the banned list
                    Lbis.append(a)
            else:
                #else put it in the banned list
                Lbis.append(a)
        if (x,y) == (X,Y):
            #it's rewind time! go back and check again!
            print("rewind")
            lway.pop(-1)
            x = lway[~0][0]
            y = lway[~0][~0]
        if must > 0:
            #if you print or not!
            print(obj.show(x,y))
            time.sleep(0.3)
    return (lway,l)

def aStar(obj, must:int = 0):
    """
    Parameters
    ----------
    obj  : object created with the class maze in the 
           "generate.py" file
    must : int
           if upper than 0, will start to print every move of the
           solving system
    Description
    -----------
    save vanished, 100% my bad
    """
    pass
