#%% Imports -------------------------------------------------------------------

import numpy as np
from skimage import io
from pathlib import Path

# bdtools
from bdtools.patch import extract_patches

# Functions
from functions import preprocess_image

np.random.seed(42)

#%% Comments ------------------------------------------------------------------

'''
keyence (old)   : --> 3.731 µm per pixel (0.268 pixel / µm)
ozp     (old)   : --> 6.250 µm per pixel (0.160 pixel / µm)
ozp     (mag10) : --> 2.347 µm per pixel
ozp     (mag06) : --> 3.676 µm per pixel
'''

#%% Inputs --------------------------------------------------------------------

# Paths
data_path = Path("D:\local_CapsSeg\data")
train_path = Path.cwd() / "data" / "train"
img_paths = (
    list(data_path.glob("**/*.jpg")) + 
    list(data_path.glob("**/*.png")) +
    list(data_path.glob("**/*.tif"))
    )

# Selection
nImg = 250  # number of images
nPatch = 10 # number of patch(es) extracted per image 
size = 1024 # size of extract patches
overlap = 0 # overlap between patches

#%% Extract -------------------------------------------------------------------

img_idxs = np.random.choice(
    range(0, len(img_paths)), size=nImg, replace=False)

for img_idx in img_idxs:
    
    path = img_paths[img_idx]
    
    if "mag06" in str(path):
    
        # Open & preprocess image
        img = preprocess_image(path)
        
        # Extract patches
        patches = extract_patches(img, size, overlap)
        
        # Select & save patches
        patch_idxs = np.random.choice(
            range(0, len(patches)), size=nPatch, replace=False)
        
        for patch_idx in patch_idxs:
            patch = patches[patch_idx]
            if "keyence" in str(path.resolve()):
                name = f"pkey_{img_idx:04d}_{patch_idx:02d}.tif"
            elif "ozp" in str(path.resolve()):
                if "mag10" in str(path.resolve()):
                    name = f"po10_{img_idx:04d}_{patch_idx:02d}.tif"
                if "mag06" in str(path.resolve()):
                    name = f"po06_{img_idx:04d}_{patch_idx:02d}.tif"
            io.imsave(
                Path(train_path, name),
                patch.astype("float32"),
                check_contrast=False
                )
    