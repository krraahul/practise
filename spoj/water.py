# ##  ------------------------- version 1 start -----------------------------------
# from enum import Enum


# class Stack:
# 	def __init__(self):
# 		self.arr = []
	
# 	def push(self, item):
# 		self.arr.append(item)
		
# 	def pop(self):
# 		return self.arr.pop()
		
# 	def isEmpty(self):
# 		return len(self.arr) == 0
		
		
# class Node:
# 	def __init__(self, value):
# 		self.value = value
# 		self.visited = False
		
# 	def isLess(self,node):
# 		return self.value < node.value
	
	
# class QNode:
# 	def __init__(self, data):
# 		self.data = data
# 		self.prev = None
# 		self.next = None
		
		
		
# class Que:
# 	def __init__(self):
# 		self.head = None
# 		self.tail = None
	
# 	def push(self, item):
# 		node = QNode(item)
# 		if self.head == None:
# 			self.head = node
# 			self.tail = node
# 		else:
# 			node.next = self.head
# 			self.head.prev = node
# 			self.head = node
	
# 	def pop(self):
# 		data = None
# 		if self.isEmpty():
# 			return data
# 		if self.tail.prev == None:
# 			data = self.tail.data
# 			self.tail = None
# 			self.head = None
# 		else:
# 			data = self.tail.data
# 			prev = self.tail.prev
# 			prev.next = None
# 			self.tail.prev = None
# 			self.tail = prev
# 		return data
		
# 	def isEmpty(self):
# 		return self.head == None and self.tail == None
		
		
# class Direction(Enum):
# 	top = 1
# 	bottom = 2
	
		
# class MinHeap:
# 	def __init__(self, compareMin):
# 		self.arr = []
# 		self.size = 0
# 		self.compareMin = compareMin
		
# 	def isEmpty(self):
# 		return self.size == 0
		
# 	def swap(self, l, r):
# 		temp = self.arr[l]
# 		self.arr[l] = self.arr[r]
# 		self.arr[r] = temp
		
		
# 	def clearHeap(self):
# 	    self.arr.clear()
	
		
# 	def add(self, item):
# 		if self.isEmpty():
# 			self.arr.append(item)
# 			self.size = self.size + 1
# 			return
# 		else:
# 			self.arr.append(item)
# 			self.size = self.size + 1
# 			self.maintainheap(self.size - 1, Direction.top)
			
# 	def maintainheap(self, pos, direction):
# 		if pos !=0 and direction == Direction.top:
# 			p = int(pos/2)
# 			if not self.compareMin(self.arr[p],self.arr[pos]) < 0:
# 			#if not self.arr[p].isLess(self.arr[pos]):
# 				self.swap(p, pos)
# 				self.maintainheap(p, direction)
			
# 		if pos < self.size and direction == Direction.bottom:
# 			c1 = 2 * pos + 1
# 			c2 = 2 * pos + 2
# 			if c1 < self.size and c2 < self.size:
# 				smallest = c1
# 				if not self.compareMin(self.arr[smallest], self.arr[c2]) < 0:
# 				#if not self.arr[smallest].isLess(self.arr[c2]):
# 					smallest = c2
# 				if self.compareMin(self.arr[smallest], self.arr[pos]) < 0:
# 				#if self.arr[smallest].isLess(self[pos]):
# 					self.swap(pos, smallest)
# 					self.maintainheap(smallest, direction)
					
# 			if c1 < self.size:
# 				smallest = c1
# 				if self.compareMin(self.arr[smallest], self.arr[pos]) < 0:
# 				#if self.arr[smallest].isLess(self.arr[pos]):
# 					self.swap(pos, smallest)
# 					self.maintainheap(smallest, direction)
	
# 	def getMin(self):
# 		if (self.size - 1) < 0:
# 			return None
# 		self.swap(0, self.size - 1)
# 		data = self.arr.pop()
# 		self.size = self.size - 1
# 		self.maintainheap(0, Direction.bottom)
# 		return data
				
	



