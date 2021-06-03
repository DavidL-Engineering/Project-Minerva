# encoding: utf-8
# 2020 R1
SetScriptVersion(Version="20.1.164")

from resources import *

(sim_list, proj_params) = param_extract("Simulation Parameters.csv")

initialize_project(proj_params)

fluent_sim_setup(sim_list, proj_params.processes)