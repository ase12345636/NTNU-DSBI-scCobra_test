from utils.plot import plot
from utils.preprocess import filter_cells_type1

def raw(adata, out_path, batch, celltype):
    out_path = out_path + "raw"

    plot(adata, None, batch , celltype, out_path)