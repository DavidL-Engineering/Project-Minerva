import os
from datetime import date

class Mesh_Properties:
    '''
    Mesh_Properties object stores the name and directory of the exported .CAS file containing the mesh.

    Instance Variables
    ---------------------
    CAS_name : Name of .CAS file containing the mesh. Does not include file extension. [str]
    CAS_dir : Directory containing the .CAS file with the name as indicated in CAS_name. [str]
    '''
    
    def __init__(self, CAS_name = None, CAS_dir = None):
        '''Define instance variables.'''
        self.CAS_name = CAS_name
        self.CAS_dir = CAS_dir
    
    def __str__(self):
        '''Print properties of Mesh_Properties object.'''
        return "\n----MESH PROPERTIES----\nCAS file: {}\nLocated in {}".format(self.CAS_name, self.CAS_dir)

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
    CG : Specification of whether CG is entered and valid. [bool]
    post : Specification of whether post-processing is desired if simulation converges. [bool]
    streamlines : Specification of whether streamline animations are desired in post-processing. [bool]
    '''
    
    def __init__(self, sol_method = None, CG = None, post = None, streamlines = None):
        '''Define instance variables.'''
        self.sol_method = sol_method #Either K-W or T-SST
        self.CG = CG #Either True or False
        self.post = post #Either True or False
        self.streamlines = streamlines #True or False

    def __str__(self):
        '''Print properties of Dimension_Properties object.'''
        return "\n----WORKFLOW PROPERTIES----\nSolution method: {}\nCG: {}\nPost-Processing: {}\nStreamline Animations: {}".format(self.sol_method, self.CG, self.post, self.streamlines)

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

    for line in lines:
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

        sim_workflow = Workflow_Properties(line[3], CG_bool, post_bool, streamlines_bool)
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

    proj_param = Project(line[13], line[14], line[15], line[16])

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

    Save(FilePath=("{}/{}.wbpj", proj_directory, project.proj_name), Overwrite=True)

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
        results_dir_check(proj_params.results_dir, simulation.sim_name, simulation.workflow.post, simulation.workflow.streamlines)
    
    return

def results_dir_check(path, name, post, streamlines):
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
    
    if post:
        sim_path = os.path.join(path, name)
        if (os.path.exists(sim_path) == False):
            os.mkdir(sim_path)
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

    for sim in sim_list:
        if sim.Workflow_Properties.sol_method.lower() in komega:
            komega_setup(sim, processes)
        elif sim.Workflow_Properties.sol_method.lower() in tsst:
            tsst_setup(sim, processes)

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
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"MenuBar*ImportSubMenu*Case...\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"{}/{}}.cas\") \"All Case Files (*.cas* *.msh* *.MSH* )\")".format((simulation.Mesh_Properties.CAS_dir.replace(os.sep, '/')), simulation.Mesh_Properties.CAS_name))
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton1(Scale)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Scale Mesh*Table1*Table2(Scaling)*DropDownList2(Mesh Was Created In)\" '( 3))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*Table1*Table2(Scaling)*DropDownList2(Mesh Was Created In)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*Table1*Table2(Scaling)*PushButton4(Scale)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*PanelButtons*PushButton1(Close)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Models\"))(cx-gui-do cx-set-list-selections \"Models*Table1*List1(Models)\" '( 2))(cx-gui-do cx-activate-item \"Models*Table1*List1(Models)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Models*Table1*PushButton2(Edit)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Viscous Model*PanelButtons*PushButton1(OK)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid"))(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Materials|Fluid|air\"))(cx-gui-do cx-set-real-entry-list \"Create/Edit Materials*RealEntry10\" '( 1.177))(cx-gui-do cx-set-real-entry-list \"Create/Edit Materials*RealEntry16\" '( 1.846e-05))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton3(Change/Create)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton1(Close)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Inlet|input (velocity-inlet, id=5)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Inlet|input (velocity-inlet, id=5)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|Inlet|input (velocity-inlet, id=5)\"))(cx-gui-do cx-set-list-selections \"Velocity Inlet*Frame3*Frame1(Momentum)*Table1*DropDownList6(Velocity Specification Method)\" '( 0))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Velocity Inlet*Frame3*Frame1(Momentum)*Table1*DropDownList6(Velocity Specification Method)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-expression-entry \"Velocity Inlet*Frame3*Frame1(Momentum)*Table1*Table8*ExpressionEntry1(Velocity Magnitude)\" '(\"18\" . 0))(cx-gui-do cx-activate-item \"Velocity Inlet*PanelButtons*PushButton1(OK)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Outlet|output (pressure-outlet, id=6)"))(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|car (wall, id=4)"))(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|road (wall, id=7)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|road (wall, id=7)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|Wall|road (wall, id=7)\"))(cx-gui-do cx-set-toggle-button2 \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*ToggleBox1(Wall Motion)*Moving Wall\" #t)(cx-gui-do cx-activate-item \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*ToggleBox1(Wall Motion)*Moving Wall\")(cx-gui-do cx-set-toggle-button2 \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table1*ToggleBox1*Absolute\" #t)(cx-gui-do cx-activate-item \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table1*ToggleBox1*Absolute\")(cx-gui-do cx-set-expression-entry \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table2*Table1*ExpressionEntry1(Speed)\" '(\"18\" . 0))(cx-gui-do cx-activate-item \"Wall*PanelButtons*PushButton1(OK)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))(cx-gui-do cx-set-toggle-button2 "Wall*Frame3*Frame1(Momentum)*Table1*Frame2*Frame1*Table1*ToggleBox1(Shear Condition)*Specified Shear" #t)(cx-gui-do cx-activate-item "Wall*Frame3*Frame1(Momentum)*Table1*Frame2*Frame1*Table1*ToggleBox1(Shear Condition)*Specified Shear")(cx-gui-do cx-activate-item "Wall*PanelButtons*PushButton1(OK)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Frames"))(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Values"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Values"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Reference Values\"))(cx-gui-do cx-set-list-selections \"Reference Values*DropDownList1(Compute from)\" '( 3))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Reference Values*DropDownList1(Compute from)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Reference Values*Table2(Reference Values)*RealEntry1(Area)\" '( {}}))(cx-gui-do cx-activate-item \"Reference Values*Table2(Reference Values)*RealEntry1(Area)\")".format(simulation.Dimension_Properties.area))
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Reference Values*Table2(Reference Values)*RealEntry5(Length)\" '( {}}))(cx-gui-do cx-activate-item \"Reference Values*Table2(Reference Values)*RealEntry5(Length)\")".format(simulation.Dimension_Properties.length))
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
    setup1.SendCommand(Command='(cx-gui-do cx-set-text-entry "Drag Report Definition*Table1*TextEntry3(Name)" "drag")(cx-gui-do cx-activate-item "Drag Report Definition*Table1*TextEntry3(Name)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\")(cx-gui-do cx-set-list-selections \"Drag Report Definition*Table1*Table2*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table2*List2(Wall Zones)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\")(cx-gui-do cx-activate-item \"Drag Report Definition*PanelButtons*PushButton1(OK)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*Force ReportSubMenu*Lift...")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-text-entry "Lift Report Definition*Table1*TextEntry3(Name)" "lift")(cx-gui-do cx-activate-item "Lift Report Definition*Table1*TextEntry3(Name)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\")(cx-gui-do cx-set-list-selections \"Lift Report Definition*Table1*Table2*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table2*List2(Wall Zones)\")(cx-gui-do cx-set-real-entry-list \"Lift Report Definition*Table1*Table1*Table2(Force Vector)*RealEntry2(Y)\" '( 0))(cx-gui-do cx-set-real-entry-list \"Lift Report Definition*Table1*Table1*Table2(Force Vector)*RealEntry3(Z)\" '( 1))(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\")(cx-gui-do cx-activate-item \"Lift Report Definition*PanelButtons*PushButton1(OK)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*PanelButtons*PushButton1(Close)")')
    setup1.SendCommand(Command="/mesh/repair-improve/allow-repair-at-boundaries yes")
    setup1.SendCommand(Command="/mesh/repair-improve/include-local-polyhedra-conversion-in-repair yes")
    setup1.SendCommand(Command="/mesh/repair-improve/repair")
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|General"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|General"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|General"))')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton3(Check)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton5(Report Quality)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Solution|Run Calculation\"))(cx-gui-do cx-set-list-selections \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table1*DropDownList2(Length Scale Method)\" '( 2))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table1*DropDownList2(Length Scale Method)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table3*RealEntry3(Length Scale)\" '({}))(cx-gui-do cx-activate-item \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table3*RealEntry3(Length Scale)\")".format(simulation.Dimension_Properties.length))
    setup1.SendCommand(Command='(cx-gui-do cx-set-integer-entry "Run Calculation*Table1*Table3(Parameters)*Table1*Table1*IntegerEntry1(Number of Iterations)" 600)(cx-gui-do cx-activate-item "Run Calculation*Table1*Table3(Parameters)*Table1*Table1*IntegerEntry1(Number of Iterations)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Initialization*Table1*Frame11*PushButton2(Initialize)")')
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
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"MenuBar*ImportSubMenu*Case...\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"{}/{}}.cas\") \"All Case Files (*.cas* *.msh* *.MSH* )\")".format((simulation.Mesh_Properties.CAS_dir.replace(os.sep, '/')), simulation.Mesh_Properties.CAS_name))
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton1(Scale)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Scale Mesh*Table1*Table2(Scaling)*DropDownList2(Mesh Was Created In)\" '( 3))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*Table1*Table2(Scaling)*DropDownList2(Mesh Was Created In)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*Table1*Table2(Scaling)*PushButton4(Scale)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*PanelButtons*PushButton1(Close)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton3(Check)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton5(Report Quality)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton5(Report Quality)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (SST k-omega)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (SST k-omega)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (SST k-omega)"))(cx-gui-do cx-set-toggle-button2 "Viscous Model*Table1*ToggleBox1(Model)*Transition SST (4 eqn)" #t)(cx-gui-do cx-activate-item "Viscous Model*Table1*ToggleBox1(Model)*Transition SST (4 eqn)")(cx-gui-do cx-activate-item "Viscous Model*PanelButtons*PushButton1(OK)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (Transition SST (4 eqn))"))(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Materials|Fluid|air\"))(cx-gui-do cx-set-real-entry-list \"Create/Edit Materials*RealEntry10\" '( 1.177))(cx-gui-do cx-set-real-entry-list \"Create/Edit Materials*RealEntry16\" '( 1.846e-05))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton3(Change/Create)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton1(Close)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Inlet|input (velocity-inlet, id=5)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Inlet|input (velocity-inlet, id=5)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|Inlet|input (velocity-inlet, id=5)\"))(cx-gui-do cx-set-list-selections \"Velocity Inlet*Frame3*Frame1(Momentum)*Table1*DropDownList6(Velocity Specification Method)\" '( 0))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Velocity Inlet*Frame3*Frame1(Momentum)*Table1*DropDownList6(Velocity Specification Method)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-expression-entry \"Velocity Inlet*Frame3*Frame1(Momentum)*Table1*Table8*ExpressionEntry1(Velocity Magnitude)\" '(\"18\" . 0))(cx-gui-do cx-activate-item \"Velocity Inlet*PanelButtons*PushButton1(OK)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|road (wall, id=7)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|road (wall, id=7)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|Wall|road (wall, id=7)\"))(cx-gui-do cx-set-toggle-button2 \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*ToggleBox1(Wall Motion)*Moving Wall\" #t)(cx-gui-do cx-activate-item \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*ToggleBox1(Wall Motion)*Moving Wall\")(cx-gui-do cx-set-toggle-button2 \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table1*ToggleBox1*Absolute\" #t)(cx-gui-do cx-activate-item \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table1*ToggleBox1*Absolute\")(cx-gui-do cx-set-expression-entry \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table2*Table1*ExpressionEntry1(Speed)\" '(\"18\" . 0))(cx-gui-do cx-activate-item \"Wall*PanelButtons*PushButton1(OK)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Wall|walls (wall, id=8)"))(cx-gui-do cx-set-toggle-button2 "Wall*Frame3*Frame1(Momentum)*Table1*Frame2*Frame1*Table1*ToggleBox1(Shear Condition)*Specified Shear" #t)(cx-gui-do cx-activate-item "Wall*Frame3*Frame1(Momentum)*Table1*Frame2*Frame1*Table1*ToggleBox1(Shear Condition)*Specified Shear")(cx-gui-do cx-activate-item "Wall*PanelButtons*PushButton1(OK)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Values"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Values"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Reference Values\"))(cx-gui-do cx-set-list-selections \"Reference Values*DropDownList1(Compute from)\" '( 3))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Reference Values*DropDownList1(Compute from)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Reference Values*Table2(Reference Values)*RealEntry1(Area)\" '({}))(cx-gui-do cx-activate-item \"Reference Values*Table2(Reference Values)*RealEntry1(Area)\")".format(simulation.Dimension_Properties.area))
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Reference Values*Table2(Reference Values)*RealEntry5(Length)\" '({}))(cx-gui-do cx-activate-item \"Reference Values*Table2(Reference Values)*RealEntry5(Length)\")".format(simulation.Dimension_Properties.length))
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Methods"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Methods"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Solution|Methods\"))(cx-gui-do cx-set-list-selections \"Solution Methods*Table1*Table2(Pressure-Velocity Coupling)*DropDownList2(Scheme)\" '( 3))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Methods*Table1*Table2(Pressure-Velocity Coupling)*DropDownList2(Scheme)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList2(Pressure)\" '( 1))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList2(Pressure)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-toggle-button2 "Solution Methods*Table1*CheckButton5(Pseudo Transient)" #t)(cx-gui-do cx-activate-item "Solution Methods*Table1*CheckButton5(Pseudo Transient)")(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Controls"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Controls"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Controls"))(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*Force ReportSubMenu*Drag...")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-toggle-button2 "Drag Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force" #t)(cx-gui-do cx-activate-item "Drag Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force")(cx-gui-do cx-set-text-entry "Drag Report Definition*Table1*TextEntry3(Name)" "drag")(cx-gui-do cx-activate-item "Drag Report Definition*Table1*TextEntry3(Name)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Drag Report Definition*Table1*Table2*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table2*List2(Wall Zones)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\")(cx-gui-do cx-activate-item \"Drag Report Definition*PanelButtons*PushButton1(OK)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*Force ReportSubMenu*Lift...")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-text-entry "Lift Report Definition*Table1*TextEntry3(Name)" "lift")(cx-gui-do cx-activate-item "Lift Report Definition*Table1*TextEntry3(Name)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\")(cx-gui-do cx-set-list-selections \"Lift Report Definition*Table1*Table2*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table2*List2(Wall Zones)\")(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\")(cx-gui-do cx-set-real-entry-list \"Lift Report Definition*Table1*Table1*Table2(Force Vector)*RealEntry2(Y)\" '( 0))(cx-gui-do cx-set-real-entry-list \"Lift Report Definition*Table1*Table1*Table2(Force Vector)*RealEntry3(Z)\" '( 1))(cx-gui-do cx-activate-item \"Lift Report Definition*PanelButtons*PushButton1(OK)\")")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*PanelButtons*PushButton1(Close)")')
    setup1.SendCommand(Command="/mesh/repair-improve/allow-repair-at-boundaries yes")
    setup1.SendCommand(Command="/mesh/repair-improve/include-local-polyhedra-conversion-in-repair yes")
    setup1.SendCommand(Command="/mesh/repair-improve/repair")
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Solution|Run Calculation\"))(cx-gui-do cx-set-list-selections \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table1*DropDownList2(Length Scale Method)\" '( 2))")
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table1*DropDownList2(Length Scale Method)")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table3*RealEntry3(Length Scale)\" '({}))(cx-gui-do cx-activate-item \"Run Calculation*Table1*Table2(Pseudo Transient Settings)*Table1(Fluid Time Scale)*Table3*RealEntry3(Length Scale)\")".format(simulation.Dimension_Properties.length))
    setup1.SendCommand(Command='(cx-gui-do cx-set-integer-entry "Run Calculation*Table1*Table3(Parameters)*Table1*Table1*IntegerEntry1(Number of Iterations)" 600)(cx-gui-do cx-activate-item "Run Calculation*Table1*Table3(Parameters)*Table1*Table1*IntegerEntry1(Number of Iterations)")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Initialization*Table1*Frame11*PushButton2(Initialize)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*FileMenu*Close Fluent")')
    Save(Overwrite=True)

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
    None
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
            print("Converged")
        else:
            sim_list[i].results.convergence = "Diverged or Error"
            print("Diverged or Error")
    
    return

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
            fluent_results_aggregator(sim_list[i], i, proj_params)
    
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
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"{}}/drag{}.txt\") \"All Files (*)\")".format(raw_results_dir, index))
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
    None
    '''

    raw_results_dir = os.path.join(proj_params.results_dir, simulation.sim_name + "\\Raw Results").replace(os.sep, '/')

    cop_file = open("{}/cp_x_0m_{}.txt".format(raw_results_dir, index), 'r')
    drag_file = open("{}/drag{}.txt".format(raw_results_dir, index), 'r')
    lift_file = open("{}/lift{}.txt".format(raw_results_dir, index), 'r')
    iter_file = open("{}/iter{}.txt".format(raw_results_dir, index), 'r')
    f_left_file = open("{}/f_left{}.txt".format(raw_results_dir, index), 'r')
    f_right_file = open("{}/f_right{}.txt".format(raw_results_dir, index), 'r')
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
    simulation.results.mom_roll = roll_value
    simulation.results.mom_pitch = pitch_value
    simulation.results.mom_yaw = yaw_value
    simulation.results.cop = cop_values

