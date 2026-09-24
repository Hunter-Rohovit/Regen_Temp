import json
import numpy as np
import shutil
import pandas as pd
from pathlib import Path
from scipy.interpolate import PchipInterpolator


# --- 1. GET CONTINUOUS CONTOUR --- (Will allow us to set dX manually later)
contour_file = Path(__file__).parent / "current_contour.csv"
data = pd.read_csv(contour_file)

z_raw = data["Z_Coordinate_in"].to_numpy()
r_raw = data["R_Coordinate_in"].to_numpy()
interpContour = PchipInterpolator(z_raw, r_raw)


# --- 2. SET DZ & GENERATE A NEW CSV TO BE USED IN SOLVERS--- 

dz = 0.01 #in, this is the step size that will be used in all of the code

z = np.arange(z_raw[0],z_raw[-1],dz)
r = interpContour(z)






# --- 2. UPLOAD GEOMETRY TO DESIGN DATABASE --- (Manually Upload If Design Is Good)
# Save a copy of contour parameters JSON file to next Design # Folder
# Save a copy of Optimized Contour CSV file to next Design # Folder
def uploadToDesigns():

    geometry_dir = Path(__file__).parent
    designs_dir = geometry_dir / "Designs"

    # Find next design number
    design_numbers = [
        int(folder.name.replace("Design", ""))
        for folder in designs_dir.glob("Design*")
        if folder.is_dir()
    ]

    next_design = max(design_numbers, default=0) + 1

    # Create new design folder
    design_dir = designs_dir / f"Design{next_design}"
    design_dir.mkdir()

    # Copy current contour parameters
    shutil.copy(
        geometry_dir / "current_parameters.json",
        design_dir / "contour_parameters.json"
    )

    # Copy current optimized contour
    shutil.copy(
        geometry_dir / "current_contour.csv",
        design_dir / "optimized_contour.csv"
    )

    print(f"Design{next_design} saved to: {design_dir}")