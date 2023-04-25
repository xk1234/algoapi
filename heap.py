import array

class Heap:
  #         0 -> Smallest
  #    1          2
  #  3   4     5     6
  #7  8 9 10 11 12 13 14 -> Biggest
  def __init__(self, arr=[]):
    self.h = array.array('d', arr)
    self.n = 0

  def left(self, i):
    return self.h[2 * i + 1]

  def right(self, i):
    return self.h[2*i+2]

  def parent(self, i):
    return self.h[(i-1)//2]

  def parentpos(self,i):
    return (i-1)//2

  def leftpos(self, i):
    return 2 * i + 1

  def rightpos(self, i):
    return 2*i+2
  
  def add(self, data):
    self.h.append(data)
    self.bubbleup(self.n)
    self.n += 1

  def removeMin(self):
    # remove element at idx from the heap
    mn = self.h[0]
    self.h[0] = self.h[self.n-1]
    self.h = self.h[:-1]
    self.bubbledown(0)
    return mn
  def bubbleup(self, idx):
    pos = idx
    print(self.h[pos], self.parent(pos))
    # while element at pos < parent
    while self.h[pos] < self.parent(pos):
      # swap with parent
      self.h[pos], self.h[self.parentpos(pos)] = self.h[self.parentpos(pos)], self.h[pos]
      pos = self.parentpos(pos)

  def bubbledown(self, idx):
    pos = idx
    
    # while element at pos > min of children
    while min(self.left(pos), self.right(pos)) > self.h[pos]:
      if self.left(pos) < self.right(pos):
        # swap with left child
        self.h[pos], self.h[self.leftpos(pos)] = self.h[self.leftpos(pos)], self.h[pos]
        pos = self.leftpos(pos)
      else:
        # swap with right child
        self.h[pos], self.h[self.rightpos(pos)] = self.h[self.rightpos(pos)], self.h[pos]
        pos = self.rightpos(pos)

  def __str__(self):
    return str(self.h)


h = Heap([1] + list(range(1,15)))
