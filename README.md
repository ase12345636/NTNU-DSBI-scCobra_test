## Data information

### scCobra_immune
```
data = "/Group16T/raw_data/scCobra/Immune_ALL_human.h5ad"
out_path = "/Group16T/common/ccuc/scCobra/result/immune/"
batch = 'batch'
celltype = 'final_annotation'
```

### scCobra_lung
```
data = "/Group16T/raw_data/scCobra/Lung_atlas_public.h5ad"
out_path = "/Group16T/common/ccuc/scCobra/result/lung/"
batch = 'batch'
celltype = 'cell_type'
```

### scCobra_pancreas
```
data = "/Group16T/raw_data/scCobra/human_pancreas_norm_complexBatch.h5ad"
out_path = "/Group16T/common/ccuc/scCobra/result/pancreas/"
batch = 'tech'
celltype = 'celltype'
```

## Method install

### scDML
```
conda create -n scDML python==3.8.12
git clone https://github.com/eleozzr/scDML
cd scDML
pip install .
```

### Harmony
```
pip install harmony-pytorch
```

### scVi
```
pip install scvi-tools
```