from mpi4py import MPI
import numpy as np
from my_function import *


# get number of processors and processor rank
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

params = np.random.random((15, 3)) * 100.0  # parameters to send to my_function
n = params.shape[0]

count = n // size  # number of catchments for each process to analyze
remainder = n % size  # extra catchments if n is not a multiple of size

if rank < remainder:  # processes with rank < remainder analyze one extra catchment
    start = rank * (count + 1)  # index of first catchment to analyze
    stop = start + count + 1  # index of last catchment to analyze
else:
    start = rank * count + remainder
    stop = start + count

local_params = params[start:stop, :]  # get the portion of the array to be analyzed by each rank
local_results = np.empty((local_params.shape[0], local_params.shape[1] + 1))  # create result array
local_results[:, :local_params.shape[1]] = local_params  # write parameter values to result array
local_results[:, -1] = my_function(local_results[:, 0], local_results[:, 1], local_results[:, 2])  # run the function for each parameter set and rank

# send results to rank 0
if rank > 0:
    comm.Send(local_results, dest=0, tag=14)  # send results to process 0
else:
    final_results = np.copy(local_results)  # initialize final results with results from process 0
    for i in range(1, size):  # determine the size of the array to be received from each process
        if i < remainder:
            rank_size = count + 1
        else:
            rank_size = count
        tmp = np.empty((rank_size, final_results.shape[1]), dtype=np.float)  # create empty array to receive results
        comm.Recv(tmp, source=i, tag=14)  # receive results from the process
        final_results = np.vstack((final_results, tmp))  # add the received results to the final results
    print("results")
    print(final_results)