def results_formatter(sim_list, proj_params):
    export_directory = os.path.join(proj_params.results_dir).replace(os.sep, '/')

    current_date = date.today().strftime("%d/%m/%Y")

    with open("{}/Simulation Results.csv".format(export_directory), 'w') as csvfile:
        csvfile.write("Simulation Name,.CAS File Name,Date,Number of Iterations,A. Drag [N] (Total),B. Drag [N]: Pressure + Viscous,A. Lift [N] (Total),B. Lift [N]: Pressure + Viscous,Force Left [N] (Total),Force Right [N] (Total),Roll Moment [N-m] (axis = [1,0,0]),Pitch Moment [N-m] (axis = [0,1,0]),Yaw Moment [N-m] (axis = [0,0,1]),Center of Pressure (x=0 [m]),Status\n")
        for i in range(len(sim_list)):
            if sim_list[i].results.convergence == "Converged":
                csvfile.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(sim_list[i].sim_name, sim_list[i].mesh.CAS_name, sim_current_date, sim_list[i].results.iterations, sim_list[i].results.drag_tot, sim_list[i].results.drag_comp, sim_list[i].results.lift_tot, sim_list[i].results.lift_comp, sim_list[i].results.f_left, sim_list[i].results.f_right, sim_list[i].results.mom_roll, sim_list[i].results.mom_pitch, sim_list[i].results.mom_yaw, sim_list[i].results.cop, sim_list[i].results.convergence))
            else:
                csvfile.write("{},{},{},,,,,,,,,,,,{}\n".format(sim_list[i].sim_name, sim_list[i].mesh.CAS_name, current_date, sim_list[i].results.convergence))
        csvfile.close()