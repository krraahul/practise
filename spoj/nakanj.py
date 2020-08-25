class Qnode:
    def __init__(self,data):
        self.prev = None
        self.next =None
        self.data = data

class Que:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self,data):
        node = Qnode(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            
    def rem(self):
        data = None
        if self.tail != None and self.tail.prev == None:
            data = self.tail.data
            self.head = None
            self.tail = None
        elif self.tail != None:
            data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        return data
        
    def isEmpty(self):
        return self.head == None and self.tail == None


aton = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7
}

def initgraph(r,c):
    graph = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(0)
        graph.append(row)
    return graph
 
 
rmax, cmax = 8,8
rmoves = [1,-1,2,-2]
cmoves = [1,-1,2,-2]


def  findnextnodes(graph,rq,cq,r,c,dr,dc,nextlayer):
  
    for i in range(len(rmoves)):
        for j in range(len(cmoves)):
           
            if abs(rmoves[i]) == abs(cmoves[j]):
                continue
           
            nr = r + rmoves[i]
            nc = c + cmoves[j]
         
            if nr >= rmax or nr < 0 or nc >= cmax or nc < 0:
                continue
            if nr == dr and nc == dc:
              
                return (True, nextlayer)
            if graph[nr][nc] == 1:
                continue
            graph[nr][nc] = 1
            nextlayer = nextlayer + 1
           
            rq.add(nr)
            cq.add(nc)
    return (False, nextlayer)

def evaluateBoard(graph, sr,sc,dr,dc):
    rq = Que()
    cq = Que()
    r = sr
    c = sc
    rq.add(r)
    cq.add(c)
    if sr == dr and sc == dc:
        return 0
    currentlayer = 1
    nextlayer = 0
    step = 1
    while not rq.isEmpty():
        r = rq.rem()
        c = cq.rem()
      
        bfound, nextlayer =  findnextnodes(graph,rq,cq,r,c,dr,dc,nextlayer)
        
        if bfound:
            return step
        else:
            currentlayer = currentlayer -1
            if currentlayer == 0:
                currentlayer = nextlayer
                nextlayer = 0
                step = step + 1
        graph[r][c] = 1
    return -1
    
def readinput():
    t = int(input())
    for i in range(t):
        graph = initgraph(rmax,cmax)
        src, dest = input().split()
        sc,sr = list(src)
        dc,dr = list(dest)
        sc = aton[sc]
        dc = aton[dc]
        sr = int(sr) -1
        dr = int(dr) - 1
        
        res = evaluateBoard(graph, sr, sc, dr, dc)
        if res != -1:
            print(res)
        #print(graph)


readinput()