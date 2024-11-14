#%% Imports -------------------------------------------------------------------

import numpy as np
from skimage import io
from pathlib import Path

# Functions 
from functions import preprocess_image

# bdmodel
from bdmodel.predict import predict

# skimage
from skimage.trasform import rescale

#%% Inputs --------------------------------------------------------------------

# Paths
path = Path(Path.cwd(), "data", "240611-12_2 merged_pix(13.771)_00.tif")
model_path = Path(Path.cwd(), "model_mass")

# Pixel size
pixSize_key = 3.731 # reference
pixSize_o10 = 2.347
pixSize_o06 = 3.676

#%% Execute -------------------------------------------------------------------

if __name__ == "__main__":
    
    # Open & preprocess image
    img = io.imread(path)
    img = np.mean(img, axis=2) # RGB to float
    img = preprocess_image(img)
    
    # Rescale images
    if "keyence" in str(path.resolve()):
        pass
    if "ozp" in str(path.resolve()):
        if "mag10" in str(path.resolve()):
            img = rescale(img, pixSize_o10 / pixSize_key)
        if "mag06" in str(path.resolve()):
            img = rescale(img, pixSize_o06 / pixSize_key)
    
    # Predict
    prds = predict(        
        img,
        model_path,
        img_norm="image",
        patch_overlap=0,
        )
    
    # Display
    import napari
    viewer = napari.Viewer()
    viewer.add_image(img)
    viewer.add_image(prds)