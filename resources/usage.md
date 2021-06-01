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