# def compareFn(pos1, pos2):
# 	node1 = graph[pos1[0]][pos1[1]]
# 	node2 = graph[pos2[0]][pos2[1]]
# 	return node1.value - node2.value
	
	
# graph = []
# RMax = 0
# CMax = 0
# hp = MinHeap(compareFn)
# tank = Node(0)
# Vol = 0
# Infinite = 999999999
# currHeight = 0

# def reset():
# 	graph = []
# 	RMax = 0
# 	CMax = 0
# 	hp = MinHeap(compareFn)
# 	tank.value = 0
# 	currHeight = 0
	
	



# def readInput():
# 	tcases = int(input())
# 	for t in range(tcases):
# 		reset()
# 		r, c = input().split()
# 		RMax = int(r)
# 		CMax = int(c)
# 		graph.clear()
# 		hp.clearHeap()
# 		for i in range(RMax):
# 			row = []
# 			rowinput = input().split()
# 			for j in range(CMax):
# 				num = int(rowinput[j])
# 				node = Node(num)
# 				row.append(node)
# 			graph.append(row)
# 		createHeap()
# 		calVol(RMax,CMax, tank)
# 		print(tank.value)
		



	
# def createHeap():
# 	for i in range(len(graph)):
# 		for j in range(len(graph[0])):
# 			hp.add((i,j))
			
			
# def calVol(RMax, CMax, tank):
#     currentHeight = 0
#     while not hp.isEmpty():
#         minNodePos = hp.getMin()
#         fillNode(minNodePos, RMax, CMax, tank)
#         newMinHeight = exploreSurface(minNodePos, RMax, CMax, tank)
#         if newMinHeight == None:
#             continue
#         if newMinHeight > currentHeight:
#             currentHeight = newMinHeight
#         #print("currentHeight = ", currentHeight)
#     #print("Volume = ", tank.value)
    

# def fillNode(minNodePos, RMax, CMax, tank):
#     x = minNodePos[0] 
#     y = minNodePos[1]
#     rc = [1,-1,0,0]
#     cc = [0,0,1,-1]
#     minNode = graph[x][y]
#     lowestNeighbourHeight = Infinite
#     for i in range(len(rc)):
#         nx = x +  rc[i]
#         ny = y + cc[i]
#         if nx < 0 or ny < 0 or not nx < RMax  or not ny < CMax:
#             return
#         newHeight = graph[nx][ny].value
#         if newHeight < lowestNeighbourHeight:
#             lowestNeighbourHeight = newHeight
#     if lowestNeighbourHeight < minNode.value:
#         return
#     #print("Filing single node",(x,y)," with value = ",lowestNeighbourHeight)
#     tank.value = tank.value + (lowestNeighbourHeight - minNode.value)
#     minNode.value = lowestNeighbourHeight
        
    

# def printGraph():
#     #print("-------start--------")
#     for i in range(len(graph)):
#         r = []
#         for j in range(len(graph[0])):
#             r.append(graph[i][j].value)
#         #print(r)
#     #print("----------end--------")
    
# def exploreSurface(minNodePos, RMax, CMax, tank):
#     q = Que()
#     st = Stack()
#     newMinHeight = Infinite
#     x = minNodePos[0] 
#     y = minNodePos[1]
#     startingNode = graph[x][y]
#     h = startingNode.value
#     #print("Starting exploring surface for height = ", h , "at pos =",(x,y))
#     #printGraph()
#     q.push((startingNode, x, y))
#     while not q.isEmpty():
#         nnode,x,y = q.pop()
#         #print("taken out from the que",(x,y))
#         if nnode.visited == True:
#             #print("landed here")
#             continue
#         nnode.visited = True
#         st.push((nnode, x, y))
#         newMin = exploreNeighbours(x,y,h,q,RMax,CMax, st)
 
#         if newMin == None:
#             return None
        
#         if newMin < h:
#             while not st.isEmpty():
#                 node = st.pop()[0]
#                 node.visited = False
#             return None
#         if newMin < newMinHeight and newMin > h:
#             newMinHeight = newMin
        
