# Tugas Studi Kasus 
import threading
import time

def start_checkout():
  print("starting checkout the payment...")
  time.sleep(2)
  
def payment(b):
    start_checkout()
    b.wait()
    print("Successfully payment")

def confirmation(b):
    print("waiting for payment getting ready...")
    b.wait()
    print("sending email confirmation...")
    
if __name__=='__main__':
  
  b = threading.Barrier(2, timeout=5)
  payment = threading.Thread(target=payment, args=(b,))
  payment.start()
  confirmation = threading.Thread(target=confirmation, args=(b,))
  confirmation.start()

  payment.join()
  confirmation.join()
  print("Done")