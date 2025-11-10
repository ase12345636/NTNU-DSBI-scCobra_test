import scanpy as sc
from utils.plot import plot

def raw(adata, out_path, batch, celltype):
    """Raw (no-integration) pipeline: compute PCA, set a standard embedding key and plot.

    Returns the adata used for plotting (with embedding at `obsm['X_emb']`).
    """
    out_path = out_path + "raw"

    # compute PCA embedding and set standard embedding name used by metrics
    sc.tl.pca(adata)
    # ensure a standardized embedding key for downstream metrics
    if 'X_pca' in adata.obsm:
        adata.obsm['X_emb'] = adata.obsm['X_pca']

    plot(adata, None, batch, celltype, out_path)
    return adata