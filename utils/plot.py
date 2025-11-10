import matplotlib.pyplot as plt
import scanpy as sc

def plot(adata, rep, batch, cell_type, save_dir):
    sc.pp.neighbors(adata, use_rep = rep)
    sc.tl.umap(adata)

    sc.pl.umap(adata, color = [batch], show=False, save=None)
    plt.savefig(f"{save_dir}_batch.png", dpi=1000, bbox_inches="tight")
    plt.close()

    sc.pl.umap(adata, color = [cell_type], show=False, save=None)
    plt.savefig(f"{save_dir}_cell.png", dpi=1000, bbox_inches="tight")
    plt.close()