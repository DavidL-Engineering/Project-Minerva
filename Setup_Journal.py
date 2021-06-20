# encoding: utf-8
# 2020 R1
SetScriptVersion(Version="20.1.164")

import os
import time
from datetime import date

class Mesh_Properties:
    '''
    Mesh_Properties object stores the name and directory of the exported .CAS file containing the mesh.

    Instance Variables
    ---------------------
    CAS_name : Name of .CAS file containing the mesh. Does not include file extension. [str]
    CAS_dir : Directory containing the .CAS file with the name as indicated in CAS_name. [str]
    '''
    
    def __init__(self, CAS_name = None, CAS_dir = None, body_size = None):
        '''Define instance variables.'''
        self.CAS_name = CAS_name
        self.CAS_dir = CAS_dir
        self.body_size = body_size
    
    def __str__(self):
        '''Print properties of Mesh_Properties object.'''
        return "\n----MESH PROPERTIES----\nCAS file: {}\nLocated in {}\nBody size: {}".format(self.CAS_name, self.CAS_dir, self.body_size)

class Dimension_Properties:
    '''
    Dimension_Properties object stores the dimensional properties of the object to be simulated.

    Instance Variables
    ---------------------
    area : Reference area of aerobody in m^2. Typically the surface area. [float]
    length : Reference length of aerobody in m. Typically the length in the x dimension. [float]
    CG_X : X-coordinate of aerobody center of gravity in m. [float]
    CG_Y : Y-coordinate of aerobody center of gravity in m. [float] 
    CG_Z : Z-coordinate of aerobody center of gravity in m. [float] 
    '''
    
    def __init__(self, area = None, length = None, CG_X = None, CG_Y = None, CG_Z = None):
        '''Define instance variables.'''
        self.area = area #Stored in m^2
        self.length = length #Stored in m
        self.CG_X = CG_X #Stored in m
        self.CG_Y = CG_Y #Stored in m
        self.CG_Z = CG_Z #Stored in m
    
    def __str__(self):
        '''Print properties of Dimension_Properties object.'''
        return "\n----DIMENSION PROPERTIES----\nArea is {}. Length is {}. Center of Gravity is ({}, {}, {})".format(self.area, self.length, self.CG_X, self.CG_Y, self.CG_Z)

class Workflow_Properties:
    '''
    Workflow_Properties object stores the simulation setup and post-processing parameters.

    Instance Variables
    ---------------------
    sol_method : Desired solution method. Either K-W or T-SST. [str]
    velocity : Inlet and road velocity. [float]
    cg : Specification of whether CG is entered and valid. [bool]
    post : Specification of whether post-processing is desired if simulation converges. [bool]
    streamlines : Specification of whether streamline animations are desired in post-processing. [bool]
    '''
    
    def __init__(self, sol_method = None, velocity = None, cg = None, post = None, streamlines = None):
        '''Define instance variables.'''
        self.sol_method = sol_method #Either K-W or T-SST
        self.velocity = velocity
        self.cg = cg #Either True or False
        self.post = post #Either True or False
        self.streamlines = streamlines #True or False

    def __str__(self):
        '''Print properties of Dimension_Properties object.'''
        return "\n----WORKFLOW PROPERTIES----\nSolution method: {}\nVelocity: {}\nCG: {}\nPost-Processing: {}\nStreamline Animations: {}".format(self.sol_method, self.velocity, self.cg, self.post, self.streamlines)

class Simulation_Results:
    '''
    Simulation_Results object stores the extracted numerical results of the FLUENT simulation.

    Instance Variables
    ---------------------
    convergence : Convergence status of completed simulation. [str]
    iterations : Number of iterations completed before convergence status reached. [int]
    drag_tot : Total drag force experienced in positive x direction in Newtons. [str]
    drag_comp : Pressure and viscous drag force components experienced in positive x direction in Newtons. [str]
    lift_tot : Total lift force experienced in positive z direction in Newtons. [str]
    lift_comp : Pressure and viscous lift force components experienced in positive z direction in Newtons. [str]
    f_left : Total aerodynamic force experienced in negative y direction in Newtons. [str]
    f_right : Total aerodynamic force experienced in positive y direction in Newtons. [str]
    mom_roll : Total aerodynamic moment experienced about x axis in Newton-metres. [str]
    mom_pitch : Total aerodynamic moment experienced about y axis in Newton-metres. [str]
    mom_yaw : Total aerodynamic moment experienced about z axis in Newton-metres. [str]
    '''
    
    def __init__(self, convergence = None, iterations = None, drag_tot = None, drag_comp = None, lift_tot = None, lift_comp = None, f_left = None, f_right = None, mom_roll = None, mom_pitch = None, mom_yaw = None, cop = None):
        '''Define instance variables.'''
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
        self.cop = cop

class Simulation:
    '''
    Simulation object contains all ANSYS module, mesh, 3D model, simulation workflow, and results processing parameters to be used in the course of CFD simulations in ANSYS Fluent and CFD-Post.

    Instance Variables
    ---------------------
    sim_name : Name of simulation. [str]
    mesh : Instance of Mesh_Properties object.
    dimension : Instance of Dimension_Properties object.
    workflow : Instance of Workflow_Properties object.
    results : Instance of Simulation_Results object.
    '''
    
    def __init__(self, sim_name = None, mesh = None, dimension = None, workflow = None, results = None):
        '''Define instance variables.'''
        self.sim_name = sim_name
        self.mesh = mesh
        self.dimension = dimension
        self.workflow = workflow
        self.results = results

    def __str__(self):
        '''Print properties of Simulation object.'''
        return ("\n--------SIMULATION PROPERTIES--------\nSimulation: {} {} {} {}\n".format(self.sim_name, self.mesh, self.dimension, self.workflow))

class Project:
    '''
    Project object contains governing parameters to be used in project.

    Instance Variables
    ---------------------
    proj_name : Name of ANSYS Workbench project. [str]
    proj_dir : Directory in which the ANSYS Workbench project should be stored. [str]
    results_dir : Directory in which the numerical and post-processing results should be stored. [str]
    processes : Number of processes to use during simulations. [int]
    '''

    def __init__(self, proj_name = None, proj_dir = None, results_dir = None, processes = None):
        '''Define instance variables.'''
        self.proj_name = proj_name
        self.proj_dir = proj_dir
        self.results_dir = results_dir
        self.processes = processes

    def __str__(self):
        '''Print properties of Project object'''
        return("\n--------PROJECT PROPERTIES--------\nProject name: {}\nProject directory: {}\nResults directory: {}\nProcesses: {}".format(self.proj_name, self.proj_dir, self.results_dir, self.processes))

def param_extract(input_file):
    '''
    Extracts simulation parameters from CSV of name indicated by input_file to instances of Simulation object and stores in list.
    Str -> List

    Parameters
    ---------------------
    input_file : string
        String containing name and file extension of CSV file with simulation parameters to be imported.

    Returns
    ---------------------
    output_list : list
        List containing instances of Simulation object generated from each line of CSV file.
    project_parameters : Project
        Instance of class Project generated from the CSV File.
    '''
    
    all_sim_param = open(input_file, 'r')
    next(all_sim_param)
    lines = all_sim_param.readlines()

    proj_param_input = lines[0].split(",")
    wb_proj_param = proj_param_extract(proj_param_input)

    output_list = []

    half_body = ["hb", "h-b", "half body", "half-body"]
    full_body = ["fb", "f-b", "full body", "full-body"]

    for line in lines:
        line = line.split(",")
        print(line)
        
        if (line[3].lower() in half_body):
          sim_mesh = Mesh_Properties(line[1], line[2], "HB")
        elif (line[3].lower() in full_body):
          sim_mesh = Mesh_Properties(line[1], line[2], "FB")

        if (line[8] == "Y") or (line[8] == "y"):
            sim_dimensions = Dimension_Properties(float(line[6]), float(line[7]), float(line[9]), float(line[10]), float(line[11]))
            CG_bool = True
        else:
            sim_dimensions = Dimension_Properties(float(line[6]), float(line[7]), 0, 0, 0)
            CG_bool = False

        if (line[12] == "Y") or (line[12] == "y"):
            post_bool = True
        else:
            post_bool = False

        if (line[13] == "Y") or (line[13] == "y"):
            streamlines_bool = True
        else:
            streamlines_bool = False
        
        if line[5] == "":
          velocity = 18.0
        else:
          velocity = float(line[5])

        sim_workflow = Workflow_Properties(line[4], velocity, CG_bool, post_bool, streamlines_bool)
        sim_param = Simulation(line[0], sim_mesh, sim_dimensions, sim_workflow, Simulation_Results())

        output_list.append(sim_param)

    all_sim_param.close

    return(output_list, wb_proj_param)

def proj_param_extract(line):
    '''
    Extracts global project parameters from list containing split string to instance of Project class.
    List -> Project (class)

    Parameters
    ---------------------
    line : List
        List containing strings with project parameters.

    Returns
    ---------------------
    proj_param : Project (class)
        Instance of Project class containing parameters of Workbench project.
    '''

    proj_param = Project(line[15], line[16], line[17], line[18])

    return(proj_param)

def initialize_project(project):
    '''
    Initializes ANSYS Workbench project.

    Parameters
    ---------------------
    project : Project object
        Instance of Project class containing project parameters.

    Returns
    ---------------------
    None
    '''
    proj_directory = project.proj_dir.replace(os.sep, '/')

    Save(
      FilePath="{}/{}.wbpj".format(proj_directory, project.proj_name),
      Overwrite=True)

    return

def results_dir(sim_list, proj_params):
    '''
    Runs results_dir_check on each simulation in a list of simulations.

    Parameters
    ---------------------
    sim_list : list
        List containing instances of Simulation object.
    proj_params : Project objects
        Instance of Project class containing project parameters.

    Returns
    ---------------------
    None
    '''
    
    for simulation in sim_list:
        results_dir_check(proj_params.results_dir, simulation.sim_name, simulation.workflow.post, simulation.workflow.streamlines, simulation.results.convergence)
    
    return

