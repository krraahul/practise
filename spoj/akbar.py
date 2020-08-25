# class QueueNode:
#     def __init__(self, data):
#         self.prev = None
#         self.next = None
#         self.data = data
        
        
# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def enqueue(self, data):
#         newNode = QueueNode(data)
#         if self.tail == None:
#             self.head = newNode
#             self.tail = newNode
#         else:
#             newNode.prev = self.tail
#             self.tail.next = newNode
#             self.tail = newNode
    
    
#     def dequeue(self):
#         data = None
#         if self.head == None:
#             return data
#         elif self.head.next == None:
#             data = self.head.data
#             self.head = None
#             self.tail = None
#         else:
#             data = self.head.data
#             self.head = self.head.next
#         return data
        
        
#     def isEmpty(self):
#         return self.head == None and self.tail == None
        
 
 
# class GraphNode:
#     def __init__(self, name):
#         self.name = name
#         self.visited = False
#         self.visitedBy = None
   
 
# def printGraph(graph):
#     print("--------------Graph start-----------")
#     for i in graph.keys():
#         neighbours = graph[i]
#         for i in range(len(neighbours)):
#             print(neighbours[i].name,' visited =',neighbours[i].visited,"visitedBy = ", neighbours[i].visitedBy, end=" ->   ")
#         print('')
#     print("--------------Graph end-------------")
        
        
# def checkUnexploredTerritory(graph, totalnodes):
#     bUnexplored = False
#     keys = graph.keys()
#     if len(keys) < totalnodes:
#         bUnexplored = True
#     else:
#         for i in keys:
#             if not graph[i][0].visited:
#                 bUnexplored = True
#                 #print(graph[i][0].name)
#                 #printGraph(graph)
#                 break
#     return bUnexplored
        


# def checkIfDetachedNode(graph, nodename, totalnodes):
#     return not nodename in graph and int(nodename) <= totalnodes
    
   
# def checkPosition(graph, strength, nodename, totalnodes):
#     #print("nodename = ",nodename)
#     if checkIfDetachedNode(graph, nodename, totalnodes):
#         node = QueueNode(nodename)
#         graph[nodename] = node
        
        
#     neighbours = graph[nodename]
#     if len(neighbours) == 0:
#         print("No")
#         return False
#     #print(graph["1"][1].name, graph["2"][0].name)
#     if neighbours[0].visited == True:
#         print("No")
#         return False
    
#     neighbours[0].visited = True
#     neighbours[0].visitedBy = nodename
#     queue = Queue()
#     queue.enqueue(neighbours[0])
#     while strength > 0:
#         if(queue.isEmpty()):
#             break
#         node = queue.dequeue()
#         #printGraph(graph)
#         for i in range(len(graph[node.name])):
#             neighbour = graph[node.name][i]
#             #print(neighbour.name)
#             if node.name != neighbour.name:
#                 if neighbour.visited == True and not neighbour.visitedBy == nodename:
#                     print("No")
#                     return False
#                 #printGraph(graph)
#                 neighbour.visited = True
#                 neighbour.visitedBy = nodename
#                 queue.enqueue(neighbour)
#         strength = strength - 1
#         #printGraph(graph)
#     return True
    
 
    
# def placeSoldiers(graph, soldiers, totalnodes):
#     bIsOptimal = True
#     for i in range(soldiers):
#         nodename, strength = input().split()
#         strength = int(strength)
#         #print("strength = ", strength, "and optima = ",bIsOptimal)
#         if bIsOptimal:
#             bIsOptimal = checkPosition(graph,strength,nodename, totalnodes)
            
#     bUnexplored = len(graph.keys()) < totalnodes or checkUnexploredTerritory(graph, totalnodes)
#     #printGraph(graph)
#     if bIsOptimal and not bUnexplored:
#         print("Yes")
        
    
    
# def buildGraph(edges):
#     #print("building graph")
#     graph = {}
#     for i in range(edges):
#         source, destination = input().split()
#         if source in graph:
#             srcNode = graph[source][0]
#         else:
#             srcNode = GraphNode(source)
#             graph[source] = [srcNode]
#         if destination in graph:
#             destNode = graph[destination][0]
#         else:
#             destNode = GraphNode(destination)
#             graph[destination] = [destNode]
#         graph[source].append(destNode)
#         graph[destination].append(srcNode)
#     #printGraph(graph)
#     return graph
        
        
# def readinput():
#     testcases = int(input())
#     for i in range(testcases):
#         nodes, edges, soldiers = input().split()
#         nodes = int(nodes)
#         edges = int(edges)
#         soldiers = int(soldiers)
#         graph = buildGraph(edges)
#         placeSoldiers(graph, soldiers, nodes)
    
    
    
