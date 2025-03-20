# Installation Instructions for packages required within the ESM track exercise block

The ESM track exercises will require several Python packages that were developed by IEK-3 at FZJ Juelich research center. For this course, these packages have been made available as open-source software from the conda channel 'conda-forge', the installation procedure for the required packages is explained below.

**NOTE:** The conda installation (step #1) should be known from your Python course at UAM, please refer to the course in case of questions. The instructions here will only be about the installation of an environment with all required IEK-3 packages for the ESM exercise course, once a working conda setup is in place. 

## 1) Install conda

Install conda first (refer to your Python course for details).

Test: Open a command line tool (e.g. Anaconda Prompt) and enter ```conda env list```. The return should show (at least) the ‘base’ environment and where it is installed:

![](../../../../internal_files/installation_instructions_preparation/conda_list_check.png)


## 2) Create a new conda environment

Go to your console where you can execute conda (e.g. Anaconda Prompt) and create a new environment that we will name 'GradSchoolESM': 

```conda create --name GradSchoolESM```

(Confirm with ```y``` and hit Enter when it asks you to confirm the environment location.)

When you now run ```conda env list``` again, it should show the new 'GradSchoolESM' environment, too:

![](../../../../internal_files/installation_instructions_preparation/conda_env_list.png)

The little asterisk (*) shows you which environment is currently active, but that information is displayed in parenthesis at the beginning of each command line '(base)' in most tools as well.


## 3) Activate the new environment

The new environment is now activated by entering the command: 

```conda activate GradSchoolESM```

As said before, the currently active environment is shown in parenthesis at the beginning of your command line (compare below and the earlier step above):

![](../../../../internal_files/installation_instructions_preparation/conda_env_activated.png)

This activation is a very important step that you need to do **every time** before you install anything or work with your environment!

## 4) Install the Python packages

The packages 'geokit', 'glaes', 'RESKit' and 'FINE' are Python packages developed at IEK-3. 'geokit' is an auxiliary package that contains geospatial methods for Python which are used in all the other packages. 'glaes' is used for land eligibility analyses and RESKit for the simulation of energy yields. 'FINE' is the framework used to build energy system models. More information on all packages can be found when googeling for 'github FZJ' + the respective package name.

**NOTE:** The following step needs an internet connection and will download a considerable amount of data!

All packages can be installed via ```conda install``` from a conda channel. This can even be done all at once in a single line command. Therefore enter into your command line with the new environment activated:

```conda install geokit glaes reskit fine -c conda-forge```

You will be asked to confrm a list of package installations and updates, please do so by entering ```y``` and hitting Enter.

**NOTE:** The first step can take a long time, and it may be that solving the environment fails mutiple times in the process. This does not matter as long as it works in the end! The installation will be complete when the command line is ready to receive new commands again, a few seconds after 'Executing transaction: done' was displayed. 

You can now test within the console if the installation worked. This test can be repeated for all other packages, simply exchange 'geokit' below with the particular package name.
- Enter ```python```. Another command line within a python environment will open.
- Enter ```import geokit```. The return should be nothing (no error message); the next line will start with '>>>'. 
- You can try the same import for the other packages: 'glaes', 'reskit' and 'FINE'.
- Enter ```exit()```. This will close the Python environment and take you back.


## 5) Copy the exercise data to your local computer and create a results folder

**NOTE:** The following steps will be done together at the beginning of the exercise week!

First create a folder where you wish to save the exercise data. **Note:** The path must be **short** so please do not create too many sub folders (else you will get an error below when cloning or copying the long dataset filenames, if so, re-create the folder at another location with shorter absolute filepath)

Then simply copy and paste the "student_files" folder of the WASCAL Graduate School ESM track from USB (will be provided at the beginning of the exercise week) into this main folder.

## 6) Create a "results" folder

Create a 'results' folder somewhere on your computer. It should **not** be inside the "student_folder" but could for example be in the same parent folder. This folder is where the temporary output files from the exercises will be created.