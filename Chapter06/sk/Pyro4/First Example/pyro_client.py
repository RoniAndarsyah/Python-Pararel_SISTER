import Pyro4

#uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()
name = input("Masukan nama anda? ").strip()
birth_year = int(input("Masukan tahun lahir anda "))
# use name server object lookup uri shortcut
server = Pyro4.Proxy("PYRONAME:server")    
print(server.welcomeMessage(name))
print(server.calculateAge(birth_year))