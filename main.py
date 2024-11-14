#%% Imports -------------------------------------------------------------------

import napari
from pathlib import Path

# Functions
from functions import process

#%% Comments ------------------------------------------------------------------

'''
- Add gamma (before at 0.5) to edt mask in bdmodel.functions.preprocess() and retrain
- Some bugs regarding rescaling with rf = 0.5 (ozp data)
- Find a way to discard border objects in ozp data (diaphragm)
'''

#%% Inputs --------------------------------------------------------------------

# Paths
data_path = Path("D:\local_CapsSeg\data")
img_paths = (
    list(data_path.glob("**/*.jpg")) + 
    list(data_path.glob("**/*.png")) +
    list(data_path.glob("**/*.tif"))
    )
model_cores_path = Path(Path.cwd(), "model_cores_edt_512")
model_shell_path = Path(Path.cwd(), "model_shell_edt_512")

# Parameters
img_idx = 900
rf = 0.5
overlap = 128

#%% Execute -------------------------------------------------------------------

if __name__ == "__main__":
    
    path = img_paths[img_idx]
    
    outputs = process(
        path, overlap,
        model_cores_path,
        model_shell_path,
        rf=1, save=True
        )
    
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