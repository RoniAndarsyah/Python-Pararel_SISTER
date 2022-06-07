from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = (rank+1)**2

data = comm.gather(data, root=3)

if rank == 3:
   print ("rank = %s " %rank +\
          "...receiving data to other process")
   for i in range(1,size):

      value = data[i]
      print(" process %s receiving %s from process %s"\
            %(rank , value , i))

else:
    print('aku nganggur lho cuman jalanin data ajah yang diatas, aku proses :'+str(rank))