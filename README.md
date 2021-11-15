# Project Description

Project Minerva is a collection of tools designed to support workflow automation as part of the Gen 11/12 cycle. Written in Python, it is the successor of Project Liber, and is designed to be used with ANSYS 2020 R1. 

Project Minerva is able to automate the following aspects of the simulation workflow

- ANSYS Workbench project initialization
- ANSYS Fluent module creation
- `.CAS` file importing and set-up
- ANSYS Fluent simulation convergence detection
- ANSYS Fluent simulation results exporting
- Simulation results aggregation and formatting
- Post-processing in ANSYS CFD-Post comprising of:
    - 3D Cp Contours
    - Pressure Contours
    - Turbulent Kinetic Energy Contours
    - Wall Shear Streamlines
    - Streamline Animations
    - Centerline Cp Polylines
    - Cp vs. X Coordinate Graphs over the Centerline
    - Cp vs. X Coordinate Tabulations over the Centerline
- ANSYS Workbench project archiving to the archive in the Aero Network Drive

# Requirements

## Aerobody CAD Requirements

It is assumed that the Cartesian coordinate system for the car is as follows (Gen 11 CAD Convention):

- Positive x in length-wise direction of car, pointing to the trailing edge.
- Positive y in width-wise direction of car, pointing to the right side of the car.
- Positive z in height-wise direction of car, pointing to upper section of car.
- x-axis aligned with length-wise centre-line of car, with nose beginning at x=0
- y-axis perpendicular to length-wise centre-line of car, with length-wise centre-line beginning at y=0

## Mesh Requirements

Boundary Conditions:

- Inlet name: inlet
- Road (wall) name: road
- Wall (wall) name: wall

## File Name Requirements

Only alphanumeric characters and spaces are permitted for user-created `.CAS` files, simulation names, project names, archive names, and directories.

# Installation Details

### Prerequisites

1. Python 3.9+
2. Microsoft Office (Excel)

### Location

The most up-to-date version of Project Minerva can be found on GitHub: 

