#%% Imports -------------------------------------------------------------------

import napari
import numpy as np
from skimage import io
from pathlib import Path

# Functions
from functions import process

#%% Comments ------------------------------------------------------------------

'''
- Some bugs regarding rescaling with rf = 0.5 (ozp data)
'''

#%% Inputs --------------------------------------------------------------------

# Paths
data_path = Path("D:\local_CapsSeg\data")
expl_path = Path("D:\local_CapsSeg\examples")
img_paths = (
    list(data_path.glob("**/*.jpg")) + 
    list(data_path.glob("**/*.png")) +
    list(data_path.glob("**/*.tif"))
    )
model_cores_path = Path(Path.cwd(), "model_cores_edt_512_gamma")
model_shell_path = Path(Path.cwd(), "model_shell_edt_512_gamma")

# Parameters
nImg = 10
rf = 1
overlap = 256

#%% Execute -------------------------------------------------------------------

if __name__ == "__main__":
    
    img_idxs = np.random.choice(
        range(len(img_paths) + 1),
        size=nImg, replace=False
        )

    for img_idx in img_idxs:
    
        path = img_paths[img_idx]
    
        outputs = process(
            path, overlap,
            model_cores_path,
            model_shell_path,
            rf=rf, save=False
            )
        
        # Save
        img_path = Path(expl_path, (path.stem + "_img.tif"))
        display_path = Path(expl_path, (path.stem + "_display.png"))
        io.imsave(img_path, outputs["img"])
        io.imsave(display_path, outputs["rgbDisplay"])
    