#     #print("Found new Level of Vol = ", newMinHeight," for ",(x,y))
#     while not st.isEmpty():
#         node,dx,dy = st.pop()
#         node.visited = False
#         tank.value = tank.value + (newMinHeight - node.value)
#         node.value = newMinHeight
#         #print("Filing ",((dx,dy)), " with ",newMinHeight - node.value)
    
    
    
    
# def emptyTheStack(st):
#      while not st.isEmpty():
#                 node = st.pop()[0]
#                 node.visited = False
                
                
    
# def exploreNeighbours(x,y,h,q, RMax, CMax, st):
#     rc = [1,-1,0,0]
#     cc = [0,0,1,-1]
#     lowestheight = Infinite
#     for i in range(len(rc)):
#         nx = x + rc[i]
#         ny = y + cc[i]
       
#         if nx < 0 or ny < 0 or nx >= RMax or ny >= CMax:
#             while not st.isEmpty():
#                 node = st.pop()[0]
#                 node.visited = False
#             return None
#         #print("for ",(x,y),"======neighbours ======",(nx,ny))
#         nnode = graph[nx][ny]
#         if nnode.visited:
#             continue
#         nnodeheight = nnode.value
#         #print("nnodeheight = ", nnodeheight)
#         if nnodeheight < h:
#             #print("lowerheight found")
#             emptyTheStack(st)
#             return None
#         if nnodeheight == h:
#             q.push((nnode,nx,ny))
#             #print("adding to the que = ",(nx,ny))
#         if nnodeheight < lowestheight and nnodeheight > h:
#             lowestheight = nnodeheight
#     #print("Returning lowest height of neighbours = ",lowestheight)
#     return lowestheight
    
# readInput()

# ## ----------------------------version 1 end ------------------------------







# ## ----------------------------version 2 start ----------------------------
# from enum import Enum
# import sys

# class Stack:
# 	def __init__(self):
# 		self.arr = []
	
# 	def push(self, item):
# 		self.arr.append(item)
		
# 	def pop(self):
# 		return self.arr.pop()
		
# 	def isEmpty(self):
# 		return len(self.arr) == 0
		
		
# class Node:
# 	def __init__(self, value):
# 		self.value = value
# 		self.visited = False
		
# 	def isLess(self,node):
# 		return self.value < node.value
	
	
# class QNode:
# 	def __init__(self, data):
# 		self.data = data
# 		self.prev = None
# 		self.next = None
		
		
		
# class Que:
# 	def __init__(self):
# 		self.head = None
# 		self.tail = None
	
# 	def push(self, item):
# 		node = QNode(item)
# 		if self.head == None:
# 			self.head = node
# 			self.tail = node
# 		else:
# 			node.next = self.head
# 			self.head.prev = node
# 			self.head = node
	
# 	def pop(self):
# 		data = None
# 		if self.isEmpty():
# 			return data
# 		if self.tail.prev == None:
# 			data = self.tail.data
# 			self.tail = None
# 			self.head = None
# 		else:
# 			data = self.tail.data
# 			prev = self.tail.prev
# 			prev.next = None
# 			self.tail.prev = None
# 			self.tail = prev
# 		return data
		
# 	def isEmpty(self):
# 		return self.head == None and self.tail == None
		
		
# class Direction(Enum):
# 	top = 1
# 	bottom = 2
	
		
# class MinHeap:
# 	def __init__(self, compareMin, graph):
# 		self.arr = []
# 		self.size = 0
# 		self.compareMin = compareMin
# 		MinHeap.graph = graph
		
# 	graph = None
		
# 	def isEmpty(self):
# 		return self.size == 0
		
# 	def swap(self, l, r):
# 		temp = self.arr[l]
# 		self.arr[l] = self.arr[r]
# 		self.arr[r] = temp
		
		
# 	def clearHeap(self):
# 	    self.arr.clear()
	
		
# 	def add(self, item):
# 		if self.isEmpty():
# 			self.arr.append(item)
# 			self.size = self.size + 1
# 			return
# 		else:
# 			self.arr.append(item)
# 			self.size = self.size + 1
# 			self.maintainheap(self.size - 1, Direction.top)
			
