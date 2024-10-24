#%% Imports -------------------------------------------------------------------

import numpy as np
from skimage import io
from pathlib import Path
from functions import preprocess_image
from bdtools.patch import extract_patches

np.random.seed(42)

#%% Comments ------------------------------------------------------------------

'''
keyence (old) : 0.268 pixel / µm --> 3.7313 µm per pixel
ozp     (new) : 0.160 pixel / µm --> 6.2500 µm per pixel
'''

#%% Inputs --------------------------------------------------------------------

# Path
data_path = Path("D:\local_CapsSeg\data")
train_path = Path(Path.cwd(), 'train')
img_paths = list(data_path.glob("**/*.jpg"))

# Selection
nImg = 20  # number of images
nPatch = 1  # number of patch(es) extracted per image 
size = 1024 # size of extract patches
overlap = 0 # overlap between patches

#%% Extract -------------------------------------------------------------------

img_idxs = np.random.choice(
    range(0, len(img_paths)), size=nImg, replace=False)

for img_idx in img_idxs:
    
    path = img_paths[img_idx]
        
    # Open & preprocess image
    img = io.imread(path)
    img = np.mean(img, axis=2) # RGB to float
    img = preprocess_image(img)
    
    # Extract patches
    patches = extract_patches(img, size, overlap)
    
    # Select & save patches
    patch_idxs = np.random.choice(
        range(0, len(patches)), size=nPatch, replace=False)
    
    for patch_idx in patch_idxs:
        patch = patches[patch_idx]
        if "keyence" in str(path.resolve()):
            name = path.name.replace(".jpg", f"_pk{patch_idx:02d}.tif")
        elif "ozp" in str(path.resolve()):
            name = path.name.replace(".jpg", f"_po{patch_idx:02d}.tif")
        io.imsave(
            Path(train_path, name),
            patch.astype("float32"),
            check_contrast=False
            )
    