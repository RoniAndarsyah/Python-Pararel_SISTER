import multiprocessing
  
def konduktor(conn, events):
    for event in events:
        conn.send(event)
        print(f"Dirijen mengirim tanda: {event}")
  
def pemain_alat_musik(conn):
    while True:
        event = conn.recv()
        if event == "eod": 
            print("Pemain alat musik menerima: permainan alat musik berhenti")    
            return
        print(f"Pemain alat musik menerima: {event}")
  


if __name__ == "__main__":
    events = ["Violin mulai bermain", "Cello mulai bermain", "Double bass mulai bermain", "Harpa mulai bermain", "end"]
    conn1, conn2 = multiprocessing.Pipe()
    process_1 = multiprocessing.Process(target=konduktor, args=(conn1, events))
    process_2 = multiprocessing.Process(target=pemain_alat_musik, args=(conn2,))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()