# 	def maintainheap(self, pos, direction):
# 		if pos !=0 and direction == Direction.top:
# 			p = int(pos/2)
# 			if not self.compareMin(self.arr[p],self.arr[pos]) < 0:
# 			#if not self.arr[p].isLess(self.arr[pos]):
# 				self.swap(p, pos)
# 				self.maintainheap(p, direction)
			
# 		if pos < self.size and direction == Direction.bottom:
# 			c1 = 2 * pos + 1
# 			c2 = 2 * pos + 2
# 			if c1 < self.size and c2 < self.size:
# 				smallest = c1
# 				if not self.compareMin(self.arr[smallest], self.arr[c2]) < 0:
# 				#if not self.arr[smallest].isLess(self.arr[c2]):
# 					smallest = c2
# 				if self.compareMin(self.arr[smallest], self.arr[pos]) < 0:
# 				#if self.arr[smallest].isLess(self[pos]):
# 					self.swap(pos, smallest)
# 					self.maintainheap(smallest, direction)
					
# 			if c1 < self.size:
# 				smallest = c1
# 				if self.compareMin(self.arr[smallest], self.arr[pos]) < 0:
# 					self.swap(pos, smallest)
# 					self.maintainheap(smallest, direction)
	
# 	def getMin(self):
# 		if (self.size - 1) < 0:
# 			return None
# 		self.swap(0, self.size - 1)
# 		data = self.arr.pop()
# 		self.size = self.size - 1
# 		self.maintainheap(0, Direction.bottom)
# 		return data
				
	



# def compareFn(pos1, pos2):
# 	node1 = MinHeap.graph[pos1[0]][pos1[1]]
# 	node2 = MinHeap.graph[pos2[0]][pos2[1]]
# 	return node1.value - node2.value
	
	

# Infinite = 999999



# def readInput():
# 	tcases = int(input())
# 	for t in range(tcases):
# 		r, c = input().split()
# 		RMax = int(r)
# 		CMax = int(c)
# 		graph = []
# 		#print((RMax,CMax))
# 		tank = Node(0)
# 		hp = MinHeap(compareFn, graph)
# 		for i in range(RMax):
# 			row = []
# 			#print("here")
# 			#print(i)
# 			rowinput = input().split()
# 			#print(rowinput)
# 			for j in range(CMax):
# 				#print(j)
# 				num = int(rowinput[j])
# 				#print(num)
# 				node = Node(num)
# 				row.append(node)
# 			graph.append(row)
# 		createHeap(graph, hp)
# 		calVol(RMax,CMax, tank, hp, graph)
# 		print(tank.value)
		



	
# def createHeap(graph, hp):
# 	for i in range(len(graph)):
# 		for j in range(len(graph[0])):
# 			hp.add((i,j))
			
			
# def calVol(RMax, CMax, tank, hp, graph):
#     currentHeight = 0
#     while not hp.isEmpty():
#         minNodePos = hp.getMin()
#         fillNode(minNodePos, RMax, CMax, tank, graph)
#         newMinHeight = exploreSurface(minNodePos, RMax, CMax, tank, graph)
#         if newMinHeight == None:
#             continue
#         if newMinHeight > currentHeight:
#             currentHeight = newMinHeight

    

# def fillNode(minNodePos, RMax, CMax, tank, graph):
#     x = minNodePos[0] 
#     y = minNodePos[1]
#     rc = [1,-1,0,0]
#     cc = [0,0,1,-1]
#     minNode = graph[x][y]
#     lowestNeighbourHeight = Infinite
#     for i in range(len(rc)):
#         nx = x +  rc[i]
#         ny = y + cc[i]
#         if nx < 0 or ny < 0 or not nx < RMax  or not ny < CMax:
#             return
#         newHeight = graph[nx][ny].value
#         if newHeight < lowestNeighbourHeight:
#             lowestNeighbourHeight = newHeight
#     if lowestNeighbourHeight < minNode.value:
#         return
#     tank.value = tank.value + (lowestNeighbourHeight - minNode.value)
#     minNode.value = lowestNeighbourHeight
        
    


    
# def exploreSurface(minNodePos, RMax, CMax, tank, graph):
#     q = Que()
#     st = Stack()
#     newMinHeight = Infinite
#     x = minNodePos[0] 
#     y = minNodePos[1]
#     startingNode = graph[x][y]
#     h = startingNode.value
    
