import os
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"
import h5py
file = h5py.File('west.h5','r')
import subprocess

bashCommand = "w_pdist"  #pdist to monitor the simulation progress
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
bashCommand = "w_succ -W west.h5 -o output.dat"  #pdist to monitor the simulation progress
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

