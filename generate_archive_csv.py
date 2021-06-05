with open("ANSYS Batch Archive.csv", 'w') as csvfile:
    csvfile.write("Project Directory,Project Name (Exclude .wbpj extension),Cycle, Series,Archived Project Name,,,Available Cycles, Available Series\n")
    csvfile.close()