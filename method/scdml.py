from scDML import scDMLModel
from utils.plot import plot

def scdml(adata, out_path, batch, celltype):
    out_path = out_path + "scdml"

    adata.obs["batch_orig"] = adata.obs[batch].copy()

    model = scDMLModel()
    adata = model.preprocess(adata, batch_key = batch)
    model.integrate(adata, 
                    batch_key = batch, 
                    ncluster_list = [15], 
                    merge_rule="rule2", 
                    expect_num_cluster = 15, 
                    mode = "unsupervised")

    plot(adata, "X_emb", 'batch_orig' , celltype, out_path)
