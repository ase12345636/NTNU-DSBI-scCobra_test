import scanpy as sc

data = "/Group16T/raw_data/scCobra/Lung_atlas_public.h5ad"

adata = sc.read_h5ad(data)
print(adata)