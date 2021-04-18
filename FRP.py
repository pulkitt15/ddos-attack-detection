import itertools

class FRP_solver(object):
    def __init__(self, V, E, R, A, D, v):
        super(FRP_solver, self).__init__()
        self.V = V
        self.E = E
        self.R = R
        self.A = A
        self.D = D
        self.v = v


    def maximal_solution(self):
        S = []
        Es = []
        for a in self.D:
            f = self.Flow(a, self.v)
            #print("f is",f)
            prev = []
            for first, second in zip(f, f[1:]):
                #print((first,second))
                if (first,second) in self.A:
                    #print("Agent Edge is ",(first,second) )
                    if (first,second) not in S:
                        S.append((first,second))

                    if len(prev) >=1 :
                        Es.append((prev[0],(first,second)))
                        prev[0] = (first,second)
        return S,Es


    def Flow(self,u, v):
         f = [u]
         while f[-1] != v:
             if not self.R.get(f[-1]):
                 print("First Index not in R", f[-1])
             elif not self.R.get(f[-1]).get(v):
                 print("Second index not in R, indexes are", f[-1],v)
             else:
              f.append(self.R[f[-1]][v])
         return f