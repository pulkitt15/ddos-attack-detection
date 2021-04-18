class routing_table(object):
    """docstring for routing_table"""
    def __init__(self, G, is_grid=0):
        super(routing_table, self).__init__()
        self.V = G[0]
        self.E = G[1]
        self.is_grid = is_grid

    def create_table(self):
        #n = len(self.V)
        R = {}
#        count = 0
        for i in self.V:
            R[i] = {}
            for j in self.V:
                R[i][j] = -1
        for v in self.V:
            if self.is_grid:
                p = self.bfs(v)
            # else:
            #     p = dijistra(v)
            for i in self.V:
                if v ==i:
                    R[i][i] = i
                else:
                    if R[i][v] == -1:
                        R[i][v] = p[i]
                        path = self.path(v,i,p)
                        R[v][i] = path[1]
#                        if p[i] not in self.V:
#                            count+=1
        return R
    
    
    def dijkstra(self, v):
        INF = 1000000000
        visited = {}
        p = {}
        d = {}
        for i in self.V:
            visited[i] = False
            p[i] = i
            d[i] = INF
            
        d[v] = 0
        n = len(self.V)
        for _ in range(n):
            v = -1
            for i in self.V:
                if not visited[i] and (v==-1 or d[i]<d[v]):
                    v=i
            if d[v] == INF:
                break
            visited[v] = True
            for u in self.E[v]:
                if d[u]>d[v]+1:
                    d[u] = d[v]+1
                    p[u]=v
        return p
            
        
    def bfs(self, v):
        visited = {}
        p = {}
        for i in self.V:
            visited[i] = 0
            p[i] = i
        queue = []
        queue.append(v)

        while queue:
          s = queue.pop(0)
          for u in self.E[s]:
              if visited[u] ==0 :
                  visited[u] = 1
                  p[u] = s
                  queue.append(u)
        return p
    
    def path(self,s,d,p):
        path = [d]
        while path[-1] != s:
            path.append(p[path[-1]])
        path.reverse()
        return path