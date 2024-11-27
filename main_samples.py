#%% Imports -------------------------------------------------------------------

from skimage import io
from pathlib import Path

# Functions
from functions import process

#%% Inputs --------------------------------------------------------------------

# Paths
smpl_path = Path("D:\local_CapsSeg\samples\keyence")
img_paths = (
    list(smpl_path.glob("**/*.jpg")) + 
    list(smpl_path.glob("**/*.png")) +
    list(smpl_path.glob("**/*.tif"))
    )
model_cores_path = Path(Path.cwd(), "model_cores_edt_512_gamma")
model_shell_path = Path(Path.cwd(), "model_shell_edt_512_gamma")

# Parameters
nImg = 50
rf = 1
overlap = 256

#%% Execute -------------------------------------------------------------------

if __name__ == "__main__":
    
    for path in img_paths:
                        
        outputs = process(
            path, overlap,
            model_cores_path,
            model_shell_path,
            rf=rf, save=False
            )
        
        display_path = Path(smpl_path.parent, (path.stem + "_display_01.png"))
        io.imsave(display_path, outputs["rgbDisplay"])
    
