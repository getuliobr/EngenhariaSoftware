import math

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
  
  def __repr__(self):
    return self.value

class LinkedList:
  def __init__(self):    
    self.first = None
    self.size = 0
    self.total = 0

  def __repr__(self):
    node = self.first
    nodes = []
    for i in range(self.size):
      nodes.append(str(node.value))
      node = node.next
    nodes.append("None")
    return " -> ".join(nodes)

  def __add_first(self, newNode):
    newNode.next = self.first
    if self.first:
      newNode.prev = self.first.prev
    self.first = newNode
  
  def __add_middle(self, curr, newNode):
    newNode.next = curr.next
    if newNode.next:
      newNode.next.prev = newNode
    curr.next = newNode
    newNode.prev = curr

  def add(self, value, pos=None):
    if pos == None:
      pos = self.size
    
    if pos < 0 or pos > self.size:
      return False

    self.total += value
    
    newNode = Node(value)
    if(pos == 0):
      self.__add_first(newNode)
    else:
      curr = self.first
      for i in range(pos - 1):
        curr = curr.next
      self.__add_middle(curr, newNode)

    self.size += 1

    return True

  def remove(self, pos):
    if pos < 0 or pos > self.size:
      return False

    returnNode = None
    if(pos == 0):
      returnNode = self.first
      self.first = self.first.next
      if self.first:
        self.first.prev = None
    else:
      returnNode = self.first
      for i in range(pos):
        returnNode = returnNode.next
      
      if returnNode.next:
        returnNode.next.prev = returnNode.prev
      returnNode.prev.next = returnNode.next

    self.size -= 1
    self.total -= returnNode.value
    return returnNode.value

  def average(self):
    return self.total/self.size

  def standardDeviation(self):
    avg = self.average()
    sum = 0
    curr = self.first
    for i in range(self.size):
      sum += pow(curr.value - avg, 2)
      curr = curr.next
    return math.sqrt(sum/(self.size-1))

  def averageLog(self):
    sum = 0
    curr = self.first
    for i in range(self.size):
      sum += math.log(curr.value)
      curr = curr.next
    return sum/self.size

  def logVariants(self):
    sum = 0
    avg = self.averageLog()
    curr = self.first
    for i in range(self.size):
      sum += (math.log(curr.value) - avg)**2
      curr = curr.next
    return sum/(self.size - 1)

  def logStandardDeviation(self):
    return math.sqrt(self.logVariants())

  def estimateRange(self):
    avg = self.averageLog()
    o = self.logStandardDeviation()
    PP = avg - 2*o
    P = avg - o 
    M = avg
    G = avg + o
    GG = avg + 2*o

    return PP, P, M, G, GG

  def estimateLimits(self):
    PP, P, M, G, GG = self.estimateRange()
    return math.exp(PP), math.exp(P), math.exp(M), math.exp(G), math.exp(GG)