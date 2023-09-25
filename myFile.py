import time
import random
class case:
    def __init__(self, x:int, y:int):
        """
        Parameters
        ----------
        x : int
            the longitute coordinate
        y : int
            the latitude coordinate
        
        Description
        -----------
        u : upper wall
        d : lower wall
        l : left wall
        r : right wall
        already : if the case was used or not
        w : used in the Kruskal's algorithm
        """
        self.x       = x
        self.y       = y
        self.u       = 1
        self.d       = 1
        self.l       = 1
        self.r       = 1
        self.already = 1
        self.w       = -1
    def up(self):
        self.u = 0
    def down(self):
        self.d = 0
    def left(self):
        self.l = 0
    def right(self):
        self.r = 0

class maze:
    """
    functions
    ---------
    create : form the labyrinth of a 'n' size with a backtracking algorithm
    show   : print with a little style the labyrinth
    solve  : solve the labyrinth created with a randomized choice mixed with
             a backtracking algorithm
    """
    def __init__(self, n:int):
        """
        Parameters
        ----------
        n : int
            The size of your map
        
        Description
        -----------
        the ~0 is just the reversed bits of 0 : -1
        self.map[~0][~0] == self.map[-1][-1]
        """
        self.n = n
        self.map = [[case(x,y) for x in range(n)]for y in range(n)]
        self.map[0][0].left()
        self.map[~0][~0].right()
    def create(self):
        """
        Description
        -----------
        This function is an iterative version of the recursive backtracking
        algorithm, i tried many times with the recursive version but it crashed
        everytime.
        
        So, this function will chose a random direction on each case, and if it
        is stuck, it will use the list 'L' to return to the last case
        """
        L = []
        N = 1
        x = 0
        y = 0
        L.append((x,y))
        chose = [0,1,2,3] #0 for up, 1 for down, 2 for left and 3 for right
        while N < self.n**2:
            #to have a maze with a size of 5,we have 5*5 cases, so 5**2
            r = random.choices(chose) #i used "choices" except of "choice" :/
            r = r[0]
            if r == 0 and y > 0 and self.map[y-1][x].already:
                #check if it can goes up
                self.map[y][x].up()
                self.map[y][x].already = 0
                self.map[y-1][x].down()
                y -= 1
                N += 1
                L.append((x,y))
                chose = [0,1,2,3] #reset the choice
            elif r == 1 and y < self.n - 1 and self.map[y+1][x].already:
                #check if it can goes down
                self.map[y][x].down()
                self.map[y][x].already = 0
                self.map[y+1][x].up()
                y += 1
                N += 1
                L.append((x,y))
                chose = [0,1,2,3] #reset the choice
            elif r == 2 and x > 0 and self.map[y][x-1].already:
                #check if it can goes left
                self.map[y][x].left()
                self.map[y][x].already = 0
                self.map[y][x-1].right()
                x -= 1
                N += 1
                L.append((x,y))
                chose = [0,1,2,3] #reset the choice
            elif r == 3 and x < self.n -1 and self.map[y][x+1].already:
                #check if it can goes right
                self.map[y][x].right()
                self.map[y][x].already = 0
                self.map[y][x+1].left()
                x += 1
                N += 1
                L.append((x,y))
                chose = [0,1,2,3] #reset the choice
            else:
                if chose:
                    for a in range(len(chose)):
                        if chose[a] == r:
                            chose.pop(a)
                            break
                    if len(chose) == 0:
                        #then, no more possibilities and go back
                        chose = [0,1,2,3] #reset the choice
                        L.pop(-1)
                        self.map[y][x].already = 0 #mark the case as used
                        x = L[-1][0]
                        y = L[-1][1]
                else:
                    chose = [0,1,2,3] #reset the choice
                    L.pop(-1)
                    x,y = L[-1]
        print('ended with ' + str(N) + " over " + str(self.n)) #light checkup
        print(self.show())
    def show(self, X:int = -1, Y:int = -1):
        """
        Parameters
        ----------
        X : int
            position used in the solve function to show where we are
        Y : int
            position used in the solve function to show where we are
        Description
        -----------
        To upgrade, bcs its a little too scratchy rn
        """
        ud   = "║   "
        ul   = "╝   "
        ur   = "╚═══"
        dl   = "╗   "
        dr   = "╔═══"
        lr   = "════"
        udlr = "╬═══"
        udl  = "╣   "
        udr  = "╠═══"
        ulr  = "╩═══"
        dlr  = "╦═══"
        no   = "   "
        
        hand = [] # "hand" because it will be used like the main variable
        hand.append(dr + (self.n-1)*dlr + dl)
        for _ in range(self.n-1): #i use '_' as nothing to use in it
            idk =  ud * (self.n+1) #"idk" is because i had no name in my mind
            hand.append(idk)
            idk = udr + udlr * (self.n-1) + udl
            hand.append(idk)
        hand.append(ud * (self.n+1))
        hand.append(ur + ulr * (self.n-1) + ul)
        Map = []
        for a in hand:
            Map.append([])
            for b in a:
                Map[-1].append(b)
        hand = Map
        
        #sorry for this line down ahead, i fully compacted it :/
        #the following script is to visualize the broken walls
        L = [[(self.map[y][x].u,self.map[y][x].d,self.map[y][x].l,self.map[y][x].r) for x in range(self.n)] for y in range(self.n)]
        for y in range(self.n):
            for x in range(self.n):
                if (X,Y) != (-1,-1): #to print the position
                    hand[1+Y*2][2+X*4] = "P"
                if L[y][x][0] == 0:
                    hand[y*2][2+x*4] = " "
                if L[y][x][1] == 0:
                    hand[2+y*2][2+x*4] = " "
                if L[y][x][2] == 0:
                    hand[1+y*2][x*4] = " "
                if L[y][x][3] == 0:
                    hand[1+y*2][4+x*4] = " "
        
        #then, put it on string and returns it!
        string = ""
        for a in hand:
            for b in a:
                string += b
            string += "\n"
        return string
    
    
    def solve(self, must:int = 0):
        """
        Parameters
        ----------
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
        while (x,y) != (self.n-1,)*2:
            """
            Lbis is for the directions that were already checked, so it doesn't
                 have to check the same direction twice
            "X" and "Y" are here to check if the player has at least moved
            """
            L = [self.map[y][x].u,self.map[y][x].d,self.map[y][x].l,self.map[y][x].r]
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
                    elif a == 1 and y < self.n-1 and (x,y+1) not in l:
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
                    elif a == 3 and x < self.n-1 and (x+1,y) not in l:
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
                print(self.show(x,y))
                time.sleep(0.3)
        return (lway,l)
    

class maze2:
    """
    functions
    ---------
    create : form the labyrinth of a 'n' size with a kruskal algorithm
    show   : print with a little style the labyrinth
    solve  : solve the labyrinth created with a randomized choice mixed with
             a kruskal algorithm (not implemented yet)
    """
    def __init__(self,n):
        self.n = n
        self.map = [[case(x,y) for x in range(n)]for y in range(n)]
        for a in range(n):
            for b in range(n):
                self.map[a][b].w = a*6+b
        self.map[0][0].left()
        self.map[~0][~0].right()
    def create(self):
        L = []
        N = 1
        x = random.randrange(0,self.n)
        y = random.randrange(0,self.n)
        chose = [0,1,2,3]
        while N < self.n**2:
            r = random.choice(chose)
            
            if r == 0 and y > 0 and self.map[y][x].already:
                self.map[y][x].up()
                self.map[y][x].already = 0
                self.map[y-1][x].down()
                
                N += 1
                L.append((x,y))
                
                
            if r == 1 and y < self.n-1 and self.map[y][x].already:
                pass
            
            if r == 2 and x > 0 and self.map[y][x].already:
                pass
            
            if r == 3 and x < self.n-1 and self.map[y][x].already:
                pass
            
            
        
    def show(self, X = -1, Y = -1):
        ud   = "║   "
        ul   = "╝   "
        ur   = "╚═══"
        dl   = "╗   "
        dr   = "╔═══"
        lr   = "════"
        udlr = "╬═══"
        udl  = "╣   "
        udr  = "╠═══"
        ulr  = "╩═══"
        dlr  = "╦═══"
        no   = "   "
        
        hand = []
        hand.append(dr + (self.n-1)*dlr + dl)
        for _ in range(self.n-1):
            idk =  ud * (self.n+1)
            hand.append(idk)
            idk = udr + udlr * (self.n-1) + udl
            hand.append(idk)
        hand.append(ud * (self.n+1))
        hand.append(ur + ulr * (self.n-1) + ul)
        Map = []
        for a in hand:
            Map.append([])
            for b in a:
                Map[-1].append(b)
        hand = Map
        L = [[(self.map[y][x].u,self.map[y][x].d,self.map[y][x].l,self.map[y][x].r) for x in range(self.n)]for y in range(self.n)]
        for y in range(self.n):
            for x in range(self.n):
                if (X,Y) != (-1,-1):
                    hand[1+Y*2][2+X*4] = "P"
                if L[y][x][0] == 0:
                    hand[y*2][2+x*4] = " "
                if L[y][x][1] == 0:
                    hand[2+y*2][2+x*4] = " "
                if L[y][x][2] == 0:
                    hand[1+y*2][x*4] = " "
                if L[y][x][3] == 0:
                    hand[1+y*2][4+x*4] = " "
        string = ""
        for a in hand:
            for b in a:
                string += b
            string += "\n"
        return string