[https://github.com/DavidL-Engineering/Project-Minerva](https://github.com/DavidL-Engineering/Project-Minerva)

### Installation

Navigate to the GitHub repository linked above and click the green code download icon and download as a ZIP file to a location of your choice.

![https://i.imgur.com/ZmDMLF6.gif](https://i.imgur.com/ZmDMLF6.gif)

Figure 1. Download of GitHub Repository as ZIP file.

Upon downloading the ZIP file, extract its contents into a location of your choice. This can be done by simply dragging and dropping the contents to a different folder, or copy and pasting the contents to a different folder.

When using Project Minerva, copy **all** the relevant files to the desired location.

# Interface-Structure

Project Minerva's data entry is accomplished entirely through CSV files that may be opened in Excel. 

The Python files that generate the CSV files are designed to be run every time the CSV file is intended to be filled out. This is because there are pre-filled entries (such as the number of Fluent Processes to use) which are determined on a real-time and per-machine basis. **If you are entering data into the CSV, always run the relevant CSV generating script before doing so.**

# Automated Simulation & Post-Processing Workflow

## Description

The overall ANSYS Fluent simulation workflow is automated using the collection of tools explained in the instructions below.

Aspects included are:

- ANSYS Workbench project initialization
- ANSYS Fluent module creation
- `.CAS` file importing and set-up
- ANSYS Fluent simulation convergence detection
- ANSYS Fluent simulation results exporting
- Simulation results aggregation and formatting
- Post-processing in ANSYS CFD-Post comprising of:
    - 3D Cp Contours
    - Pressure Contours
    - Turbulent Kinetic Energy Contours
    - Wall Shear Streamlines
    - Streamline Animations
    - Centerline Cp Polylines
    - Cp vs. X Coordinate Graphs over the Centerline
    - Cp vs. X Coordinate Tabulations over the Centerline

Due to the nature of convergence status detection, it is not currently possible to automate the entire simulation to post-processing workflow in one continuous process. As a result, the Workbench project initialization and Fluent setup are automated as one continuous process and the data extraction and post-processing are automated as separate continuous process.

## Instructions for Use

Copy the following files from extracted contents of `Project-Minerva-master.zip` into a single folder:

- `generate_setup_csv.py`
- `full_journal.py`

### Project and Fluent Setup Automation

Double click `generate_setup_csv.py` to generate the CSV where simulation information will be entered. The CSV should be generated in the same folder as the other three Python files. If no CSV is generated, ensure that Python is installed. If Python is installed, navigate to the folder in which the newly copied files are stored and type `cmd` in the Windows Explorer address bar, which opens a command prompt. In the command prompt, type:

```python
python generate_setup_csv.py
```

The result of running this file should be the creation of a file titled `Simulation Parameters.csv` .

![https://i.imgur.com/8l8HpZ0.gif](https://i.imgur.com/8l8HpZ0.gif)

Figure 2. Alternative method of running `generate_setup_csv.py`.

Open `Simulation Parameters.csv` .

In this CSV, all information pertaining to each simulation must be entered. The properties of each simulation are to be entered on one row, with each row denoting a different simulation.

Columns A-N must be entered for every simulation.

Columns P-S are project parameters and **must be entered only once in row 2.**

In column A, enter the name of the simulation. E.g. `DV6 2D Canopy Variations A1`

In column B, enter the name of the `.CAS` file to be imported for that simulation. Do not include the `.CAS` file extension. E.g. `A1`

In column C, enter the directory in which the `.CAS` file is stored. Do not include the name and extension of the file itself. The directory may be found by navigating to the folder in which the `.CAS` file is stored, clicking and copying on the address bar in Windows Explorer, and pasting the address in the cell. E.g. `D:\David - Aero\DV6\DV6 2D Canopy Variations`

![https://i.imgur.com/bgEXkf2.gif](https://i.imgur.com/bgEXkf2.gif)

Figure 3. Obtaining the directory of the `.CAS` mesh file to be imported into Fluent.

In column D, enter the body type. Available options are half-body or full-body. E.g. `HB`

In column E, enter the desired solution method. The available options are k-omega SST and T-SST. E.g. `K-W` 

In column F, enter the override velocity for the inlet and the road in m/s. Leaving this blank will result in a velocity of 18.0 m/s being used. E.g. `27.0` 

In column G, enter the area of the aerobody in m^2. E.g. `15.155`

In column H, enter the length of the aerobody in m. E.g. `5.000618`

In column I, indicate whether you are providing a center of gravity (CG). Available options are yes (Y) or no (N). E.g. `N`

In columns J, K, and L, input the respective x, y, and z coordinates of the CG in metres. If no (N) was indicated in column I, these fields can be left empty.

In column M, indicate whether post-processing is desired. Available options are yes (Y) or no (N). E.g. `N`

In column N, indicate whether streamline animation is desired. Available options are yes (Y) or no (N). E.g. `N` **Note:** This field cannot be left blank, regardless of the answer in column L.

In column P, enter the name of the Workbench Project. This will be the name under which the Workbench Project will be saved. Do not include the Workbench file extension `.wbpj` or the archive extension `.wbpz`. This information only needs to be entered for the first row. E.g. `DV6 2D Canopy Variations ABC K-W`

In column Q, enter the directory of the location in which the Workbench Project should be saved. Do not include the name and extension of the file itself. The directory may be found by navigating to the folder in which the workbench file should be stored, clicking and copying on the address bar in Windows Explorer, and pasting the address in the cell. This information only needs to be entered for the first row. E.g. `D:\David - Aero\DV6\DV6 2D Canopy Variations`

In column R, enter the directory of the location in which the results should be saved. The directory may be found by navigating to the folder in which the results should be stored, clicking and copying on the address bar in Windows Explorer, and pasting the address in the cell. This information only needs to be entered for the first row. E.g. `D:\David - Aero\DV6\DV6 2D Canopy Variations`

In column S, the script has already generated the optimal number of processes with which the simulation should be run. This value is generated based on the computer's current configuration and **will vary between computers, such that it is best left alone**. It may be modified, but only after sufficient research and for very good reasons. This information only needs to be entered for the first row.

**NOTE:** This setting is the reason why `generate_setup_csv.py` must be run and a new CSV generated before every new simulation on any given computer.

After entering the project and simulation parameters in their respective cells, save the CSV file.

Open ANSYS Workbench 2020 R1, and navigate to File→ Scripting→Run Script File.

Click the drop-down menu labelled `Journal Files (.wbjn)` and select `Python Script Files (*.py)`.

Navigate to the directory where the two Python files and the current CSV file are stored, click on `full_journal.py`, and click OK.

The simulations should be setup and run automatically from this point on.

### Numerical and Post-Processing Results

The numerical results extracted from each of the converged simulations may be found in a file titled `$Project_Name$.csv`, where `$Project_Name$` is replaced by the name of the workbench project indicated in column P of the `Simulation Parameters.csv` file. This file is stored in the results directory inputted in column R of `Simulation Parameters.csv`.

Post-processing results are stored in the "Media Files" folder within each simulation's individual results folder. The individual simulation results folders are located in the results directory inputted in column R of `Simulation Parameters.csv`, with names identical to the names of the simulations inputted in column A of `Simulation Parameters.csv`.

# Automated Workbench Project Archival

## Description

The automated workbench project archival tool in Project Minerva is able to intake multiple existing workbench projects in different or identical directories on a single machine and archive them to the Aero Archive on the Blue Sky network drive.

## Instructions for Use

Copy the following files from extracted contents of `Project-Minerva-master.zip` into a single folder:

- `generate_archive_csv.py`
- `archive_journal.py`

### Workbench Project Archive Automation

Double click `generate_archive_csv.py` to generate the CSV where the workbench project information will be entered. The CSV should be generated in the same folder as the other three Python files. If no CSV is generated, ensure that Python is installed. If Python is installed, navigate to the folder in which the newly copied files are stored and type `cmd` in the Windows Explorer address bar, which opens a command prompt. In the command prompt, type:

```python
python generate_archive_csv.py
```

The result of running this file should be the creation of a file titled `ANSYS Batch Archive.csv`.

![https://i.imgur.com/yCWfeqr.gif](https://i.imgur.com/yCWfeqr.gif)

Figure 4. Alternative method of running `generate_archive_csv.py`.

Open `ANSYS Batch Archive.csv`.

In this CSV, all information pertaining to the workbench projects to be archived and their archive location must be entered. The properties of each project and archive metadata are to be entered on one row, with each row denoting a different project.

In column A, enter the directory in which the ANSYS Workbench project is located. E.g. `D:\David - Aero\DV6\DV6 2D Canopy Variations`

In column B, enter the name of the Workbench Project. This will be the name under which the Workbench Project is currently saved. Do not include the Workbench file extension `.wbpj` or the archive extension `.wbpz`. E.g. `D:\David - Aero\DV6\DV6 2D Canopy Variations`

In column C, enter the cycle during which the project was run. Ensure that the spelling and characters exactly match one of the available cycle folders in the archive. At the time of writing the cycle folders are `Gen X`, `Gen 11`, `Gen 12`. More folders may be added as needed during future cycles. E.g. `Gen 12`

In column D, enter the design series during which the project was run. Ensure that the spelling and characters exactly match one of the available series folders in the archive. If the folder for the desired design series does not exist, it may be created in the appropriate cycle's archive folder. E.g. `DV6`

In column E, enter the name of the archived workbench project file. This name may be different than the project's present name, such that if a different name is desired when archiving the project, column E is where this name should be specified. E.g. `DV6 2D Canopy Variation C FB T-SST Airflow`

Upon entering project and archive metadata parameters in their respective cells, save the CSV file.

Open ANSYS Workbench 2020 R1, and navigate to File→ Scripting→Run Script File.

Click the drop-down menu labelled `Journal Files (.wbjn)` and select `Python Script Files (*.py)`.

Navigate to the directory where the two Python files and the current CSV file are stored, click on `archive_journal.py`, and click OK.

The workbench projects should be opened and archived automatically from this point on.

The ANSYS Workbench progress bar may be enabled to see if the currently opened project is in the progress of being archived. If the progress bar does not show any running tasks and the current project is sitting open in ANSYS Workbench, the script has completed and the application may be closed.

### Example

If I were storing the Gen 11, DV5 Parsec 5 full-body simulations run using K-Omega with post-processing into the archive, the relevant row of the `ANSYS Batch Archive.csv` file would appear as follows:

In column A: `D:\David - Aero\DV5\DV6 Parsec 5`

In column B: `DV5 Parsec 5 FB K-W`

In column C: `Gen 11`

In column D: `DV5`

In column E: `DV5 Parsec 5 FB K-W Airflow`
