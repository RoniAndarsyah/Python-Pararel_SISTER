import multiprocessing
  
def admin(conn, events):
    for event in events:
        conn.send(event)
        print(f"Admin mengcheck informasi: {event}")
  
def user(conn):
    while True:
        event = conn.recv()
        if event == "tolak": 
            print("Role user tidak di approve")    
            return
        print(f"username: {event} diapprove menjadi Owner")
  


if __name__ == "__main__":
    events = ["udinkeren", "papopeee", "Pack Brodi the guardian of kos", "Harry Potter", "tolak"]
    conn1, conn2 = multiprocessing.Pipe()
    process_1 = multiprocessing.Process(target=admin, args=(conn1, events))
    process_2 = multiprocessing.Process(target=user, args=(conn2,))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()