#     q.push((startingNode, x, y))
#     while not q.isEmpty():
#         nnode,x,y = q.pop()
        
#         if nnode.visited == True:
#             continue
#         nnode.visited = True
#         st.push((nnode, x, y))
#         newMin = exploreNeighbours(x,y,h,q,RMax,CMax, st, graph)
 
#         if newMin == None:
#             return None
        
#         if newMin < h:
#             while not st.isEmpty():
#                 node = st.pop()[0]
#                 node.visited = False
#             return None
#         if newMin < newMinHeight and newMin > h:
#             newMinHeight = newMin
        
    
#     while not st.isEmpty():
#         node,dx,dy = st.pop()
#         node.visited = False
#         tank.value = tank.value + (newMinHeight - node.value)
#         node.value = newMinHeight
        
    
    
    
    
# def emptyTheStack(st):
#      while not st.isEmpty():
#                 node = st.pop()[0]
#                 node.visited = False
                
                
    
# def exploreNeighbours(x,y,h,q, RMax, CMax, st, graph):
#     rc = [1,-1,0,0]
#     cc = [0,0,1,-1]
#     lowestheight = Infinite
#     #print((x,y))
#     for i in range(len(rc)):
#         nx = x + rc[i]
#         ny = y + cc[i]
       
#         if nx < 0 or ny < 0 or nx >= RMax or ny >= CMax:
#             while not st.isEmpty():
#                 node = st.pop()[0]
#                 node.visited = False
#             return None
#         #print("for ",(x,y),"======neighbours ======",(nx,ny))
#         nnode = graph[nx][ny]
#         if nnode.visited:
#             continue
#         nnodeheight = nnode.value
        
#         if nnodeheight < h:
            
#             emptyTheStack(st)
#             return None
#         if nnodeheight == h:
#             q.push((nnode,nx,ny))
            
#         if nnodeheight < lowestheight and nnodeheight > h:
#             lowestheight = nnodeheight
    
#     return lowestheight
    
# readInput()
# # import traceback
# # from pprint import pprint
# # try:
# # 	readInput()
# # except:
# # 	exc_type, exc_value, exc_tb = sys.exc_info()
# # 	pprint(traceback.format_exception(exc_type, exc_value, exc_tb))
# ## ----------------------------version 2 end ------------------------------














## +++++++++++++++++++++++++= version 3 start ++++++++++++++

class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        
        

def compFn(item):
    return item[0].value
        
def readGraph(graph, graphoriginal, maxrows, maxcols):
    for i in range(maxrows):
        ithrow = input().split()
        for j in range(maxcols):
            elem = int(ithrow[j])
            pos = i * maxcols + j
            graphoriginal.append((Node(elem), pos))
            graph.append((Node(elem), pos))
            graph.sort(key=compFn)
            
            
            
def printGraph(graph, cmax):
    row = []
    for i in range(len(graph)):
        row.append(graph[i][0].value)
        if (i+1)%cmax == 0:
            print(row)
            row.clear()
        
        
            

def readInput():
    testcases = int(input())
    for i in range(testcases):
        graphsorted = []
        graphoriginal = []
        tank = Node(0)
        maxrows, maxcols = input().split()
        maxrows = int(maxrows)
        maxcols = int(maxcols)
        readGraph(graphsorted, graphoriginal, maxrows, maxcols)
        calVol(graphsorted, graphoriginal, maxrows, maxcols,tank)
        print(tank.value)
        #fillGraph(graphoriginal, maxrows, maxcols, 7, tank)
        # print(graph)
        # print(graphoriginal)
    printGraph(graphoriginal, maxcols)
   
   

