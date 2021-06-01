# pyraabe-fromen
This project offers a graphical user interface (GUI) and extended features over PyRaabe v0.1.0. It includes most of the original functionality and additional functions to retrieve the coordinates of each point in the centerline output.

![](resources/pyraabe-fromen-icon.ico)

## Disclaimer
This project is not affiliated with the original PyRaabe project, its developers, or their respective organizations. For more information about PyRaabe, please see https://github.com/pnnl/pyraabe.

# Features
- Save Raabe table as CSV
- Save centerline coordinates as CSV
- Indicate extruded inlet option
- Output console in GUI window
- Indicate when the calculation is complete
- Save a default gravity vector (Edit > Set default vector)

## On hold
- Merging multiple results into one Raabe table

# Usage 
You can run this program without having Python installed on your computer. Check the releases [here](https://github.com/fromenlab/pyraabe-gui/releases) for a version compatible with your operating system. Download the `.zip` file, extract the contents, and look for `pyraabe-fromen.exe`. Create a shortcut to this file and place it in a convenient location on your computer.

1. Select the STL file for input
2. Select a folder to save the CSV files and centerline data
3. Provide a gravity vector for Raabe table calculations
4. Indicate whether the model inlet has been artificially extended. (This will impact the Raabe table but not the centerline output.)
5. Click "Run" and follow the prompts


## Observations
- Setting outlets manually runs faster than allowing the program to find them automatically
- Higher triangle count takes more time to compute
- Isotropic mesh (aspect ratio ~1) gives better results (smoother centerline and more accurate dimensions)
    - This type of mesh can be achieved from software output or by remeshing
- Subdivision may not improve results on a remeshed model

# Citation
If you find this program useful and use it for your work, please cite it. Please also cite the original project according to their preferences:

- PyRaabe, version 0.1.0 http://github.com/pnnl/pyraabe (accessed MMM YYYY)