def results_dir_check(path, name, post, streamlines, status):
    '''
    Checks if path to results folder exists and creates parent and sub-folders for indicated results folder and post-processing folders.

    Parameters
    ---------------------
    path : str
        Path to results folder for simulation.
    post : bool
        Boolean variable indicating whether post-processing results are desired.
    streamlines : bool
        Boolean variable indicating whether streamline animations are desired.

    Returns
    ---------------------
    None
    '''
    
    if (os.path.exists(path) == False):
        os.mkdir(path)
    
    sim_path = os.path.join(path, name)

    if (status == "Converged"):
        if (os.path.exists(sim_path) == False):
            os.mkdir(sim_path)
            raw_results_dir = os.path.join(sim_path, "Raw Results")
            os.mkdir(raw_results_dir)
    
    if post:
        media_dir = os.path.join(sim_path, "Media Files")
        if (os.path.exists(media_dir) == False):
            os.mkdir(media_dir)
        media_subdir = ["\\3D Cp Contour", "\\Pressure Contour", "\\TKE Contour", "\\Wall Shear Streamline"]

        for subdir in media_subdir:
            if (os.path.exists(media_dir + subdir) == False):
                os.mkdir(media_dir + subdir)
        if streamlines:
            os.mkdir(media_dir + "\\Streamline Animations")
    return

def fluent_sim_setup(sim_list, processes):
    '''
    Checks solution method to be used and runs appropriate Fluent module setup.

    Parameters
    ---------------------
    sim_list : list
        List containing instances of Simulation object.

    Returns
    ---------------------
    None
    '''
    
    komega = ["komega", "k-omega", "k-w", "kw"]
    tsst = ["t-sst", "tsst"]

    # design_points = []

    for i in range(len(sim_list)):
        sim = sim_list[i]
        if sim.workflow.sol_method.lower() in komega:
            komega_setup(sim, processes)
        elif sim.workflow.sol_method.lower() in tsst:
            tsst_setup(sim, processes)
    
    
    Save(Overwrite=True)
    designPoint1 = Parameters.GetDesignPoint(Name="0")
    backgroundSession1 = UpdateAllDesignPoints(DesignPoints = [designPoint1])
    return

def komega_setup(simulation, processes):
    '''
    Performs setup of Fluent module with K-W solution method.

    Parameters
    ---------------------
    simulation : Simulation object
        Instance of Simulation object.
    processes : int
        Integer containing number of parallel processes to use in simulation.

    Returns
    ---------------------
    None
    '''
    
    template1 = GetTemplate(TemplateName="FLUENT")
    system1 = template1.CreateSystem()
    system1.DisplayText = simulation.sim_name
    setup1 = system1.GetContainer(ComponentName="Setup")
    fluentLauncherSettings1 = setup1.GetFluentLauncherSettings()
    fluentLauncherSettings1.SetEntityProperties(Properties=Set(Dimension="ThreeD", EnvPath={}, RunParallel=True, NumberOfProcessors=processes))
    setup1.Edit()
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"MenuBar*ImportSubMenu*Case...\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"{}/{}.cas\") \"All Case Files (*.cas* *.msh* *.MSH* )\")".format((simulation.mesh.CAS_dir.replace(os.sep, '/')), simulation.mesh.CAS_name))
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton1(Scale)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Scale Mesh*Table1*Table2(Scaling)*DropDownList2(Mesh Was Created In)\" '( 3))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*Table1*Table2(Scaling)*DropDownList2(Mesh Was Created In)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*Table1*Table2(Scaling)*PushButton4(Scale)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*PanelButtons*PushButton1(Close)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton3(Check)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton5(Report Quality)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (SST k-omega)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (SST k-omega)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (SST k-omega)"))(cx-gui-do cx-activate-item "Viscous Model*PanelButtons*PushButton1(OK)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Materials|Fluid|air\"))(cx-gui-do cx-set-real-entry-list \"Create/Edit Materials*RealEntry10\" '( 1.177))(cx-gui-do cx-set-real-entry-list \"Create/Edit Materials*RealEntry16\" '( 1.846e-05))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton3(Change/Create)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton1(Close)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Inlet|inlet (velocity-inlet, id=5)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Inlet|inlet (velocity-inlet, id=5)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|Inlet|inlet (velocity-inlet, id=5)\"))(cx-gui-do cx-set-list-selections \"Velocity Inlet*Frame3*Frame1(Momentum)*Table1*DropDownList6(Velocity Specification Method)\" '( 0))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Velocity Inlet*Frame3*Frame1(Momentum)*Table1*DropDownList6(Velocity Specification Method)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-expression-entry \"Velocity Inlet*Frame3*Frame1(Momentum)*Table1*Table8*ExpressionEntry1(Velocity Magnitude)\" '(\"{}\" . 0))(cx-gui-do cx-activate-item \"Velocity Inlet*PanelButtons*PushButton1(OK)\")".format(simulation.workflow.velocity))
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|road (wall, id=7)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|road (wall, id=7)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|Wall|road (wall, id=7)\"))(cx-gui-do cx-set-toggle-button2 \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*ToggleBox1(Wall Motion)*Moving Wall\" #t)(cx-gui-do cx-activate-item \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*ToggleBox1(Wall Motion)*Moving Wall\")(cx-gui-do cx-set-toggle-button2 \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table1*ToggleBox1*Absolute\" #t)(cx-gui-do cx-activate-item \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table1*ToggleBox1*Absolute\")(cx-gui-do cx-set-expression-entry \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table2*Table1*ExpressionEntry1(Speed)\" '(\"{}\" . 0))(cx-gui-do cx-activate-item \"Wall*PanelButtons*PushButton1(OK)\")".format(simulation.workflow.velocity))
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))(cx-gui-do cx-set-toggle-button2 "Wall*Frame3*Frame1(Momentum)*Table1*Frame2*Frame1*Table1*ToggleBox1(Shear Condition)*Specified Shear" #t)(cx-gui-do cx-activate-item "Wall*Frame3*Frame1(Momentum)*Table1*Frame2*Frame1*Table1*ToggleBox1(Shear Condition)*Specified Shear")(cx-gui-do cx-activate-item "Wall*PanelButtons*PushButton1(OK)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Frames"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Frames"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Frames"))(cx-gui-do cx-activate-item "Reference Frame*PanelButtons*PushButton2(Cancel)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Values"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Values"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Reference Values\"))(cx-gui-do cx-set-list-selections \"Reference Values*DropDownList1(Compute from)\" '( 3))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Reference Values*DropDownList1(Compute from)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Reference Values*Table2(Reference Values)*RealEntry1(Area)\" '({}))(cx-gui-do cx-activate-item \"Reference Values*Table2(Reference Values)*RealEntry1(Area)\")".format(simulation.dimension.area))
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Reference Values*Table2(Reference Values)*RealEntry5(Length)\" '({}))(cx-gui-do cx-activate-item \"Reference Values*Table2(Reference Values)*RealEntry5(Length)\")".format(simulation.dimension.length))
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Methods"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Methods"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Solution|Methods\"))(cx-gui-do cx-set-list-selections \"Solution Methods*Table1*Table2(Pressure-Velocity Coupling)*DropDownList2(Scheme)\" '( 3))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Methods*Table1*Table2(Pressure-Velocity Coupling)*DropDownList2(Scheme)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList2(Pressure)\" '( 1))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList2(Pressure)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-toggle-button2 "Solution Methods*Table1*CheckButton5(Pseudo Transient)" #t)(cx-gui-do cx-activate-item "Solution Methods*Table1*CheckButton5(Pseudo Transient)")(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*Force ReportSubMenu*Drag...")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-toggle-button2 "Drag Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force" #t)(cx-gui-do cx-activate-item "Drag Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force")(cx-gui-do cx-set-text-entry "Drag Report Definition*Table1*TextEntry3(Name)" "drag")(cx-gui-do cx-activate-item "Drag Report Definition*Table1*TextEntry3(Name)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Drag Report Definition*Table1*Table2*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table2*List2(Wall Zones)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\")(cx-gui-do cx-activate-item \"Drag Report Definition*PanelButtons*PushButton1(OK)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*Force ReportSubMenu*Lift...")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-text-entry "Lift Report Definition*Table1*TextEntry3(Name)" "lift")(cx-gui-do cx-activate-item "Lift Report Definition*Table1*TextEntry3(Name)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\")(cx-gui-do cx-set-list-selections \"Lift Report Definition*Table1*Table2*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table2*List2(Wall Zones)\")(cx-gui-do cx-set-real-entry-list \"Lift Report Definition*Table1*Table1*Table2(Force Vector)*RealEntry2(Y)\" '( 0))(cx-gui-do cx-set-real-entry-list \"Lift Report Definition*Table1*Table1*Table2(Force Vector)*RealEntry3(Z)\" '( 1))(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\")(cx-gui-do cx-activate-item \"Report Definitions*PanelButtons*PushButton1(Close)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Lift Report Definition*PanelButtons*PushButton1(OK)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Solution|Run Calculation\"))(cx-gui-do cx-set-list-selections \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table1*DropDownList2(Length Scale Method)\" '( 2))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table1*DropDownList2(Length Scale Method)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table3*RealEntry3(Length Scale)\" '( {}))(cx-gui-do cx-activate-item \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table3*RealEntry3(Length Scale)\")".format(simulation.dimension.length))
    setup1.SendCommand(Command='(cx-gui-do cx-set-integer-entry "Run Calculation*Table1*Table3(Parameters)*Table1*Table1*IntegerEntry1(Number of Iterations)" 600)(cx-gui-do cx-activate-item "Run Calculation*Table1*Table3(Parameters)*Table1*Table1*IntegerEntry1(Number of Iterations)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Initialization*Table1*Frame11*PushButton2(Initialize)")')
    setup1.SendCommand(Command="/mesh/repair-improve/allow-repair-at-boundaries yes")
    setup1.SendCommand(Command="/mesh/repair-improve/include-local-polyhedra-conversion-in-repair yes")
    setup1.SendCommand(Command="/mesh/repair-improve/repair")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*FileMenu*Close Fluent")')
    Save(Overwrite=True)

    return

