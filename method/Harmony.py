import scanpy as sc
from harmony import harmonize
from utils.plot import plot

def Harmony(adata, out_path, batch, celltype):
    out_path = out_path + "harmony"

    sc.tl.pca(adata)

    adata.obsm['X_pca_harmony'] = harmonize(
        adata.obsm['X_pca'],
        adata.obs,
        batch_key=batch,
    )

    plot(adata, "X_pca_harmony", batch , celltype, out_path)