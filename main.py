#%% Imports -------------------------------------------------------------------

import napari
from pathlib import Path

# Functions
from functions import process

#%% Comments ------------------------------------------------------------------

'''
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
model_cores_path = Path(Path.cwd(), "model_cores_edt_512_gamma")
model_shell_path = Path(Path.cwd(), "model_shell_edt_512_gamma")

# Parameters
img_idx = 369
rf = 1
overlap = 256

#%% Execute -------------------------------------------------------------------

if __name__ == "__main__":

    path = img_paths[img_idx]
    
    outputs = process(
        path, overlap,
        model_cores_path,
        model_shell_path,
        rf=rf, save=False
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
    
#%%
    
    # from skimage.filters import gaussian
    # from skimage.morphology import disk, binary_dilation
    # from skimage.segmentation import clear_border
    
    # img = outputs["img"]
    # cLabels = outputs["cLabels"]
    # sLabels = outputs["sLabels"]
    # msk = img != img[0, 0]
    # msk = gaussian(msk, sigma=50) > 0.99
    # # msk = binary_dilation(msk, footprint=disk(10))
    
    # # Display
    # viewer = napari.Viewer()
    # viewer.add_image(img)  
    # viewer.add_image(msk, blending="additive") 
    # viewer.add_labels(cLabels, blending="additive") 
    # viewer.add_labels(sLabels, blending="additive") 
    # # viewer.add_image(img_grd_msk) 
