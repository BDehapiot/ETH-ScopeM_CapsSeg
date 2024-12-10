#%% Imports -------------------------------------------------------------------

from pathlib import Path

# Functions
from functions import get_paths, merge_df

#%% Inputs --------------------------------------------------------------------

# Paths
data_path = Path(Path.cwd(), "data", "test")

# Path (selection)
tags_in = ["EM"]
tags_out = ["12-5"]
tagsStr = f"{tags_in}in_{tags_out}out"

#%% Execute -------------------------------------------------------------------

paths = get_paths(data_path, tags_in, tags_out)
sData_df_merged, cData_df_merged = merge_df(paths)
sData_df_merged_path = data_path / f"{tagsStr}_sData_merged.csv"
cData_df_merged_path = data_path / f"{tagsStr}_cData_merged.csv"
sData_df_merged.to_csv(sData_df_merged_path, index=False, float_format='%.3f')
cData_df_merged.to_csv(cData_df_merged_path, index=False, float_format='%.3f')