def tsst_setup(simulation, processes):
    '''
    Performs setup of Fluent module with T-SST solution method.

    Parameters
    ---------------------
    simulation : Simulation object
        Instance of Simulation object.
    processes : int
        Integer containing number of parallel processes to use in simulation.

    Returns
    ---------------------
    None
    '''
    
    template1 = GetTemplate(TemplateName="FLUENT")
    system1 = template1.CreateSystem()
    system1.DisplayText = simulation.sim_name
    setup1 = system1.GetContainer(ComponentName="Setup")
    fluentLauncherSettings1 = setup1.GetFluentLauncherSettings()
    fluentLauncherSettings1.SetEntityProperties(Properties=Set(Dimension="ThreeD", EnvPath={}, RunParallel=True, NumberOfProcessors=processes))
    setup1.Edit()
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"MenuBar*ImportSubMenu*Case...\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"{}/{}.cas\") \"All Case Files (*.cas* *.msh* *.MSH* )\")".format((simulation.mesh.CAS_dir.replace(os.sep, '/')), simulation.mesh.CAS_name))
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton1(Scale)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Scale Mesh*Table1*Table2(Scaling)*DropDownList2(Mesh Was Created In)\" '( 3))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*Table1*Table2(Scaling)*DropDownList2(Mesh Was Created In)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*Table1*Table2(Scaling)*PushButton4(Scale)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*PanelButtons*PushButton1(Close)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton3(Check)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton5(Report Quality)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (SST k-omega)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (SST k-omega)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (SST k-omega)"))(cx-gui-do cx-set-toggle-button2 "Viscous Model*Table1*ToggleBox1(Model)*Transition SST (4 eqn)" #t)(cx-gui-do cx-activate-item "Viscous Model*Table1*ToggleBox1(Model)*Transition SST (4 eqn)")(cx-gui-do cx-activate-item "Viscous Model*PanelButtons*PushButton1(OK)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (Transition SST (4 eqn))"))(cx-gui-do cx-activate-item "Viscous Model*PanelButtons*PushButton1(OK)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Materials|Fluid|air\"))(cx-gui-do cx-set-real-entry-list \"Create/Edit Materials*RealEntry10\" '( 1.177))(cx-gui-do cx-set-real-entry-list \"Create/Edit Materials*RealEntry16\" '( 1.846e-05))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton3(Change/Create)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton1(Close)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Inlet|inlet (velocity-inlet, id=5)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Inlet|inlet (velocity-inlet, id=5)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|Inlet|inlet (velocity-inlet, id=5)\"))(cx-gui-do cx-set-list-selections \"Velocity Inlet*Frame3*Frame1(Momentum)*Table1*DropDownList6(Velocity Specification Method)\" '( 0))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Velocity Inlet*Frame3*Frame1(Momentum)*Table1*DropDownList6(Velocity Specification Method)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-expression-entry \"Velocity Inlet*Frame3*Frame1(Momentum)*Table1*Table8*ExpressionEntry1(Velocity Magnitude)\" '(\"{}\" . 0))(cx-gui-do cx-activate-item \"Velocity Inlet*PanelButtons*PushButton1(OK)\")".format(simulation.workflow.velocity))
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|road (wall, id=7)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|road (wall, id=7)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|Wall|road (wall, id=7)\"))(cx-gui-do cx-set-toggle-button2 \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*ToggleBox1(Wall Motion)*Moving Wall\" #t)(cx-gui-do cx-activate-item \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*ToggleBox1(Wall Motion)*Moving Wall\")(cx-gui-do cx-set-toggle-button2 \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table1*ToggleBox1*Absolute\" #t)(cx-gui-do cx-activate-item \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table1*ToggleBox1*Absolute\")(cx-gui-do cx-set-expression-entry \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table2*Table1*ExpressionEntry1(Speed)\" '(\"{}\" . 0))(cx-gui-do cx-activate-item \"Wall*PanelButtons*PushButton1(OK)\")".format(simulation.workflow.velocity))
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))(cx-gui-do cx-set-toggle-button2 "Wall*Frame3*Frame1(Momentum)*Table1*Frame2*Frame1*Table1*ToggleBox1(Shear Condition)*Specified Shear" #t)(cx-gui-do cx-activate-item "Wall*Frame3*Frame1(Momentum)*Table1*Frame2*Frame1*Table1*ToggleBox1(Shear Condition)*Specified Shear")(cx-gui-do cx-activate-item "Wall*PanelButtons*PushButton1(OK)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Frames"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Frames"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Frames"))(cx-gui-do cx-activate-item "Reference Frame*PanelButtons*PushButton2(Cancel)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Values"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Values"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Reference Values\"))(cx-gui-do cx-set-list-selections \"Reference Values*DropDownList1(Compute from)\" '( 3))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Reference Values*DropDownList1(Compute from)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Reference Values*Table2(Reference Values)*RealEntry1(Area)\" '({}))(cx-gui-do cx-activate-item \"Reference Values*Table2(Reference Values)*RealEntry1(Area)\")".format(simulation.dimension.area))
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Reference Values*Table2(Reference Values)*RealEntry5(Length)\" '({}))(cx-gui-do cx-activate-item \"Reference Values*Table2(Reference Values)*RealEntry5(Length)\")".format(simulation.dimension.length))
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Methods"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Methods"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Solution|Methods\"))(cx-gui-do cx-set-list-selections \"Solution Methods*Table1*Table2(Pressure-Velocity Coupling)*DropDownList2(Scheme)\" '( 3))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Methods*Table1*Table2(Pressure-Velocity Coupling)*DropDownList2(Scheme)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList2(Pressure)\" '( 1))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList2(Pressure)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-toggle-button2 "Solution Methods*Table1*CheckButton5(Pseudo Transient)" #t)(cx-gui-do cx-activate-item "Solution Methods*Table1*CheckButton5(Pseudo Transient)")(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*Force ReportSubMenu*Drag...")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-toggle-button2 "Drag Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force" #t)(cx-gui-do cx-activate-item "Drag Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force")(cx-gui-do cx-set-text-entry "Drag Report Definition*Table1*TextEntry3(Name)" "drag")(cx-gui-do cx-activate-item "Drag Report Definition*Table1*TextEntry3(Name)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Drag Report Definition*Table1*Table2*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table2*List2(Wall Zones)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\")(cx-gui-do cx-activate-item \"Drag Report Definition*PanelButtons*PushButton1(OK)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*Force ReportSubMenu*Lift...")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-text-entry "Lift Report Definition*Table1*TextEntry3(Name)" "lift")(cx-gui-do cx-activate-item "Lift Report Definition*Table1*TextEntry3(Name)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\")(cx-gui-do cx-set-list-selections \"Lift Report Definition*Table1*Table2*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table2*List2(Wall Zones)\")(cx-gui-do cx-set-real-entry-list \"Lift Report Definition*Table1*Table1*Table2(Force Vector)*RealEntry2(Y)\" '( 0))(cx-gui-do cx-set-real-entry-list \"Lift Report Definition*Table1*Table1*Table2(Force Vector)*RealEntry3(Z)\" '( 1))(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\")(cx-gui-do cx-activate-item \"Report Definitions*PanelButtons*PushButton1(Close)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Lift Report Definition*PanelButtons*PushButton1(OK)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Solution|Run Calculation\"))(cx-gui-do cx-set-list-selections \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table1*DropDownList2(Length Scale Method)\" '( 2))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table1*DropDownList2(Length Scale Method)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table3*RealEntry3(Length Scale)\" '( {}))(cx-gui-do cx-activate-item \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table3*RealEntry3(Length Scale)\")".format(simulation.dimension.length))
    setup1.SendCommand(Command='(cx-gui-do cx-set-integer-entry "Run Calculation*Table1*Table3(Parameters)*Table1*Table1*IntegerEntry1(Number of Iterations)" 600)(cx-gui-do cx-activate-item "Run Calculation*Table1*Table3(Parameters)*Table1*Table1*IntegerEntry1(Number of Iterations)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Initialization*Table1*Frame11*PushButton2(Initialize)")')
    setup1.SendCommand(Command="/mesh/repair-improve/allow-repair-at-boundaries yes")
    setup1.SendCommand(Command="/mesh/repair-improve/include-local-polyhedra-conversion-in-repair yes")
    setup1.SendCommand(Command="/mesh/repair-improve/repair")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*FileMenu*Close Fluent")')
    Save(Overwrite=True)

    return

def completion_status(sim_list, proj_params):
    '''
    Detects if entire workbench project has finished running simulations.

    Parameters
    ---------------------
    sim_list : List 
        List containing Simulation objects.
    proj_params : Project object
        Instance of Project class containing project parameters.

    Returns
    ---------------------
    None
    '''

    wb_files_dir = os.path.join(proj_params.proj_dir, proj_params.proj_name + "_files")

    last_sim_index = len(sim_list)-1

    complete = 0

    if last_sim_index == 0:
        flu_dir = "FLU"
    else:
        flu_dir = "FLU-{}".format(last_sim_index)

    last_sim_dir = "{}\\progress_files\\dp0\\{}\\Fluent\\Solution.trn".format(wb_files_dir, flu_dir)
    while complete == 0:
        if os.path.isfile(last_sim_dir):
            complete = 1
        else:
            time.sleep(60)
    
    return

def convergence_status(sim_list, proj_params):
    '''
    Performs batch detection of convergence status on all simulations in sim_list.

    Parameters
    ---------------------
    sim_list : List 
        List containing Simulation objects.
    proj_params : Project object
        Instance of Project class containing project parameters.

    Returns
    ---------------------
    sim_list : List 
        List containing Simulation objects.
    '''
    
    wb_files_dir = os.path.join(proj_params.proj_dir, proj_params.proj_name + "_files").replace(os.sep, '/')

    for i in range(len(sim_list)):
        if i==0:
            flu_dir = "FLU"
        else:
            flu_dir = "FLU-{}".format(i)
        status_file = open("{}/progress_files/dp0/{}/Fluent/Solution.trn".format(wb_files_dir, flu_dir), 'r')
        if "solution is converged" in status_file.read():
            sim_list[i].results.convergence = "Converged"
        else:
            sim_list[i].results.convergence = "Diverged or Error"
    
    return(sim_list)

