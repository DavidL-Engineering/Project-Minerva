import os
from psutil import virtual_memory

tot_mem_GB = round(virtual_memory().total / (1024 ** 3))
cores_by_mem = tot_mem_GB / 8

physical_cores = os.cpu_count()/2

if cores_by_mem < physical_cores:
    parallel_processes = cores_by_mem
else:
    parallel_processes = physical_cores

with open("Simulation Parameters.csv", 'w') as csvfile:
    csvfile.write("Simulation Name,.CAS File Name (Exclude \".cas\" file extension),.CAS File Directory,Body Type (HB/FB),Solution Method (K-W/T-SST),Override Velocity [m/s] (Blank for 18 m/s),Area [m^2],Length[m],CG (Y/N),CGx [m], CGy [m],CGz [m],Post-Processing (Y/N),Streamline Animations (Y/N),,Workbench Project Name,Workbench Project Save Directory,Results Directory,Fluent Processes\n,,,,,,,,,,,,,,,,,,{}".format(parallel_processes))
    csvfile.close()