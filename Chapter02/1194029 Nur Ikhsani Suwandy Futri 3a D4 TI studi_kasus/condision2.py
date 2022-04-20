import threading
import time
from random import randint

class SomeItem:
  # init method
  def _init_(self):
    # initialize empty list
    self.list = []
  
  # add to list method for producer
  def produce(self, item):
    print("Adding item to list...")
    self.list.append(item)
    
  # remove item from list method for consumer
  def consume(self):
    print("consuming item from list...")
    item = self.list[0]
    print("Item consumed: ", item)
    self.list.remove(item)

def producer(si, cond):
    r = randint(1,5)
    # creating random number of items
    for i in range(1, r):
      print("working on item creation, it will take: " + str(i) + " seconds")
      time.sleep(i)
      print("acquiring lock...")
      cond.acquire()
      try:
        si.produce(i)
        cond.notify()
      finally:
        cond.release()
      
def consumer(si, cond):
    cond.acquire()
    while True:
      try:
        si.consume()
      except:
        print("No item to consume...")
        # wait with a maximum timeout of 10 sec
        val = cond.wait(10)
        if val:
          print("notification received about item production...")
          continue
        else:
          print("waiting timeout...")
          break
        
    cond.release()
    
if __name__=='main_':
  # condition object
  cond = threading.Condition()
  # SomeItem object
  si = SomeItem()
  # producer thread
  p = threading.Thread(target=producer, args=(si,cond,))
  p.start()
  # consumer thread
  c = threading.Thread(target=consumer, args=(si,cond,))
  c.start()

  #print('Waiting for producer and consumer threads...')
  p.join()
  c.join()
  print("Done")