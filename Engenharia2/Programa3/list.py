import math

class Node:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.next = None
    self.prev = None
  
  def __repr__(self):
    return (self.x, self.y)

class LinkedList:
  def __init__(self):    
    self.first = None
    self.size = 0
    self.totalX = 0
    self.totalY = 0
    self.XY = 0
    self.XX = 0
    self.YY = 0

  def __repr__(self):
    node = self.first
    nodes = []
    for i in range(self.size):
      nodes.append(f"({node.x},{node.y})")
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

  def add(self, x, y, pos=None):
    if pos == None:
      pos = self.size
    
    if pos < 0 or pos > self.size:
      return False

    self.totalX += x
    self.totalY += y
    self.XY += x*y
    self.XX += x*x
    self.YY += y*y
    
    newNode = Node(x, y)
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

    self.totalX -= returnNode.x
    self.XX -= returnNode.x*returnNode.x

    self.totalY -= returnNode.y
    self.YY -= returnNode.y*returnNode.y

    self.XY -= returnNode.x*returnNode.y

    return (returnNode.x, returnNode.y)

  def average(self):
    return (self.totalX/self.size, self.totalY/self.size)

  def standardDeviation(self):
    avgX, avgY = self.average()
    sumX = 0
    sumY = 0
    curr = self.first
    for i in range(self.size):
      sumX += pow(curr.x - avgX, 2)
      sumY += pow(curr.y - avgY, 2)
      curr = curr.next
    return (math.sqrt(sumX/(self.size-1)), math.sqrt(sumY/(self.size-1)))

  def linearRegression(self):
    avgX, avgY = self.average()
    N = self.size
    b1 = (self.XY - N*avgX*avgY)/(self.XX - N*avgX*avgX)
    b0 = avgY - b1*avgX
    return (b0, b1)

  def correlation(self):
    N = self.size
    r = (N*(self.XY) - self.totalX*self.totalY)/math.sqrt((N*self.XX - self.totalX*self.totalX)*(N*self.YY - self.totalY*self.totalY))
    return (r, r*r)

  def estimate(self, xk):
    b0, b1 = self.linearRegression()
    return b0 + b1*xk