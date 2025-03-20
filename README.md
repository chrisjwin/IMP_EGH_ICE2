# WASCAL Graduate School - ESM track

This repository serves to collect all data, scripts and files regarding the practical exercises for the ESM track in the WASCAL graduate school.

The repository contains 2 main folders:

- student_files
- internal_files

The student_files folder will be downloaded and given to the students for their exercises 'as is'. It will contain data, scripts and instructions, plus an empty folder for 'results'. 

The internal folder contains all other pre-processing etc. scripts that should be kept for reproduction and adaptation in the future. It could also contain lecture data (slides etc.) in the future if needed, to store all ESM track lecture content in a single place. The students will **not** get any files from the internal folder. 

## Some conventions for Python scripts and data for practical exercises

1) **Please name your exercise folder according to Heidis lecture units**

In Heidis GEARS shared folder on Sciebo: "GEARS\04_IMP-EGH_track6_EnergySystemsModelingAndScenarioGeneration\LectureSlides" she listed all units with numbers and short names that are also used in other folders (such as e.g.: "Unit_1_IntroductionInEnergySystemsModeling"). Please use the same folder names within the "student_files/exercises" parent folder to keep consistency for the students.

2) **Please use the Powerpoint template for the exercise instructions**

The exercises should be described in a consistent and self-explaining way, one slide per sub task within your exercise. The template was attached to Heidi's mail, you can also find it in the internal_files folder under this path: "./internal_files/templates/Unit_XYZ_Exercise_ExerciseShortTitle.pptx"

3) **Please use only Jupyter Notebook (.ipynb) files for the student exercises**

The reasons are manifold, the main points are:
- Each step can be executed in individual cells and the interim output variables can be accessed between each cell step
- Graphical plots can be generated and accessed on the fly within the same script
- We should restrict ourselves to a single platform to minimize installation time/effort for us and complexity for the students
- Jupyter Notebook is very simple to install and execute for students with little knowledge 

4) **All scripts should please use relative paths in combination with a single base path**

Please define input and output base folders at the top of the script and use structures relative to the file position 
instead of hard code. One option for e.g. the results folder (but similarly for the data etc. folder) could look like
this in a Jupyter notebook (executed from within a .ipynb in /student_files/exercises/):

```python
# NOTE: The results folder exists in your repo under /student_files/results/, but the files created therein will not be pushed back to git

# this is the current working directory ("student_files/exercises")
cwd = pathlib.Path().cwd()
print(f"Current working directory: {cwd}")

# the results folder is in "student_files/results", so go "2 folders up"
results_folder = os.path.join(os.path.dirname(os.path.dirname(cwd)), 'results')
# make sure folder exists
assert os.path.isdir(results_folder), f"results folder does not exist: '{results_folder}'"

print(f"Results folder:", results_folder)
```

The reason is that students will have to execute the exercise scripts on their own notebooks and will therefore download the data to individual main folders and also save to individual folders. This relative path concept will allow the students to run all notebooks in the practical exercises. 


5) **Please use the existing data folder structures**

- If data may be used by others as well, please save it in the "student_files/data" folder. Ergo, if you need some data, please check first if it is already available in the respective folder.
- Else you are welcome to create an own input data folder within student_files/data with a descriptive name so others can find your data as well.
- Do not use space characters in folder/file names.