def results_extract(sim_list, proj_params):
    '''
    Performs batch execution of fluent_results_export on simulations that have converged.

    Parameters
    ---------------------
    sim_list : List 
        List containing Simulation objects.
    proj_params : Project object
        Instance of Project class containing project parameters.

    Returns
    ---------------------
    None
    '''
    for i in range(len(sim_list)):
        if sim_list[i].results.convergence == "Converged":
            fluent_results_export(sim_list[i], i, proj_params)
            sim_list[i] = fluent_results_aggregator(sim_list[i], i, proj_params)
    
    results_formatter(sim_list, proj_params)

    return

def fluent_results_export(simulation, index, proj_params):
    '''
    Exports results from a given Fluent simulation into .txt files.

    Parameters
    ---------------------
    simulation : Simulation object
        Instance of Simulation object.
    index : int
        Integer of current index of converged simulation.
    proj_params : Project object
        Instance of Project class containing project parameters.

    Returns
    ---------------------
    None
    '''

    if index==0:
        module = "FLU"
        flu_dir = "FLU"
    else:
        module = "FLU {}".format(index)
        flu_dir = "FLU-{}".format(index)
    
    raw_results_dir = os.path.join(proj_params.results_dir, simulation.sim_name + "\\Raw Results").replace(os.sep, '/')
    wb_files_dir = os.path.join(proj_params.proj_dir, proj_params.proj_name + "_files").replace(os.sep, '/')
    
    system1 = GetSystem(Name=module)
    solution1 = system1.GetContainer(ComponentName="Solution")
    solution1.Edit()
    setup1 = system1.GetContainer(ComponentName="Setup")
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Results|Reports|Forces"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Results|Reports|Forces"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Results|Reports|Forces\"))(cx-gui-do cx-set-list-selections \"Force Reports*List2(Wall Zones)\" '( 0 2))(cx-gui-do cx-activate-item \"Force Reports*List2(Wall Zones)\")(cx-gui-do cx-set-list-selections \"Force Reports*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Force Reports*List2(Wall Zones)\")")
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"{}/drag{}.txt\") \"All Files (*)\")".format(raw_results_dir, index))
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame1(Direction Vector)*RealEntry1(X)\" '( 0))(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame1(Direction Vector)*RealEntry3(Z)\" '( 1))")
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"lift{}.txt\") \"All Files (*)\")".format(index))
    setup1.SendCommand(Command="(cx-gui-do cx-set-toggle-button2 \"Force Reports*Table1*ToggleBox1(Options)*Moments\" #t)(cx-gui-do cx-activate-item \"Force Reports*Table1*ToggleBox1(Options)*Moments\")(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame2(Moment Center)*RealEntry1(X)\" '({}))(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame2(Moment Center)*RealEntry2(Y)\" '({}))(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame2(Moment Center)*RealEntry3(Z)\" '({}))".format(simulation.dimension.CG_X, simulation.dimension.CG_Y, simulation.dimension.CG_Z))
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"roll_moment{}.txt\") \"All Files (*)\")".format(index))
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame3(Moment Axis)*RealEntry1(X)\" '( 0))(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame3(Moment Axis)*RealEntry2(Y)\" '( 1))")
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"pitch_moment{}.txt\") \"All Files (*)\")".format(index))
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame3(Moment Axis)*RealEntry2(Y)\" '( 0))(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame3(Moment Axis)*RealEntry3(Z)\" '( 1))")
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"yaw_moment{}.txt\") \"All Files (*)\")".format(index))
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame3(Moment Axis)*RealEntry3(Z)\" '( 0))(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame3(Moment Axis)*RealEntry1(X)\" '( 1))(cx-gui-do cx-set-toggle-button2 \"Force Reports*Table1*ToggleBox1(Options)*Forces\" #t)(cx-gui-do cx-activate-item \"Force Reports*Table1*ToggleBox1(Options)*Forces\")(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame1(Direction Vector)*RealEntry3(Z)\" '( 0))(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame1(Direction Vector)*RealEntry2(Y)\" '( -1))")
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"force_left{}.txt\") \"All Files (*)\")".format(index))
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame1(Direction Vector)*RealEntry2(Y)\" '( 1))")
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"force_right{}.txt\") \"All Files (*)\")".format(index))
    setup1.SendCommand(Command='(cx-gui-do cx-set-toggle-button2 "Force Reports*Table1*ToggleBox1(Options)*Center of Pressure" #t)(cx-gui-do cx-activate-item "Force Reports*Table1*ToggleBox1(Options)*Center of Pressure")')
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"cp_x_0m_{}.txt\") \"All Files (*)\")".format(index))
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Force Reports*PanelButtons*PushButton2(Cancel)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*FileMenu*Close Fluent")')
    
    
    iter_file = open("{}/dp0/{}/Fluent/drag-rfile.out".format(wb_files_dir, flu_dir), 'r')
    iter_lines = iter_file.readlines()
    iter_data = iter_lines[len(iter_lines)-1]
    

    output = open("{}/iter{}.txt".format(raw_results_dir, index), 'w')
    output.write(iter_data)
    output.close()
    iter_file.close()

    return

def fluent_results_aggregator(simulation, index, proj_params):
    '''
    Aggregates exported fluent results and imports into their Simulation_Results object.

    Parameters
    ---------------------
    simulation : Simulation object
        Instance of Simulation object.
    index : int
        Integer of current index of converged simulation.
    proj_params : Project object
        Instance of Project class containing project parameters.

    Returns
    ---------------------
    simulation : Simulation object
        Instance of Simulation object.
    '''

    raw_results_dir = os.path.join(proj_params.results_dir, simulation.sim_name + "\\Raw Results").replace(os.sep, '/')

    cop_file = open("{}/cp_x_0m_{}.txt".format(raw_results_dir, index), 'r')
    drag_file = open("{}/drag{}.txt".format(raw_results_dir, index), 'r')
    lift_file = open("{}/lift{}.txt".format(raw_results_dir, index), 'r')
    iter_file = open("{}/iter{}.txt".format(raw_results_dir, index), 'r')
    f_left_file = open("{}/force_left{}.txt".format(raw_results_dir, index), 'r')
    f_right_file = open("{}/force_right{}.txt".format(raw_results_dir, index), 'r')
    pitch_file = open("{}/pitch_moment{}.txt".format(raw_results_dir, index), 'r')
    roll_file = open("{}/roll_moment{}.txt".format(raw_results_dir, index), 'r')
    yaw_file = open("{}/yaw_moment{}.txt".format(raw_results_dir, index), 'r')

    cop_all_data = cop_file.readlines()
    drag_all_data = drag_file.readlines()
    lift_all_data = lift_file.readlines()
    iter_all_data = iter_file.readlines()
    f_left_all_data = f_left_file.readlines()
    f_right_all_data = f_right_file.readlines()
    pitch_all_data = pitch_file.readlines()
    roll_all_data = roll_file.readlines()
    yaw_all_data = yaw_file.readlines()

    # cop values are on line 5
    # drag values are on line 13
    # lift values are on line 13
    # iter values are on line 1
    # f_left values are on line 13
    # f_right values are on line 13
    # pitch moment values are on line 13
    # roll moment values are on line 13
    # yaw moment values are on line 13

    cop_line_data = cop_all_data[4].split()
    drag_line_data = drag_all_data[12].split()
    lift_line_data = lift_all_data[12].split()
    iter_line_data = iter_all_data[0].split()
    f_left_line_data = f_left_all_data[12].split()
    f_right_line_data = f_right_all_data[12].split()
    pitch_line_data = pitch_all_data[12].split()
    roll_line_data = roll_all_data[12].split()
    yaw_line_data = yaw_all_data[12].split()

    cop_values = str(cop_line_data[1]) + " " + str(cop_line_data[2])
    drag_comp_values = str(drag_line_data[1]) + " " + str(drag_line_data[2])
    drag_tot_value = str(drag_line_data[3])
    lift_comp_values = str(lift_line_data[1] + " " + lift_line_data[2])
    lift_tot_value = str(lift_line_data[3])
    iter_value = str(iter_line_data[0])
    f_left_value = str(f_left_line_data[3])
    f_right_value = str(f_right_line_data[3])
    pitch_value = str(pitch_line_data[3])
    roll_value = str(roll_line_data[3])
    yaw_value =str(yaw_line_data[3])

    simulation.results.iterations = iter_value
    simulation.results.drag_tot = drag_tot_value
    simulation.results.drag_comp = drag_comp_values
    simulation.results.lift_tot = lift_tot_value
    simulation.results.lift_comp = lift_comp_values
    simulation.results.f_left = f_left_value
    simulation.results.f_right = f_right_value

    if simulation.workflow.cg == True:
      simulation.results.mom_roll = roll_value
      simulation.results.mom_pitch = pitch_value
      simulation.results.mom_yaw = yaw_value
    else:
      simulation.results.mom_roll = 0
      simulation.results.mom_pitch = 0
      simulation.results.mom_yaw = 0
    simulation.results.cop = cop_values

    return(simulation)

def results_formatter(sim_list, proj_params):
    export_directory = proj_params.results_dir.replace(os.sep, '/')

    current_date = date.today().strftime("%d/%m/%Y")

    with open("{}/{} Simulation Results.csv".format(export_directory, proj_params.proj_name), 'w') as csvfile:
        csvfile.write('Simulation Name,.CAS File Name,Date,Number of Iterations,A. Drag [N] (Total),B. Drag [N]: Pressure + Viscous,A. Lift [N] (Total),B. Lift [N]: Pressure + Viscous,Force Left [N] (Total),Force Right [N] (Total),"Roll Moment [N-m] (axis = [1,0,0])","Pitch Moment [N-m] (axis = [0,1,0])","Yaw Moment [N-m] (axis = [0,0,1])",Center of Pressure (x=0 [m]),Status\n')
        for i in range(len(sim_list)):
            simulation = sim_list[i]
            if simulation.results.convergence == "Converged":
                csvfile.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(simulation.sim_name, simulation.mesh.CAS_name, current_date, simulation.results.iterations, simulation.results.drag_tot, simulation.results.drag_comp, simulation.results.lift_tot, simulation.results.lift_comp, simulation.results.f_left, simulation.results.f_right, simulation.results.mom_roll, simulation.results.mom_pitch, simulation.results.mom_yaw, simulation.results.cop, simulation.results.convergence))
            else:
                csvfile.write("{},{},{},,,,,,,,,,,,{}\n".format(simulation.sim_name, simulation.mesh.CAS_name, current_date, simulation.results.convergence))
        csvfile.close()

    return