# readinput()




#------------------------------------------------------------------
def printGraph(graph):
    print("--------------Graph start-----------")
    for i in graph.keys():
        neighbours = graph[i]
        for i in range(len(neighbours)):
            print(neighbours[i].name,"visitedBy = ","---", neighbours[i].visitedBy, end=" ->   ")
        print('')
    print("--------------Graph end-------------")

class QueNode:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class Que:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def traverseright(self):
        h = self.head
        while not h == None:
            print(h.data)
            h = h.next
            
    def traverseleft(self):
        h = self.tail
        while not h == None:
            print(h.data)
            h = h.prev
    
    def add(self, data):
        qnode = QueNode(data)
        if self.tail == None:
            self.head = qnode
            self.tail = qnode
        else:
            qnode.prev = self.tail
            self.tail.next = qnode
            self.tail = qnode
    
    def rem(self):
        #if last node
        data = None
        if self.head == None:
            return data
        elif self.head.next == None:
            data = self.head.data
            self.head = None
            self.tail = None
        else:
            data = self.head.data
            self.head = self.head.next
        return data
        
    
    def isEmpty(self):
        return self.tail == None and self.head == None 
        
        

class Gnode:
    def __init__(self, name):
        self.name = name
        self.visitedBy = None
        
     
    
def buildGraph(totalnodes, edges):
    graph = {}
    for i in range(edges):
        src, des = input().split()
        if src in graph and des in graph:
            srcNode = graph[src][0]
            desNode = graph[des][0]
        elif src not in graph and des not in graph:
            srcNode = Gnode(src)
            desNode = Gnode(des)
            graph[src] = [srcNode]
            graph[des] = [desNode]
        elif src not in graph:
            srcNode = Gnode(src)
            graph[src] = [srcNode]
        elif des not in graph:
            desNode = Gnode(des)
            graph[des] = [desNode]
        
        graph[src].append(desNode)
        graph[des].append(srcNode)
    return graph;
       
       
def evaluatePos(graph, nodename, strength):
    if not nodename in graph:
        graph[nodename] = [Gnode(nodename)] #placed on disconnected node
        graph[nodename][0].visitedBy = nodename
    elif graph[nodename][0].visitedBy != None:
        # placing soldier on someone else's territory
        print("No")
        return False
    else:
        graph[nodename][0].visitedBy = nodename
    
    if strength == 0:
        return True
    q = Que() #initialize the queue
    q.add(graph[nodename][0]) # insert the current node
    while not q.isEmpty() and strength > 0:
        currentnode = q.rem()
        neighbours = graph[currentnode.name]
        for neighbour in neighbours:
            if neighbour.name == currentnode.name:
                # self loop
                continue
            elif neighbour.visitedBy !=None and neighbour.visitedBy != nodename:
                # overlapping territory detected
                # print(neighbour.name, neighbour.visitedBy, currentnode.name)
                # printGraph(graph)
                # print("here")
                print("No")
                return False
            elif neighbour.visitedBy == None:
                neighbour.visitedBy = currentnode.name
                q.add(neighbour)
        strength = strength - 1                                                                                                                                                                                                 
    
    #if q.isEmpty() and strength == 0:
    q.traverseright()
    if strength == 0:
        return True
    else:
        # print(nodename)
        # print("here")
        # q.traverseright()
        print("No")
        return False
        
       
       
def checkPositions(graph, totalnodes, soldiers):
    bOptimal = True
    for i in range(soldiers):
        nodename, strength = input().split()
        strength = int(strength)
        if bOptimal:
            bOptimal = evaluatePos(graph, nodename, strength)
    
    if bOptimal  and totalnodes == len(graph.keys()): # All nodes are evaluated
        print("Yes")
        
       
       
def readinput():
    testcases = int(input())
    for i in range(testcases):
        totalnodes, connectededges, soldiers = input().split()
        totalnodes = int(totalnodes)
        connectededges = int(connectededges)
        soldiers = int(soldiers)
        graph = buildGraph(totalnodes, connectededges)
        checkPositions(graph, totalnodes, soldiers)
        
readinput()