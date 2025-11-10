import scvi
from utils.plot import plot

def scVi(adata, out_path, batch, celltype):
    out_path = out_path + "scvi"

    # work on a copy and return it so main can evaluate metrics
    adata = adata.copy()

    scvi.model.SCVI.setup_anndata(adata, batch_key = batch)
    model = scvi.model.SCVI(adata)
    model.train()
    adata.obsm["X_scVI"] = model.get_latent_representation()

    # standardize embedding key for metrics
    adata.obsm['X_emb'] = adata.obsm['X_scVI']

    plot(adata, "X_scVI", batch , celltype, out_path)
    return adata
