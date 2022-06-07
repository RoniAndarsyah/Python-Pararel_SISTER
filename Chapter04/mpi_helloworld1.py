from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
  print("First rank")
elif rank == 1:
  print ("Second rank")
else:
  print("Not first or second rank")
    
print("Hello world from rank", str(rank), "of", str(size))