def calVol(graphsorted, graphoriginal, maxrows, maxcols,tank):
    for i in range(len(graphsorted)):
         originalpos = graphsorted[i][1]
         originalheight = graphsorted[i][0].value
         if graphoriginal[originalpos][0].value > originalheight:
             continue
         
         fillGraph(graphoriginal, maxrows, maxcols, originalpos, tank)
         newheight = graphoriginal[originalpos][0].value
         explore_surface(graphoriginal, originalpos, newheight, maxrows, maxcols, tank)
        
    
    
def fillGraph(graph, rmax, cmax, pos, tank):
    rc = [1,-1,0,0]
    cc = [0,0,1,-1]
    x = int(pos/cmax)
    y = pos % cmax
    minheight = 9999999
    originalheight = graph[pos][0].value
    print("trying to  fill column of height  = ", graph[pos][0].value, " at", (x,y))
    for i in range(len(rc)):
        nx = x + rc[i]
        ny = y + cc[i]
        if nx < 0 or ny < 0 or not nx < rmax or not ny < cmax:
            minheight = graph[pos][0].value
            return
            break
        
        npos = (nx * cmax) + ny
        print(graph[npos][0].value)
        if graph[npos][0].value <= originalheight:
            return
        if minheight > graph[npos][0].value:
            minheight = graph[npos][0].value
    tank.value =tank.value +  (minheight - graph[pos][0].value)
    print("Single column fill with value = ", minheight)
    print("tank value here = ",tank.value)
    graph[pos][0].value = minheight
    
    
    
def explore_neighbours(graph, rmax, cmax, pos, que):
    rc = [1,-1,0,0]
    cc = [0,0,1,-1]
    x = int(pos/cmax)
    y = pos % cmax
    minheight = 9999999
    originalheight = graph[pos][0].value
    print("original height  = ", originalheight, " at",(x,y))
    for i in range(len(rc)):
        nx = x + rc[i]
        ny = y + cc[i]
        if nx < 0 or ny < 0 or not nx < rmax or not ny < cmax:
            minheight = graph[pos][0].value
            return None
        
        npos = (nx * cmax) + ny
        if graph[npos][0].value == 37:
            print("-----------------hell ya ----", graph[npos][0].visited)
        print("Exploring ",graph[npos][0].value)
        if graph[npos][0].visited:
            continue
        #print("Exploring ",graph[npos][0].value)
        if graph[npos][0].value < graph[pos][0].value:
            return None
        if graph[npos][0].value == originalheight:
            que.append(npos)
            print("pushing to que = ",(nx,ny))
       
        if minheight > graph[npos][0].value and not graph[npos][0].visited and graph[npos][0].value > originalheight:
            minheight = graph[npos][0].value
    print("new height = ", minheight)
    return minheight
    
    
    
def flushoutStack(graph, stack):
    while len(stack) > 0:
        pos = stack.pop()
        graph[pos][0].visited = False
        
        
def explore_surface(graph, pos, surfaceheight, rmax, cmax, tank):
    que = []
    stack = []
    minwallheight = 99999999
    que.append(pos)
    while len(que) > 0:
        nodepos = que.pop(0)
        
        neighbourmin = explore_neighbours(graph, rmax, cmax, nodepos, que)
        if neighbourmin == None:
            flushoutStack(graph, stack)
            return
        
        graph[nodepos][0].visited = True
        stack.append(nodepos)
            
        print("min wall height",minwallheight)
        if minwallheight > neighbourmin and minwallheight > surfaceheight:
            minwallheight = neighbourmin
            
    while len(stack) > 0:
        print("here")
        nodepos = stack.pop()
        print("current height = ", graph[nodepos][0].value, "and final height = ", minwallheight)
        tank.value = tank.value + (minwallheight - graph[nodepos][0].value)
        print("tank value = ", tank.value)
        graph[nodepos][0].value = minwallheight
    flushoutStack(graph, stack)
        
    
        
        


readInput()
## ---------------------------version3 end -----------------