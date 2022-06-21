import Pyro4

#uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()
name = input("Siapa nama anda? ").strip()
npm = input("Berapa npm anda? ").strip()
major = input("Jurusan apakah anda? ").strip()
# use name server object lookup uri shortcut
server = Pyro4.Proxy("PYRONAME:server")    
print(server.welcomeMessage(name, npm, major))




