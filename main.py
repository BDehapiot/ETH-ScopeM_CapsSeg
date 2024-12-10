#%% Imports -------------------------------------------------------------------

import napari
from pathlib import Path

# Functions
from functions import process

#%% Comments ------------------------------------------------------------------

#%% Inputs --------------------------------------------------------------------

# Paths
data_path = Path(Path.cwd(), "data", "test")
img_name = "all" # image name or "all" for batch processing

# Parameters
rf = 1
overlap = 256
save = False

#%% Execute -------------------------------------------------------------------

if __name__ == "__main__":

    model_cores_path = Path(Path.cwd(), "model_cores_edt_512_gamma")
    model_shell_path = Path(Path.cwd(), "model_shell_edt_512_gamma")      

    if img_name == "all":
        img_paths = (
            list(data_path.glob("**/*.jpg")) + 
            list(data_path.glob("**/*.png")) +
            list(data_path.glob("**/*.tif"))
            )
    else:
        img_paths = list(data_path.rglob(f"*{img_name}*"))

    for path in img_paths:
        
        if "display.png" not in path.name:

            outputs = process(
                path, overlap,
                model_cores_path,
                model_shell_path,
                rf=rf, save=save
                )
    
    if len(img_paths) == 1:
    
        # Display
        viewer = napari.Viewer()
        viewer.add_image(
            outputs["img"], name="image", contrast_limits=(0, 1), opacity=0.33)
        viewer.add_image(
            outputs["sProbs"], name="sProbs", contrast_limits=(0, 1), 
            blending="additive", colormap="yellow", visible=False
            )
        viewer.add_image(
            outputs["cProbs"], name="cProbs", contrast_limits=(0, 1), 
            blending="additive", colormap="cyan", visible=False
            )
        viewer.add_image(
            outputs["sDisplay"], name="sDisplay", contrast_limits=(0, 255), 
            blending="additive", colormap="yellow"
            )
        viewer.add_image(
            outputs["cDisplay"], name="cDisplay", contrast_limits=(0, 255),
            blending="additive", colormap="cyan"
            )
