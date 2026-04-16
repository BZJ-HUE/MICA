# A Cross-Modal Multi-View Contrastive Learning Framework for Spatial Multi-Omics Integration

![Framework](./Workflow.png)

# Installation & Dependencies
You'll need to install the following packages in order to run the codes.

* python==3.8
* torch>=1.8.0
* cudnn>=10.2
* numpy==1.22.3
* scanpy==1.9.1
* anndata==0.8.0
* rpy2==3.4.1
* pandas==1.4.2
* scipy==1.8.1
* scikit-learn==1.1.1
* scikit-misc==0.2.0
* tqdm==4.64.0
* matplotlib==3.4.2
* R==4.0.3

# Tutorial
For the step-by-step tutorial, please refer to:(https://github.com/BZJ-HUE/MICA/tree/main/Tutorial)

In addition, the data set used in the distribution tutorial about Mouse Embryo MICA Tutorial has been uploaded to the datd file and can be downloaded directly.

## Data

The datasets used in this study are all publicly available from previously published resources.

- **Human lymph node (HLN) spatial RNA--protein dataset**  
  The HLN dataset used in this work was derived from the dataset reported in SpatialGlue and is available via [Zenodo](https://zenodo.org/records/10362607).  
  The original 10x Visium human lymph node data are also available from GEO under accession number [GSE263617](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE263617).

- **SPOTS mouse spleen spatial transcriptome--proteome dataset**  
  This dataset is available from GEO under accession number [GSE198353](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198353).

- **MISAR-seq E18.5 mouse brain spatial epigenome--transcriptome dataset**  
  This dataset is available from the National Genomics Data Center (NGDC) under accession number [OEP003285](https://www.biosino.org/node/project/detail/OEP003285).

- **Spatial ATAC--RNA-seq mouse embryo dataset**  
  This dataset is publicly available from GEO under accession number [GSE214991](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE214991).
