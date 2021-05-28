# pyraabe-gui
GUI and extended features over PyRaabe v0.1.0

# Features
- [x] Output Raabe table as CSV
- [x] Output centerline coordinates as CSV
- [] Checkbox for "extruded" option
- [] Console output to GUI window
- [] UI indicator that processing is complete
- [] User preferences for default gravity vector

## On hold
- [] Field for additional paths to merge (taken from GUI)
    - [] Take raw input of paths to merge, instead of looking in output directory
    - [] Option for custom suffix/ID on output files

# Observations
- Setting outlets manually runs faster than allowing the program to find them automatically
- Higher triangle count takes more time to compute
- Isotropic mesh (aspect ratio ~1) gives better results (smoother centerline and more accurate dimensions)
    - Can be achieved from software output or by remeshing
- Subdivision may not improve results on a remeshed model