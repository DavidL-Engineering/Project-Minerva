import os
with open("Simulation Parameters.csv", 'w') as csvfile:
    csvfile.write("Simulation Name,.CAS File Name (Exclude \".cas\" file extension),.CAS File Directory,Body Type (HB/FB),Solution Method (K-W/T-SST),Override Velocity [m/s] (Blank for 18 m/s),Area [m^2],Length[m],CG (Y/N),CGx [m], CGy [m],CGz [m],Post-Processing (Y/N),Streamline Animations (Y/N),,Workbench Project Name,Workbench Project Save Directory,Results Directory,Fluent Processes\n,,,,,,,,,,,,,,,,,{}".format(os.cpu_count()/2))
    csvfile.close()