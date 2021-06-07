# encoding: utf-8
# 2020 R1
SetScriptVersion(Version="20.1.164")

import os

abspath = os.path.abspath(__file__)
dir = os.path.dirname(abspath)
os.chdir(dir)

csvfile = open("Ansys Batch Archive.csv", 'r')

next(csvfile)
lines = csvfile.readlines()

proj_dir = []
proj_name = []
cycle = []
series = []
archive_name = []

for line in lines:
    entries = line.split(",")
    proj_dir.append(entries[0])
    proj_name.append(entries[1])
    cycle.append(entries[2])
    series.append(entries[3])
    archive_name.append(entries[4].strip())

csvfile.close()

for j in range(len(proj_dir)):
    Open(FilePath="{}/{}.wbpj".format(proj_dir[j].replace(os.sep, '/'), proj_name[j]))
    Archive(
        FilePath="//172.16.1.12/hpc/sims/Archives/{}/{}/{}.wbpz".format(cycle[j], series[j], archive_name[j]),
        IncludeExternalImportedFiles=True)