def post_processing(sim_list, proj_params):
    stream = []

    for i in range(len(sim_list)):
        if sim_list[i].workflow.post == True:
            post_plots(sim_list[i], i, proj_params)
            if sim_list[i].workflow.streamlines == True:
                stream.append(i)

    for j in range(len(stream)):
      simulation = sim_list[stream[j]]
      if simulation.mesh.body_size == "FB":
        post_streamlines_fb(simulation, j, proj_params)
      if simulation.mesh.body_size == "HB":
        post_streamlines_hb(simulation, j, proj_params)

    return

def post_plots(simulation, index, proj_params):
    sim_path = os.path.join(proj_params.results_dir, simulation.sim_name)
    media_dir = os.path.join(sim_path, "Media Files")
    cp_dir = os.path.join(media_dir, "\\3D Cp Contour").replace(os.sep, '/')
    pressure_dir = os.path.join(media_dir, "\\Pressure Contour").replace(os.sep, '/')
    tke_dir = os.path.join(media_dir, "\\TKE Contour").replace(os.sep, '/')
    wallshear_dir = os.path.join(media_dir, "\\Wall Shear Streamline").replace(os.sep, '/')
    
    
    if index == 0:
        module = "FLU"
    else:
        module = "FLU {}".format(index)

    template1 = GetTemplate(TemplateName="Results")
    system1 = GetSystem(Name=module)
    system2 = template1.CreateSystem(
        Position="Right",
        RelativeTo=system1)
    solutionComponent1 = system1.GetComponent(Name="Solution")
    resultsComponent1 = system2.GetComponent(Name="Results")
    solutionComponent1.TransferData(TargetComponent=resultsComponent1)
    results1 = system2.GetContainer(ComponentName="Results")
    results1.Edit()
    results1.SendCommand(Command="""VIEW:View 1
      Light Angle = 50, 110
    END

    VIEW:View 2
      Light Angle = 50, 110
    END

    VIEW:View 3
      Light Angle = 50, 110
    END

    VIEW:View 4
      Light Angle = 50, 110
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /DATA READER/CASE:Case {}/BOUNDARY:car, view=/VIEW:View 1""".format(simulation.sim_name))
    results1.SendCommand(Command="> autolegend plot=/CONTOUR:TKE Contour, view=VIEW:View 1")
    results1.SendCommand(Command="""CONTOUR:TKE Contour
    Apply Instancing Transform = On
    Clip Contour = Off
    Colour Map = Default Colour Map
    Colour Scale = Logarithmic
    Colour Variable = Turbulence Kinetic Energy
    Colour Variable Boundary Values = Conservative
    Constant Contour Colour = Off
    Contour Range = Global
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Contours = Off
    Font = Sans Serif
    Fringe Fill = On
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Location List = car
    Max = 0.0 [m^2 s^-2]
    Min = 0.0 [m^2 s^-2]
    Number of Contours = 5000
    Show Numbers = Off
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Text Colour = 0, 0, 0
    Text Colour Mode = Default
    Text Height = 0.024
    Transparency = 0.0
    Use Face Values = On
    Value List = 0 [m^2 s^-2],1 [m^2 s^-2]
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/CONTOUR:Pressure Contour, view=VIEW:View 1")
    results1.SendCommand(Command="""CONTOUR:Pressure Contour
    Apply Instancing Transform = On
    Clip Contour = Off
    Colour Map = Default Colour Map
    Colour Scale = Linear
    Colour Variable = Pressure
    Colour Variable Boundary Values = Conservative
    Constant Contour Colour = Off
    Contour Range = Global
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Contours = Off
    Font = Sans Serif
    Fringe Fill = On
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Location List = car
    Max = 0.0 [Pa]
    Min = 0.0 [Pa]
    Number of Contours = 5000
    Show Numbers = Off
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Text Colour = 0, 0, 0
    Text Colour Mode = Default
    Text Height = 0.024
    Transparency = 0.0
    Use Face Values = On
    Value List = 0 [Pa],1 [Pa]
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Wall Shear Streamline, view=VIEW:View 1")
    results1.SendCommand(Command="""STREAMLINE:Wall Shear Streamline
    Absolute Tolerance = 0.0 [m]
    Apply Instancing Transform = On
    Colour = 0, 0, 1
    Colour Map = Default Colour Map
    Colour Mode = Constant
    Colour Scale = Linear
    Colour Variable = Wall Shear
    Colour Variable Boundary Values = Conservative
    Cross Periodics = On
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Draw Streams = On
    Draw Symbols = Off
    Grid Tolerance = 0.01
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Width = 1
    Location List = car
    Locator Sampling Method = Equally Spaced
    Max = 0.0 [Pa]
    Maximum Number of Items = 25
    Min = 0.0 [Pa]
    Number of Samples = 500
    Number of Sides = 8
    Range = Global
    Reduction Factor = 1.0
    Reduction or Max Number = Max Number
    Sample Spacing = 0.1
    Sampling Aspect Ratio = 1
    Sampling Grid Angle = 0 [degree]
    Seed Point Type = Equally Spaced Samples
    Simplify Geometry = Off
    Specular Lighting = On
    Stream Drawing Mode = Line
    Stream Initial Direction = 0 , 0 , 0 
    Stream Size = 1.0
    Stream Symbol = Ball
    Streamline Direction = Forward
    Streamline Maximum Periods = 20
    Streamline Maximum Segments = 10000
    Streamline Maximum Time = 0.0 [s]
    Streamline Type = Surface Streamline
    Streamline Width = 2
    Surface Drawing = Smooth Shading
    Surface Streamline Direction = Forward and Backward
    Symbol Size = 1.0
    Symbol Start Time = 10.0 [s]
    Symbol Stop Time = -10.0 [s]
    Symbol Time Interval = 1.0 [s]
    Tolerance Mode = Grid Relative
    Transparency = 0.0
    Variable = Wall Shear
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""LIBRARY:
      CEL:
        EXPRESSIONS:
          Cp Expr = (Pressure - Reference Pressure ) / (0.5 * areaAve(Density)@inlet * areaAve(Velocity)@inlet^2)
        END
      END
    END

    EXPRESSION EVALUATOR:
      Evaluated Expression = Cp Expr
    END

    > forceupdate EXPRESSION EVALUATOR""")
    results1.SendCommand(Command="""USER SCALAR VARIABLE:Cp Var
    Boundary Values = Conservative
    Calculate Global Range = On
    Expression = Cp Expr
    Recipe = Expression
    Variable to Copy = Pressure
    Variable to Gradient = Pressure
    END""")
    results1.SendCommand(Command="> autolegend plot=/CONTOUR:Cp Contour, view=VIEW:View 1")
    results1.SendCommand(Command="""CONTOUR:Cp Contour
    Apply Instancing Transform = On
    Clip Contour = Off
    Colour Map = Default Colour Map
    Colour Scale = Linear
    Colour Variable = Cp Var
    Colour Variable Boundary Values = Conservative
    Constant Contour Colour = Off
    Contour Range = Local
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Contours = Off
    Font = Sans Serif
    Fringe Fill = On
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Location List = car
    Max = 0.0
    Min = 0.0
    Number of Contours = 5000
    Show Numbers = Off
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Text Colour = 0, 0, 0
    Text Colour Mode = Default
    Text Height = 0.024
    Transparency = 0.0
    Use Face Values = On
    Value List = 0,1
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/ISOSURFACE:Y 0 Plane, view=VIEW:View 1")
    results1.SendCommand(Command="""ISOSURFACE:Y 0 Plane
    Apply Instancing Transform = On
    Apply Texture = Off
    Blend Texture = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Use Plot Variable
    Colour Scale = Linear
    Colour Variable = Y
    Colour Variable Boundary Values = Conservative
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Max = 0.0 [m]
    Min = 0.0 [m]
    Range = Global
    Render Edge Angle = 0 [degree]
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Texture Angle = 0
    Texture Direction = 0 , 1 , 0 
    Texture File =  
    Texture Material = Metal
    Texture Position = 0 , 0 
    Texture Scale = 1
    Texture Type = Predefined
    Tile Texture = Off
    Transform Texture = Off
    Transparency = 0.0
    Value = 0.0 [m]
    Variable = Y
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /ISOSURFACE:Y 0 Plane, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /ISOSURFACE:Y 0 Plane, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/POLYLINE:Centerline Polyline, view=VIEW:View 1")
    results1.SendCommand(Command="""POLYLINE:Centerline Polyline
    Apply Instancing Transform = On
    Boundary List = car
    Colour = 0, 1, 0
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Cp Var
    Colour Variable Boundary Values = Conservative
    Contour Level = 1
    Domain List = /DOMAIN GROUP:All Domains
    Input File =  
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Line Width = 15
    Location = /ISOSURFACE:Y 0 Plane
    Max = 0.0
    Min = 0.0
    Option = Boundary Intersection
    Range = Global
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""CHART:Cp vs X Coord
    Chart Axes Font = Tahoma, 10, False, False, False, False
    Chart Axes Titles Font = Tahoma, 10, True, False, False, False
    Chart Grid Line Width = 1
    Chart Horizontal Grid = On
    Chart Legend = On
    Chart Legend Font = Tahoma, 8, False, False, False, False
    Chart Legend Inside = Outside Chart
    Chart Legend Justification = Center
    Chart Legend Position = Bottom
    Chart Legend Width Height = 0.2 , 0.4 
    Chart Legend X Justification = Right
    Chart Legend XY Position = 0.73 , 0.275 
    Chart Legend Y Justification = Center
    Chart Line Width = 2
    Chart Lines Order = Series 1,Chart Line 1
    Chart Minor Grid = Off
    Chart Minor Grid Line Width = 1
    Chart Symbol Size = 4
    Chart Title = Cp vs X Coordinate
    Chart Title Font = Tahoma, 12, True, False, False, False
    Chart Title Visibility = On
    Chart Type = XY
    Chart Vertical Grid = On
    Chart X Axis Automatic Number Formatting = On
    Chart X Axis Label = X Axis <units>
    Chart X Axis Number Format = %10.3e
    Chart Y Axis Automatic Number Formatting = On
    Chart Y Axis Label = Y Axis <units>
    Chart Y Axis Number Format = %10.3e
    Default Chart X Variable = X
    Default Chart Y Variable = Cp Var
    Default Difference Line Calculation = From Points
    Default Histogram Y Axis Weighting = None
    Default Time Chart Variable = Pressure
    Default Time Chart X Expression = Time
    Default Time Variable Absolute Value = Off
    Default Time Variable Boundary Values = Conservative
    Default X Variable Absolute Value = Off
    Default X Variable Boundary Values = Conservative
    Default Y Variable Absolute Value = Off
    Default Y Variable Boundary Values = Conservative
    FFT Full Input Range = On
    FFT Max = 0.0
    FFT Min = 0.0
    FFT Subtract Mean = Off
    FFT Window Type = Hanning
    FFT X Function = Frequency
    FFT Y Function = Power Spectral Density
    Histogram Automatic Divisions = Automatic
    Histogram Divisions = -1.0,1.0
    Histogram Divisions Count = 10
    Histogram Y Axis Value = Count
    Is FFT Chart = Off
    Max X = 1.0
    Max Y = 1.0
    Min X = -1.0
    Min Y = -1.0
    Use Data For X Axis Labels = On
    Use Data For Y Axis Labels = On
    X Axis Automatic Range = On
    X Axis Inverted = Off
    X Axis Logarithmic Scaling = Off
    Y Axis Automatic Range = On
    Y Axis Inverted = Off
    Y Axis Logarithmic Scaling = Off
      CHART SERIES:Series 1
      Chart Line Custom Data Selection = Off
      Chart Line Filename =  
      Chart Series Type = Regular
      Location = /POLYLINE:Centerline Polyline
      Monitor Data Filename =  
      Monitor Data Source = Case
      Monitor Data X Variable Absolute Value = Off
      Monitor Data Y Variable Absolute Value = Off
      Operating Point Data Case = Case {}
      Operating Point Data Filename =  
      Operating Point Data Source = File
      Series Name = Series 1
      Time Chart Expression = Time
      Time Chart Type = Point
        CHART LINE:Chart Line 1
        Auto Chart Line Colour = On
        Auto Chart Symbol Colour = On
        Chart FFT Line Type = Bars
        Chart Line Colour = 1.0, 0.0, 0.0
        Chart Line Style = Automatic
        Chart Line Type = Lines
        Chart Line Visibility = On
        Chart Symbol Colour = 0.0, 1.0, 0.0
        Chart Symbol Style = Automatic
        Fill Area = On
        Fill Area Options = Automatic
        Is Valid = True
        Line Name = Series 1
        Use Automatic Line Naming = On
        END
      END
      OBJECT REPORT OPTIONS:
          Report Caption = Pressure coefficient along centerline of car by distance along X axis from nose of car
      END
    END""".format(simulation.sim_name))
    results1.SendCommand(Command=">chart print, Chart Name = /CHART:Cp vs X Coord, filename = {}/Cp vs X Coord.png, x size = 2000, y size = 2000, format = png, factor = 1.83074".format(media_dir))
    results1.SendCommand(Command="> report hideItem=/CHART:Cp vs X Coord")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /WIREFRAME:Wireframe, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.655433
        Pan = -0.0111499, -0.372659
        Rotation Quaternion = -0.707107, 0, 0, 0.707107
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(cp_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(pressure_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(tke_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(wallshear_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.512924
        Pan = 0, 0
        Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.689005
        Pan = -0.0972085, -0.337592
        Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(cp_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(pressure_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename ={}/TKE Contour 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(tke_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(wallshear_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 1.59745
        Pan = 0, 0
        Rotation Quaternion = -0.5, 0.5, 0.5, 0.5
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(cp_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(pressure_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(tke_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(wallshear_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 1.59745
        Pan = 0, 0
        Rotation Quaternion = -0.5, -0.5, -0.5, 0.5
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(cp_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(pressure_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(tke_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(wallshear_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.609706
        Pan = 0, 0
        Rotation Quaternion = 0, 0, 0, 1
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.624948
        Pan = -0.141048, -0.546109
        Rotation Quaternion = 0, 0, 0, 1
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(cp_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(pressure_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(tke_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(wallshear_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.640572
        Pan = -0.079174, -0.550776
        Rotation Quaternion = 1, 4.47035e-08, -6.12324e-17, 1.44757e-24
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(cp_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(pressure_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(tke_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(wallshear_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.640572
        Pan = -0.079174, -0.550776
        Rotation Quaternion = 0.611682, -0.00437015, -0.0498028, -0.789522
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.707071
        Pan = 0.0309811, -0.313254
        Rotation Quaternion = 0.16889, 0.490153, 0.833347, -0.191657
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(cp_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(pressure_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(tke_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(wallshear_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.656586
        Pan = 0.154765, -0.404108
        Rotation Quaternion = -0.466997, 0.0118956, -0.123012, 0.87557
        
      END

    END

    VIEW:View 1
      Light Angle = 90.0881, 104.046
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(cp_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(pressure_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(tke_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(wallshear_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = 0.00328224, -0.331506
        Rotation Quaternion = -0.863355, 0.0798891, -0.128229, 0.481439
        
      END

    END

    VIEW:View 1
      Light Angle = 126.207, 83.4066
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = -0.0328224, -0.246168
        Rotation Quaternion = -0.866455, 0.0319442, -0.101365, 0.487802
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(cp_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(pressure_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(tke_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Wall Shear Streamline, view=VIEW:View 1")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(wallshear_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = -0.0328224, -0.246168
        Rotation Quaternion = -0.0665846, -0.813088, -0.53828, 0.211405
        
      END

    END

    VIEW:View 1
      Light Angle = 95.0494, 82.0174
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = -0.0328224, -0.246168
        Rotation Quaternion = -0.0149095, -0.854263, -0.494958, 0.15814
        
      END

    END

    VIEW:View 1
      Light Angle = 89.0957, 75.2699
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(cp_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(pressure_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(tke_dir))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(wallshear_dir))
    results1.SendCommand(Command="> report showItem=/CHART:Cp vs X Coord")
    results1.SendCommand(Command="""EXPORT:
     Export File = {}/Cp vs X Coord.csv
     Export Chart Name = Cp vs X Coord
     Overwrite = On
    END
    >export chart""".format(media_dir))
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.512924
        Pan = 0, 0
        Rotation Quaternion = -0.707107, 0, 0, 0.707107
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /DATA READER/CASE:Case {}/BOUNDARY:car, view=/VIEW:View 1""".format(simulation.sim_name))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.656586
        Pan = 0.0997342, -0.360136
        Rotation Quaternion = -0.707107, 0, 0, 0.707107
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Centerline Polyline.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(media_dir))
    results1.SendCommand(Command=">setPreferences Viewer Background Colour Type = Solid, Viewer Background Image File =  , Viewer Background Colour = 0&0&0, Global Text Colour = 1&1&1")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Centerline Polyline Black.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(media_dir))
    results1.SendCommand(Command=">setPreferences Viewer Background Type = Colour, Viewer Background Colour Type = Top-Bottom Gradient, Viewer Background Colour = 0.42&0.55&0.871, Viewer Background Colour 2 = 1&1&1, Global Text Colour = 0&0&0, Global Edge Colour = 0&0&0")
    results1.Exit()

    return

def post_streamlines_fb(simulation, index, proj_params):
    if index==0:
        module = "POST"
    else:
        module = "POST {}".format(index)
    
    sim_path = os.path.join(proj_params.results_dir, simulation.sim_name)
    media_dir = os.path.join(sim_path, "Media Files")
    animate_dir = os.path.join(media_dir, "\\Streamline Animations").replace(os.sep, '/')
    
    system1 = GetSystem(Name=module)
    results1 = system1.GetContainer(ComponentName="Results")
    results1.Edit()
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /DATA READER/CASE:Case {}/BOUNDARY:car, view=/VIEW:View 1""".format(simulation.sim_name))
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.656586
        Pan = 0.0997342, -0.360136
        Rotation Quaternion = -0.555856, 0.2474, 0.348336, 0.713069
        
      END

    END

    VIEW:View 1
      Light Angle = 101.003, 125.876
    END

    > update
    > autolegend plot=/ISOSURFACE:Isosurface Y 0, view=VIEW:View 1""")
    results1.SendCommand(Command="""ISOSURFACE:Isosurface Y 0
    Apply Instancing Transform = On
    Apply Texture = Off
    Blend Texture = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Velocity
    Colour Variable Boundary Values = Conservative
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Max = 0.0 [m s^-1]
    Min = 0.0 [m s^-1]
    Range = Global
    Render Edge Angle = 0 [degree]
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Texture Angle = 0
    Texture Direction = 0 , 1 , 0 
    Texture File =  
    Texture Material = Metal
    Texture Position = 0 , 0 
    Texture Scale = 1
    Texture Type = Predefined
    Tile Texture = Off
    Transform Texture = Off
    Transparency = 0.0
    Value = 0.0 [m]
    Variable = Y
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /ISOSURFACE:Isosurface Y 0, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /ISOSURFACE:Isosurface Y 0, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/ISOSURFACE:Isosurface Pos Y 40, view=VIEW:View 1")
    results1.SendCommand(Command="""ISOSURFACE:Isosurface Pos Y 40
    Apply Instancing Transform = On
    Apply Texture = Off
    Blend Texture = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Velocity
    Colour Variable Boundary Values = Conservative
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Max = 0.0 [m s^-1]
    Min = 0.0 [m s^-1]
    Range = Global
    Render Edge Angle = 0 [degree]
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Texture Angle = 0
    Texture Direction = 0 , 1 , 0 
    Texture File =  
    Texture Material = Metal
    Texture Position = 0 , 0 
    Texture Scale = 1
    Texture Type = Predefined
    Tile Texture = Off
    Transform Texture = Off
    Transparency = 0.0
    Value = 0.4 [m]
    Variable = Y
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /ISOSURFACE:Isosurface Pos Y 40, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /ISOSURFACE:Isosurface Pos Y 40, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/ISOSURFACE:Isosurface Neg Y 40, view=VIEW:View 1")
    results1.SendCommand(Command="""ISOSURFACE:Isosurface Neg Y 40
    Apply Instancing Transform = On
    Apply Texture = Off
    Blend Texture = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Velocity
    Colour Variable Boundary Values = Conservative
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Max = 0.0 [m s^-1]
    Min = 0.0 [m s^-1]
    Range = Global
    Render Edge Angle = 0 [degree]
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Texture Angle = 0
    Texture Direction = 0 , 1 , 0 
    Texture File =  
    Texture Material = Metal
    Texture Position = 0 , 0 
    Texture Scale = 1
    Texture Type = Predefined
    Tile Texture = Off
    Transform Texture = Off
    Transparency = 0.0
    Value = -0.4 [m]
    Variable = Y
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /ISOSURFACE:Isosurface Neg Y 40, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /ISOSURFACE:Isosurface Neg Y 40, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Streamline Y 0, view=VIEW:View 1")
    results1.SendCommand(Command="""STREAMLINE:Streamline Y 0
    Absolute Tolerance = 0.0 [m]
    Apply Instancing Transform = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Velocity
    Colour Variable Boundary Values = Conservative
    Cross Periodics = On
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Draw Streams = On
    Draw Symbols = Off
    Grid Tolerance = 0.01
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Width = 1
    Location List = /ISOSURFACE:Isosurface Y 0
    Locator Sampling Method = Vertex
    Max = 0.0 [m s^-1]
    Maximum Number of Items = 150
    Min = 0.0 [m s^-1]
    Number of Samples = 500
    Number of Sides = 8
    Range = Global
    Reduction Factor = 1.0
    Reduction or Max Number = Max Number
    Sample Spacing = 0.1
    Sampling Aspect Ratio = 1
    Sampling Grid Angle = 0 [degree]
    Seed Point Type = Equally Spaced Samples
    Simplify Geometry = Off
    Specular Lighting = On
    Stream Drawing Mode = Line
    Stream Initial Direction = 0 , 0 , 0 
    Stream Size = 1.0
    Stream Symbol = Ball
    Streamline Direction = Forward and Backward
    Streamline Maximum Periods = 20
    Streamline Maximum Segments = 10000
    Streamline Maximum Time = 0.0 [s]
    Streamline Type = 3D Streamline
    Streamline Width = 2
    Surface Drawing = Smooth Shading
    Surface Streamline Direction = Forward and Backward
    Symbol Size = 1.0
    Symbol Start Time = 10.0 [s]
    Symbol Stop Time = -10.0 [s]
    Symbol Time Interval = 1.0 [s]
    Tolerance Mode = Grid Relative
    Transparency = 0.0
    Variable = Velocity
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Streamline Y 0, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Streamline Pos Y 40, view=VIEW:View 1")
    results1.SendCommand(Command="""STREAMLINE:Streamline Pos Y 40
    Absolute Tolerance = 0.0 [m]
    Apply Instancing Transform = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Velocity
    Colour Variable Boundary Values = Conservative
    Cross Periodics = On
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Draw Streams = On
    Draw Symbols = Off
    Grid Tolerance = 0.01
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Width = 1
    Location List = /ISOSURFACE:Isosurface Pos Y 40
    Locator Sampling Method = Vertex
    Max = 0.0 [m s^-1]
    Maximum Number of Items = 150
    Min = 0.0 [m s^-1]
    Number of Samples = 500
    Number of Sides = 8
    Range = Global
    Reduction Factor = 1.0
    Reduction or Max Number = Max Number
    Sample Spacing = 0.1
    Sampling Aspect Ratio = 1
    Sampling Grid Angle = 0 [degree]
    Seed Point Type = Equally Spaced Samples
    Simplify Geometry = Off
    Specular Lighting = On
    Stream Drawing Mode = Line
    Stream Initial Direction = 0 , 0 , 0 
    Stream Size = 1.0
    Stream Symbol = Ball
    Streamline Direction = Forward and Backward
    Streamline Maximum Periods = 20
    Streamline Maximum Segments = 10000
    Streamline Maximum Time = 0.0 [s]
    Streamline Type = 3D Streamline
    Streamline Width = 2
    Surface Drawing = Smooth Shading
    Surface Streamline Direction = Forward and Backward
    Symbol Size = 1.0
    Symbol Start Time = 10.0 [s]
    Symbol Stop Time = -10.0 [s]
    Symbol Time Interval = 1.0 [s]
    Tolerance Mode = Grid Relative
    Transparency = 0.0
    Variable = Velocity
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Streamline Pos Y 40, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Streamline Neg Y 40, view=VIEW:View 1")
    results1.SendCommand(Command="""STREAMLINE:Streamline Neg Y 40
    Absolute Tolerance = 0.0 [m]
    Apply Instancing Transform = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Velocity
    Colour Variable Boundary Values = Conservative
    Cross Periodics = On
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Draw Streams = On
    Draw Symbols = Off
    Grid Tolerance = 0.01
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Width = 1
    Location List = /ISOSURFACE:Isosurface Neg Y 40
    Locator Sampling Method = Vertex
    Max = 0.0 [m s^-1]
    Maximum Number of Items = 150
    Min = 0.0 [m s^-1]
    Number of Samples = 500
    Number of Sides = 8
    Range = Global
    Reduction Factor = 1.0
    Reduction or Max Number = Max Number
    Sample Spacing = 0.1
    Sampling Aspect Ratio = 1
    Sampling Grid Angle = 0 [degree]
    Seed Point Type = Equally Spaced Samples
    Simplify Geometry = Off
    Specular Lighting = On
    Stream Drawing Mode = Line
    Stream Initial Direction = 0 , 0 , 0 
    Stream Size = 1.0
    Stream Symbol = Ball
    Streamline Direction = Forward and Backward
    Streamline Maximum Periods = 20
    Streamline Maximum Segments = 10000
    Streamline Maximum Time = 0.0 [s]
    Streamline Type = 3D Streamline
    Streamline Width = 2
    Surface Drawing = Smooth Shading
    Surface Streamline Direction = Forward and Backward
    Symbol Size = 1.0
    Symbol Start Time = 10.0 [s]
    Symbol Stop Time = -10.0 [s]
    Symbol Time Interval = 1.0 [s]
    Tolerance Mode = Grid Relative
    Transparency = 0.0
    Variable = Velocity
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Streamline Neg Y 40, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
    Camera Mode = User Specified
    CAMERA:
    Option = Pivot Point and Quaternion
    Pivot Point = 2.51148, 0.64251, 0.68061
    Scale = 0.803174
    Pan = 2.19897, -0.011249
    Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17

    END

    END

    > update
    ANIMATION:ANIMATION
    QAnim MPEG Filename = {}/Trailing Edge and Wake Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4

    END""".format(animate_dir))
    results1.SendCommand(Command="""ANIMATION:
    Animation Bit Rate = 5152000
    Animation Frame Rate = 24
    Animation Quality = Highest
    Animation Speed Factor = 2
    Antialiasing = On
    Drop Last MPEG Frame = Off
    Hardcopy Tolerance = 0.0001
    Intermediate File Format = jpg
    Keep Intermediate Files = Off
    MPEG Height = 1080
    MPEG Scale = 100
    MPEG Size = 1080p
    MPEG Width = 1920
    Output Directory = .
    Output to User Directory = Off
    QAnim Override Symbol = On
    QAnim Symbol Size = 0.05
    QAnim Symbol Spacing = 0.3
    QAnim Symbol Type = Ball
    Screen Capture = Off
    Speed Adjustment Selection = Normal
    Speed Scaling Method = Distribute Frames Smoothly
    Timestep Interpolation Method = Timestep
    Variable Bit Rate = On
    White Background = Off
    END""")
    results1.SendCommand(Command="""ANIMATION: ANIMATION
    QAnim Object List = /STREAMLINE:Streamline Neg Y 40,/STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
    QAnim Frames = 100
    QAnim MPEG Filename = {}/Trailing Edge and Wake Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4
    END
    >animate quickAnimate""".format(animate_dir))
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 4.4939, 0.459533, 0.511379
        Scale = 0.860138
        Pan = -1.27971, -0.419625
        Rotation Quaternion = -3.72529e-09, 0.707107, 0.707107, -3.72529e-09
        
      END

    END

    > update
    ANIMATION:ANIMATION
    QAnim MPEG Filename = {}/Canopy Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4

    END""".format(animate_dir))
    results1.SendCommand(Command="""ANIMATION: ANIMATION
    QAnim Object List = /STREAMLINE:Streamline Neg Y 40,/STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
    QAnim Frames = 100
    QAnim MPEG Filename = {}/Canopy Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4
    END
    >animate quickAnimate""".format(animate_dir))
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 3.23676, 0.504839, 0.995587
        Scale = 0.289498
        Pan = -0.24374, -1.06636
        Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17
        
      END

    END

    > update
    ANIMATION:ANIMATION
    QAnim MPEG Filename = {}/Right Side Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4

    END""".format(animate_dir))
    results1.SendCommand(Command="""ANIMATION: ANIMATION
    QAnim Object List = /STREAMLINE:Streamline Neg Y 40,/STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
    QAnim Frames = 100
    QAnim MPEG Filename = {}/Right Side Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4
    END
    >animate quickAnimate""".format(animate_dir))
    results1.Exit()

    return

def post_streamlines_hb(simulation, index, proj_params):
    if index==0:
        module = "POST"
    else:
        module = "POST {}".format(index)
    
    sim_path = os.path.join(proj_params.results_dir, simulation.sim_name)
    media_dir = os.path.join(sim_path, "Media Files")
    animate_dir = os.path.join(media_dir, "\\Streamline Animations").replace(os.sep, '/')

    system1 = GetSystem(Name=module)
    results1 = system1.GetContainer(ComponentName="Results")
    results1.Edit()
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /DATA READER/CASE:Case {}/BOUNDARY:car, view=/VIEW:View 1""".format(simulation.sim_name))
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.656586
        Pan = 0.0997342, -0.360136
        Rotation Quaternion = -0.555856, 0.2474, 0.348336, 0.713069
        
      END

    END

    VIEW:View 1
      Light Angle = 101.003, 125.876
    END

    > update
    > autolegend plot=/ISOSURFACE:Isosurface Y 0, view=VIEW:View 1""")
    results1.SendCommand(Command="""ISOSURFACE:Isosurface Y 0
    Apply Instancing Transform = On
    Apply Texture = Off
    Blend Texture = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Velocity
    Colour Variable Boundary Values = Conservative
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Max = 0.0 [m s^-1]
    Min = 0.0 [m s^-1]
    Range = Global
    Render Edge Angle = 0 [degree]
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Texture Angle = 0
    Texture Direction = 0 , 1 , 0 
    Texture File =  
    Texture Material = Metal
    Texture Position = 0 , 0 
    Texture Scale = 1
    Texture Type = Predefined
    Tile Texture = Off
    Transform Texture = Off
    Transparency = 0.0
    Value = 0.0 [m]
    Variable = Y
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /ISOSURFACE:Isosurface Y 0, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /ISOSURFACE:Isosurface Y 0, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/ISOSURFACE:Isosurface Pos Y 40, view=VIEW:View 1")
    results1.SendCommand(Command="""ISOSURFACE:Isosurface Pos Y 40
    Apply Instancing Transform = On
    Apply Texture = Off
    Blend Texture = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Velocity
    Colour Variable Boundary Values = Conservative
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Max = 0.0 [m s^-1]
    Min = 0.0 [m s^-1]
    Range = Global
    Render Edge Angle = 0 [degree]
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Texture Angle = 0
    Texture Direction = 0 , 1 , 0 
    Texture File =  
    Texture Material = Metal
    Texture Position = 0 , 0 
    Texture Scale = 1
    Texture Type = Predefined
    Tile Texture = Off
    Transform Texture = Off
    Transparency = 0.0
    Value = 0.4 [m]
    Variable = Y
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /ISOSURFACE:Isosurface Pos Y 40, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /ISOSURFACE:Isosurface Pos Y 40, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Streamline Y 0, view=VIEW:View 1")
    results1.SendCommand(Command="""STREAMLINE:Streamline Y 0
    Absolute Tolerance = 0.0 [m]
    Apply Instancing Transform = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Velocity
    Colour Variable Boundary Values = Conservative
    Cross Periodics = On
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Draw Streams = On
    Draw Symbols = Off
    Grid Tolerance = 0.01
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Width = 1
    Location List = /ISOSURFACE:Isosurface Y 0
    Locator Sampling Method = Vertex
    Max = 0.0 [m s^-1]
    Maximum Number of Items = 150
    Min = 0.0 [m s^-1]
    Number of Samples = 500
    Number of Sides = 8
    Range = Global
    Reduction Factor = 1.0
    Reduction or Max Number = Max Number
    Sample Spacing = 0.1
    Sampling Aspect Ratio = 1
    Sampling Grid Angle = 0 [degree]
    Seed Point Type = Equally Spaced Samples
    Simplify Geometry = Off
    Specular Lighting = On
    Stream Drawing Mode = Line
    Stream Initial Direction = 0 , 0 , 0 
    Stream Size = 1.0
    Stream Symbol = Ball
    Streamline Direction = Forward and Backward
    Streamline Maximum Periods = 20
    Streamline Maximum Segments = 10000
    Streamline Maximum Time = 0.0 [s]
    Streamline Type = 3D Streamline
    Streamline Width = 2
    Surface Drawing = Smooth Shading
    Surface Streamline Direction = Forward and Backward
    Symbol Size = 1.0
    Symbol Start Time = 10.0 [s]
    Symbol Stop Time = -10.0 [s]
    Symbol Time Interval = 1.0 [s]
    Tolerance Mode = Grid Relative
    Transparency = 0.0
    Variable = Velocity
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Streamline Y 0, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Streamline Pos Y 40, view=VIEW:View 1")
    results1.SendCommand(Command="""STREAMLINE:Streamline Pos Y 40
    Absolute Tolerance = 0.0 [m]
    Apply Instancing Transform = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Velocity
    Colour Variable Boundary Values = Conservative
    Cross Periodics = On
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Faces = On
    Draw Lines = Off
    Draw Streams = On
    Draw Symbols = Off
    Grid Tolerance = 0.01
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Width = 1
    Location List = /ISOSURFACE:Isosurface Pos Y 40
    Locator Sampling Method = Vertex
    Max = 0.0 [m s^-1]
    Maximum Number of Items = 150
    Min = 0.0 [m s^-1]
    Number of Samples = 500
    Number of Sides = 8
    Range = Global
    Reduction Factor = 1.0
    Reduction or Max Number = Max Number
    Sample Spacing = 0.1
    Sampling Aspect Ratio = 1
    Sampling Grid Angle = 0 [degree]
    Seed Point Type = Equally Spaced Samples
    Simplify Geometry = Off
    Specular Lighting = On
    Stream Drawing Mode = Line
    Stream Initial Direction = 0 , 0 , 0 
    Stream Size = 1.0
    Stream Symbol = Ball
    Streamline Direction = Forward and Backward
    Streamline Maximum Periods = 20
    Streamline Maximum Segments = 10000
    Streamline Maximum Time = 0.0 [s]
    Streamline Type = 3D Streamline
    Streamline Width = 2
    Surface Drawing = Smooth Shading
    Surface Streamline Direction = Forward and Backward
    Symbol Size = 1.0
    Symbol Start Time = 10.0 [s]
    Symbol Stop Time = -10.0 [s]
    Symbol Time Interval = 1.0 [s]
    Tolerance Mode = Grid Relative
    Transparency = 0.0
    Variable = Velocity
    Variable Boundary Values = Conservative
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      Principal Axis = Z
      Reflection Plane Option = XY Plane
      Rotation Angle = 0.0 [degree]
      Rotation Axis From = 0 [m], 0 [m], 0 [m]
      Rotation Axis To = 0 [m], 0 [m], 0 [m]
      Rotation Axis Type = Principal Axis
      Scale Vector = 1 , 1 , 1 
      Translation Vector = 0 [m], 0 [m], 0 [m]
      X = 0.0 [m]
      Y = 0.0 [m]
      Z = 0.0 [m]
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Streamline Pos Y 40, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
    Camera Mode = User Specified
    CAMERA:
    Option = Pivot Point and Quaternion
    Pivot Point = 2.51148, 0.64251, 0.68061
    Scale = 0.803174
    Pan = 2.19897, -0.011249
    Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17

    END

    END

    > update
    ANIMATION:ANIMATION
    QAnim MPEG Filename = {}/Trailing Edge and Wake Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4

    END""".format(animate_dir))
    results1.SendCommand(Command="""ANIMATION:
    Animation Bit Rate = 5152000
    Animation Frame Rate = 24
    Animation Quality = Highest
    Animation Speed Factor = 2
    Antialiasing = On
    Drop Last MPEG Frame = Off
    Hardcopy Tolerance = 0.0001
    Intermediate File Format = jpg
    Keep Intermediate Files = Off
    MPEG Height = 1080
    MPEG Scale = 100
    MPEG Size = 1080p
    MPEG Width = 1920
    Output Directory = .
    Output to User Directory = Off
    QAnim Override Symbol = On
    QAnim Symbol Size = 0.05
    QAnim Symbol Spacing = 0.3
    QAnim Symbol Type = Ball
    Screen Capture = Off
    Speed Adjustment Selection = Normal
    Speed Scaling Method = Distribute Frames Smoothly
    Timestep Interpolation Method = Timestep
    Variable Bit Rate = On
    White Background = Off
    END""")
    results1.SendCommand(Command="""ANIMATION: ANIMATION
    QAnim Object List = /STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
    QAnim Frames = 100
    QAnim MPEG Filename = {}/Trailing Edge and Wake Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4
    END
    >animate quickAnimate""".format(animate_dir))
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 4.4939, 0.459533, 0.511379
        Scale = 0.860138
        Pan = -1.27971, -0.419625
        Rotation Quaternion = -3.72529e-09, 0.707107, 0.707107, -3.72529e-09
        
      END

    END

    > update
    ANIMATION:ANIMATION
    QAnim MPEG Filename = {}/Canopy Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4

    END""".format(animate_dir))
    results1.SendCommand(Command="""ANIMATION: ANIMATION
    QAnim Object List = /STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
    QAnim Frames = 100
    QAnim MPEG Filename = {}/Canopy Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4
    END
    >animate quickAnimate""".format(animate_dir))
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 3.23676, 0.504839, 0.995587
        Scale = 0.289498
        Pan = -0.24374, -1.06636
        Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17
        
      END

    END

    > update
    ANIMATION:ANIMATION
    QAnim MPEG Filename = {}/Right Side Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4

    END""".format(animate_dir))
    results1.SendCommand(Command="""ANIMATION: ANIMATION
    QAnim Object List = /STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
    QAnim Frames = 100
    QAnim MPEG Filename = {}/Right Side Streamline Animation.mp4
    QAnim Save MPEG = On
    QAnim Looping = Loop
    QAnim Looping Cycles = 1
    Video Format = mp4
    END
    >animate quickAnimate""".format(animate_dir))
    results1.Exit()

    return

abspath = os.path.abspath(__file__)
dir = os.path.dirname(abspath)
os.chdir(dir)

(sim_list, proj_params) = param_extract("Simulation Parameters.csv")

initialize_project(proj_params)

fluent_sim_setup(sim_list, proj_params.processes)