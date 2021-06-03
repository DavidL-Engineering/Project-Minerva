import os

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
    
    def __init__(self, convergence = None, iterations = None, drag_tot = None, drag_comp = None, lift_tot = None, lift_comp = None, f_left = None, f_right = None, mom_roll = None, mom_pitch = None, mom_yaw = None):
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
        sim_param = Simulation(line[0], sim_mesh, sim_dimensions, sim_workflow)

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

def results_dir(sim_list: list, proj_params):
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


def komega_setup(simulation, processes):
    '''
    Performs setup of Fluent module with K-W solution method.

    Parameters
    ---------------------
    simulation : Simulation object
        Instance of Simulation object.

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


def tsst_setup(simulation, processes):
    '''
    Performs setup of Fluent module with T-SST solution method.

    Parameters
    ---------------------
    simulation : Simulation object
        Instance of Simulation object.

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