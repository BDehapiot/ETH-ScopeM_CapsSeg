#%% Imports -------------------------------------------------------------------

from pathlib import Path

# Functions 
from functions import preprocess_image

# bdmodel
from bdmodel.predict import predict

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

#%% Execute -------------------------------------------------------------------

if __name__ == "__main__":
    
    path = img_paths[img_idx]
    
    # Open & preprocess image
    img = preprocess_image(path)
        
    # Predict
    cProbs = predict(        
        img, model_cores_path,
        img_norm="image", patch_overlap=256, 
        )
    sProbs = predict(        
        img, model_shell_path,
        img_norm="image", patch_overlap=256,
        )
    
    # Display
    import napari
    viewer = napari.Viewer()
    viewer.add_image(img, name="image", blending="additive", opacity=0.33)
    viewer.add_image(cProbs, blending="additive", colormap="cyan")
    viewer.add_image(sProbs, blending="additive", colormap="yellow")