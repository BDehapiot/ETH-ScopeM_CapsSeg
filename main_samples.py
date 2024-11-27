#%% Imports -------------------------------------------------------------------

import numpy as np
from skimage import io
from pathlib import Path

# Functions
from functions import process

#%% Inputs --------------------------------------------------------------------

# Paths
data_path = Path("D:\local_CapsSeg\data")
smpl_path = Path("D:\local_CapsSeg\samples")
img_paths = (
    list(data_path.glob("**/*.jpg")) + 
    list(data_path.glob("**/*.png")) +
    list(data_path.glob("**/*.tif"))
    )
model_cores_path = Path(Path.cwd(), "model_cores_edt_512_gamma")
model_shell_path = Path(Path.cwd(), "model_shell_edt_512_gamma")

# Parameters
nImg = 50
rf = 1
overlap = 256

#%% Execute -------------------------------------------------------------------

if __name__ == "__main__":
    
    np.random.seed(42)
    idxs = np.random.choice(
        range(len(img_paths) + 1),
        size=nImg, replace=False
        )
    
    for idx in idxs:
        
        path = img_paths[idx]
                
        outputs = process(
            path, overlap,
            model_cores_path,
            model_shell_path,
            rf=rf, save=False
            )
        
        img_path = Path(smpl_path, (path.stem + ".tif"))
        io.imsave(img_path, outputs["img"])
        display_path = Path(smpl_path, (path.stem + "_display_01.png"))
        io.imsave(display_path, outputs["rgbDisplay"])
    
