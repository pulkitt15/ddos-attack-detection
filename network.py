import math
from routing import routing_table
from random import sample, choice
from slant import ALP_solver
from FRP import FRP_solver
class network(object):
    """ Remove return value in attacker & victim"""
    def __init__(self, V_size, D_size, k, n, t):
        super(grid, self).__init__()
        self.n = n
        self.k = k
        self.V_size = V_size
        self.D_size = D_size
        self.V = []
        self.D = []
        self.E = {}
        self.R = []
        self.A = []
        self.victims = []
        self.G = (self.V, self.E)
        self.s = {}
        self.SS = []
        self.threshold = t

    def create_grid(self):
        x = int(math.sqrt(self.V_size))
        for i in range(x):
            for j in range(x):
                self.V.append((i,j))
                t = []
                if i>0:
                    t.append((i-1,j))
                if j>0:
                    t.append((i,j-1))
                if i+1<=x-1:
                    t.append((i+1,j))
                if j+1<=x-1:
                    t.append((i,j+1))
                self.E[(i,j)] = t

        r = routing_table(self.G,1)
        self.R = r.create_table()

    def add_agents(self):
        i,j = self.k-1,0
        x = int(math.sqrt(self.V_size))

        while j<x:
            if i+1>=x:
                i=i-x
                j += 1
            self.A.append(((i,j),(i+1,j)))
            i+=x

        i,j = self.k-1,0
        x = int(math.sqrt(self.V_size))

        while j<x:
            if i+1>=x:
                i=i-x
                j += 1
            self.A.append(((j,i),(j,i+1)))
            i+=x

    def select_attackers(self):
        self.D = sample(self.V, self.D_size)
        print("The attacker nodes are: ", self.D)
        return self.D[0]
        
    def select_victims(self, n = None):
        if n:
            self.n = n
        t = [i for i in self.V if i not in self.D]
        for i in range(self.n):
            self.victims.append(choice(t))
#        print("The victim nodes are: ", self.victims)
        return self.victims[-1]

    def get_suspicion_map(self):
        P = []
        L = []
        for i in self.victims:
            P.append((self.A,self.D,i))
            f = FRP_solver(self.V, self.E, self.R, self.A,self.D,i)
            L.append(f.maximal_solution())

        a = ALP_solver(self.V, self.E, self.R, P, L)
        self.s = a.SLANT()
#        print(self.s)
        for i in self.V:
            if self.s[i] >= self.threshold:
                self.SS.append(self.s[i])
        return self.s
    
    def FPR(self):
        t = [i for i in self.V if i not in self.D]
        num,den = 0,0
        for i in t:
            if self.s[i] >= self.threshold:
                num+=1
        for i in self.V:
            if self.s[i] >= self.threshold:
                den+=1
        if den == 0:
            den = 0.000001
        return num/den
    
    def ss_len(self):
        den = 0
        for i in self.V:
            if self.s[i] >= self.threshold:
                den+=1
        return den

    def FNR(self):
        num = 0
        for i in self.D:
            if self.s[i] < self.threshold:
                num+=1
        return num/self.D_size
    
    def initiate(self):
        self.create_grid()
        self.add_agents()
        self.select_attackers()
        self.select_victims()
        
    def run(self):
        s = self.get_suspicion_map()
        f1 =self.FPR()
        f2= self.FNR()
        print("Suspicion set size is",self.ss_len() )
        print("FPR score is",f1)
        char = input("Do you want to print whole suspicion map(Y/N)? ")
        if char=='Y' or char=='y':
            print("Suspicion map:\n",s)
        print("FNR score is",f2)

            
        
        
    



    






        