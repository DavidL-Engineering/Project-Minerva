import os

class Mesh_Properties:
    def __init__(self, CAS_name = None, CAS_dir = None):
        self.CAS_name = CAS_name
        self.CAS_dir = CAS_dir
    
    def __str__(self):
        return "\n----MESH PROPERTIES----\nCAS file: {}\nLocated in {}".format(self.CAS_name, self.CAS_dir)

class Dimension_Properties:
    def __init__(self, area = None, length = None, CG_X = None, CG_Y = None, CG_Z = None):
        self.area = area #Stored in m^2
        self.length = length #Stored in m
        self.CG_X = CG_X #Stored in m
        self.CG_Y = CG_Y #Stored in m
        self.CG_Z = CG_Z #Stored in m
    
    def __str__(self):
        return "\n----DIMENSION PROPERTIES----\nArea is {}. Length is {}. Center of Gravity is ({}, {}, {})".format(self.area, self.length, self.CG_X, self.CG_Y, self.CG_Z)

class Workflow_Properties:
    def __init__(self, sol_method = None, CG = None, post = None, streamlines = None, results_dir = None):
        self.sol_method = sol_method #Either K-W or T-SST
        self.CG = CG #Either True or False
        self.post = post #Either True or False
        self.streamlines = streamlines #True or False
        self.results_dir = results_dir

    def __str__(self):
        return "\n----WORKFLOW PROPERTIES----\nSolution method: {}\nCG: {}\nPost-Processing: {}\nStreamline Animations: {}\nResults located in: {}".format(self.sol_method, self.CG, self.post, self.streamlines, self.results_dir)

class Simulation_Results:
    def __init__(self, convergence = None, iterations = None, drag_tot = None, drag_comp = None, lift_tot = None, lift_comp = None, f_left = None, f_right = None, mom_roll = None, mom_pitch = None, mom_yaw = None):
        self.convergence = convergence
        self.iterations = iterations
        self.drag_tot = drag_tot
        self.drag_comp = drag_comp
        self.lift_tot = lift_tot
        self.lift_comp = lift_comp
        self.f_left = f_left
        self.f_right = f_right
        self.mom_roll = mom_roll
        self.mom_pitch = mom_pitch
        self.mom_yaw = mom_yaw

class Simulation:
    def __init__(self, sim_name = None, mesh = None, dimension = None, workflow = None, results = None):
        self.sim_name = sim_name
        self.mesh = mesh
        self.dimension = dimension
        self.workflow = workflow
        self.results = results

    def __str__(self):
        return ("\n--------SIMULATION PROPERTIES--------\nSimulation: {} {} {} {}\n".format(self.sim_name, self.mesh, self.dimension, self.workflow))

def param_extract(input_file):
    '''
    Extracts simulation parameters to instances of Simulation() and stores in list
    Str -> List

    '''
    all_sim_param = open(input_file, 'r')
    next(all_sim_param)
    line = all_sim_param.readline()

    output_list = []

    for line in all_sim_param:
        line = line.split(",")
        sim_mesh = Mesh_Properties(line[1], line[2])

        if (line[6] == "Y") or (line[6] == "y"):
            sim_dimensions = Dimension_Properties(line[4], line[5], line[7], line[8], line[9])
            CG_bool = True
        else:
            sim_dimensions = Dimension_Properties(line[4], line[5], 0, 0, 0)
            CG_bool = False

        if (line[10] == "Y") or (line[10] == "y"):
            post_bool = True
        else:
            post_bool = False

        if (line[11] == "Y") or (line[11] == "y"):
            streamlines_bool = True
        else:
            streamlines_bool = False

        sim_workflow = Workflow_Properties(line[3], CG_bool, post_bool, streamlines_bool, line[12])
        sim_param = Simulation(line[0], sim_mesh, sim_dimensions, sim_workflow)

        output_list.append(sim_param)

    all_sim_param.close

    return(output_list)

def initialize_project(input_file):
    all_sim_param = open(input_file, 'r')

    next(all_sim_param)
    line = all_sim_param.readline()
    line = line.split(",")
    # print(line)

    proj_name = line[14]
    proj_dir = line[15]
    print(proj_dir)
    proj_dir = proj_dir.replace(os.sep, '/')
    print(proj_dir)

    Save(FilePath=("{}/{}.wbpj", proj_dir, proj_name), Overwrite=True)

def results_dir(sim_list: list):
    for simulation in sim_list:
        results_dir_check(simulation.workflow.results_dir, simulation.workflow.post, simulation.workflow.streamlines)

def results_dir_check(path, post: bool, streamlines: bool):
    '''
    Str -> None

    Checks if path to results folder exists and creates parent and sub-folders if not
    '''
    if (os.path.exists(path) == False):
        os.mkdir(path)
    
    if post:
        media_dir = os.path.join(path, "Media Files")
        if (os.path.exists(media_dir) == False):
            os.mkdir(media_dir)
        media_subdir = ["\\3D Cp Contour", "\\Pressure Contour", "\\TKE Contour", "\\Wall Shear Streamline"]

        for subdir in media_subdir:
            if (os.path.exists(media_dir + subdir) == False):
                os.mkdir(media_dir + subdir)
        if streamlines:
            os.mkdir(media_dir + "\\Streamline Animations")
    return