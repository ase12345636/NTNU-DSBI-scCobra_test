from method.raw import raw
from method.Harmony import Harmony
from method.scVi import scVi
from utils.preprocess import filter_cells_type1
from utils import metrics
import os
import pandas as pd

data = "/Group16T/raw_data/scCobra/Immune_ALL_human.h5ad"
out_path = "/Group16T/common/ccuc/scCobra/result/immune/"
batch = 'batch'
celltype = 'final_annotation'
adata = filter_cells_type1(data)

# ensure dataset result folder exists
os.makedirs(out_path, exist_ok=True)

# Aggregated metrics file per dataset
metrics_csv = os.path.join(out_path, "metrics.csv")
if os.path.exists(metrics_csv):
	combined = pd.read_csv(metrics_csv, index_col=0)
else:
	combined = pd.DataFrame()

# raw
adata_copy = adata.copy()
adata_res = raw(adata_copy, out_path, batch, celltype)
# ensure metrics functions find the expected keys
adata_res.obs['celltype'] = adata_res.obs[celltype]
adata_res.obs['BATCH'] = adata_res.obs[batch]
_, res_df = metrics.evaluate_dataset(adata_res, method="raw", n_celltype=adata_res.obs[celltype].nunique())
if combined.empty:
	combined = res_df
else:
	combined = combined.join(res_df, how='outer')
combined.to_csv(metrics_csv)

# Harmony
adata_copy = adata.copy()
adata_res = Harmony(adata_copy, out_path, batch, celltype)
adata_res.obs['celltype'] = adata_res.obs[celltype]
adata_res.obs['BATCH'] = adata_res.obs[batch]
_, res_df = metrics.evaluate_dataset(adata_res, method="harmony", n_celltype=adata_res.obs[celltype].nunique())
combined = combined.join(res_df, how='outer')
combined.to_csv(metrics_csv)

# scVI
adata_copy = adata.copy()
adata_res = scVi(adata_copy, out_path, batch, celltype)
adata_res.obs['celltype'] = adata_res.obs[celltype]
adata_res.obs['BATCH'] = adata_res.obs[batch]
_, res_df = metrics.evaluate_dataset(adata_res, method="scvi", n_celltype=adata_res.obs[celltype].nunique())
combined = combined.join(res_df, how='outer')
combined.to_csv(metrics_csv)

data = "/Group16T/raw_data/scCobra/Lung_atlas_public.h5ad"
out_path = "/Group16T/common/ccuc/scCobra/result/lung/"
batch = 'batch'
celltype = 'cell_type'
adata = filter_cells_type1(data)

os.makedirs(out_path, exist_ok=True)
metrics_csv = os.path.join(out_path, "metrics.csv")
if os.path.exists(metrics_csv):
	combined = pd.read_csv(metrics_csv, index_col=0)
else:
	combined = pd.DataFrame()

adata_copy = adata.copy()
adata_res = raw(adata_copy, out_path, batch, celltype)
# ensure metrics functions find the expected keys
adata_res.obs['celltype'] = adata_res.obs[celltype]
adata_res.obs['BATCH'] = adata_res.obs[batch]
_, res_df = metrics.evaluate_dataset(adata_res, method="raw", n_celltype=adata_res.obs[celltype].nunique())
if combined.empty:
	combined = res_df
else:
	combined = combined.join(res_df, how='outer')
combined.to_csv(metrics_csv)

adata_copy = adata.copy()
adata_res = Harmony(adata_copy, out_path, batch, celltype)
adata_res.obs['celltype'] = adata_res.obs[celltype]
adata_res.obs['BATCH'] = adata_res.obs[batch]
_, res_df = metrics.evaluate_dataset(adata_res, method="harmony", n_celltype=adata_res.obs[celltype].nunique())
combined = combined.join(res_df, how='outer')
combined.to_csv(metrics_csv)

adata_copy = adata.copy()
adata_res = scVi(adata_copy, out_path, batch, celltype)
adata_res.obs['celltype'] = adata_res.obs[celltype]
adata_res.obs['BATCH'] = adata_res.obs[batch]
_, res_df = metrics.evaluate_dataset(adata_res, method="scvi", n_celltype=adata_res.obs[celltype].nunique())
combined = combined.join(res_df, how='outer')
combined.to_csv(metrics_csv)


data = "/Group16T/raw_data/scCobra/human_pancreas_norm_complexBatch.h5ad"
out_path = "/Group16T/common/ccuc/scCobra/result/pancreas/"
batch = 'tech'
celltype = 'celltype'
adata = filter_cells_type1(data)

os.makedirs(out_path, exist_ok=True)
metrics_csv = os.path.join(out_path, "metrics.csv")
if os.path.exists(metrics_csv):
	combined = pd.read_csv(metrics_csv, index_col=0)
else:
	combined = pd.DataFrame()

adata_copy = adata.copy()
adata_res = raw(adata_copy, out_path, batch, celltype)
adata_res.obs['celltype'] = adata_res.obs[celltype]
adata_res.obs['BATCH'] = adata_res.obs[batch]
_, res_df = metrics.evaluate_dataset(adata_res, method="raw", n_celltype=adata_res.obs[celltype].nunique())
if combined.empty:
	combined = res_df
else:
	combined = combined.join(res_df, how='outer')
combined.to_csv(metrics_csv)

adata_copy = adata.copy()
adata_res = Harmony(adata_copy, out_path, batch, celltype)
adata_res.obs['celltype'] = adata_res.obs[celltype]
adata_res.obs['BATCH'] = adata_res.obs[batch]
_, res_df = metrics.evaluate_dataset(adata_res, method="harmony", n_celltype=adata_res.obs[celltype].nunique())
combined = combined.join(res_df, how='outer')
combined.to_csv(metrics_csv)

adata_copy = adata.copy()
adata_res = scVi(adata_copy, out_path, batch, celltype)
adata_res.obs['celltype'] = adata_res.obs[celltype]
adata_res.obs['BATCH'] = adata_res.obs[batch]
_, res_df = metrics.evaluate_dataset(adata_res, method="scvi", n_celltype=adata_res.obs[celltype].nunique())
combined = combined.join(res_df, how='outer')
combined.to_csv(metrics_csv)
