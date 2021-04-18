class ALP_solver(object):
    def __init__(self, V, E, R, P, L):
        super(ALP_solver, self).__init__()
        self.V = V
        self.E = E
        self.R = R
        self.L = L
        self.P = P


    def SLANT(self):
        s =  {}
        for i in self.V:
            s[i] = 0
        n = len(self.P)
        for i in range(n):
            S = self.L[i][0]  #S is set of agents in maximal solution of the FRP
            #print(S)
            for u in self.V:
                del_u = 0
                for a in S:
                    del_u = del_u +self.sigma(u, self.Cone(a, self.P[i][2]), S)
                s[u] =  s[u]+del_u/n 
        return s

    def sigma(self,u, C, S):
        if u in C:
            return 1/(len(S))
        return 0

    def Cone(self,a, v):
        c = []
        for u in self.V:
            if a in self.Flow(u,v):
                c.append(u)
        return c


    def Flow(self,u, v):
        f = [u]
        while f[-1] != v:
            f.append(self.R[f[-1]][v])
        #print("==========  ",u,v,"  ==============")
        #print(f)
        #print("=================")
        t = [(f[i],f[i+1]) for i in range(len(f)-1) ]
        #print(t)
        #print("=================")
        return t
            





    