import socket
s =socket.socket()
host=socket.gethostname()
port=60000
s.connect((host,port))
s.send('Selamat Datang di server kita!'.encode())
with open('received.txt','wb') as f:
    print ('File dibuka')
    while True :
        print ('Menerima data...')
        data=s.recv(1024)
        if not data:
            break
        print ('Data=>',data.decode())
        # write data to a file
        f.write(data)
f.close()
print ('Berhasil mendapatkan file')
s.close()
print ('Koneksi terputus')
