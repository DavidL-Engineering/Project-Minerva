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
    def __init__(self, sol_method = None, CG = None, post = None, streamlines = None, results_dir = None, processes = None):
        self.sol_method = sol_method #Either K-W or T-SST
        self.CG = CG #Either True or False
        self.post = post #Either True or False
        self.streamlines = streamlines #True or False
        self.results_dir = results_dir
        self.processes = processes #integer

    def __str__(self):
        return "\n----WORKFLOW PROPERTIES----\nSolution method: {}\nCG: {}\nPost-Processing: {}\nStreamline Animations: {}\nResults located in: {}\nNumber of simulation processes: {}".format(self.sol_method, self.CG, self.post, self.streamlines, self.results_dir, self.processes)

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

        sim_workflow = Workflow_Properties(line[3], CG_bool, post_bool, streamlines_bool, line[12], line[13])
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

    proj_name = line[15]
    proj_dir = line[16]
    proj_dir = proj_dir.replace(os.sep, '/')

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

def fluent_sim_setup(sim_list):

    komega = ["komega", "k-omega", "k-w", "kw"]
    tsst = ["t-sst", "tsst"]

    for sim in sim_list:
        if sim.Workflow_Properties.sol_method.lower() in komega:
            komega_setup(sim)
        elif sim.Workflow_Properties.sol_method.lower() in tsst::
            tsst_setup(sim)


def komega_setup(simulation):
    
    template1 = GetTemplate(TemplateName="FLUENT")
    system1 = template1.CreateSystem()
    system1.DisplayText = simulation.sim_name
    setup1 = system1.GetContainer(ComponentName="Setup")
    fluentLauncherSettings1 = setup1.GetFluentLauncherSettings()
    fluentLauncherSettings1.SetEntityProperties(Properties=Set(Dimension="ThreeD", EnvPath={}, RunParallel=True, NumberOfProcessors=simulation.Workflow_Properties.processes))
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


def tsst_setup(simulation):
    template1 = GetTemplate(TemplateName="FLUENT")
    system1 = template1.CreateSystem()
    system1.DisplayText = simulation.sim_name
    setup1 = system1.GetContainer(ComponentName="Setup")
    fluentLauncherSettings1 = setup1.GetFluentLauncherSettings()
    fluentLauncherSettings1.SetEntityProperties(Properties=Set(Dimension="ThreeD", EnvPath={}, RunParallel=True, NumberOfProcessors=simulation.Workflow_Properties.processes))
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