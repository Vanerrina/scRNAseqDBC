# Tree-based models on single-cell RNA sequencing data to identify breast cancer gene drivers
This repository contains Python scripts and data used for applying tree-based models to single-cell RNA sequencing (scRNA-seq) data to identify breast cancer gene drivers. The goal is to leverage machine learning techniques to uncover important genetic markers associated with breast cancer progression.
The implementation was developed and tested using [Python](https://www.python.org/) version 3.11.2.

## Table of Contents
- [Overview](#overview)
- [Usage Notes](#usage)
- [Dataset](#dataset)
- [Citation](#citation)
- [Contact](#contact)

## Overview
Breast cancer (BC) relies on an intricate environment comprising diverse cancer cell clones that shape the disease evolution. Single-cell RNA sequencing (scRNA-seq) is a valuable resource for the characterization of BC tumor biology, the assessment of its heterogeneity along with multifaceted networks existing between the malignant cells and other components of the tumor microenvironment (TME). Furthermore, scRNA-seq provides the opportunity to identify novel BC druggable targets, thus allowing the advancement of precision therapeutic approaches. The employment of machine learning techniques in cancer research can efficiently analyze large-scale omics data, making them well-suited for scRNA-seq applications. Here, we provide a novel scRNA-seq BC dataset, which uncovers 6 distinct cell clusters encompassing cancer cells and TME cell populations. By leveraging the transparency and interpretability of tree-based machine learning models, we identify gene expression changes that drive the dynamic evolutionary trajectories of the cell populations. Our dataset provides a novel transcriptomic resource that can further enhance the understanding of the complex BC ecosystem.

<!-- ![Figure 1](https://github.com/user-attachments/assets/0b10c17f-f918-462b-9e33-8efeefad8271) -->

An overview of the scRNA-seq analysis of BC tissue is provided in Figure 1. Briefly, the overall process includes the following steps: acquiring tissue sample from a BC patient, 10X Genomics scRNA-seq library construction and sequencing, scRNA-seq data processing (including cell annotation and trajectory inference), machine leaning classification tasks and model evaluation and explainability.

## Dataset
The sequencing data generated in this study have been deposited in the GEO repository with accession number GSE288223.

Raw counts and processed scRNA-seq data (including filtering, normalization, PCA, clustering labels, cell annotations, UMAP coordinates, and pseudotime calculation) are available as h5ad files. Both datasets are stored [here](https://drive.google.com/file/d/1JGtv232LbYCtL7wDkQYgUUPMus9MOueS/view?usp=sharing) as AnnData objects.

## Usage Notes
This repository contains several Python scripts and Jupyter notebooks for processing and analyzing single-cell RNA sequencing (scRNA-seq). Below is a brief description of each file:

- **data_preprocessing_scRNAseqDBC.ipynb** – Prepares and cleans scRNA-seq data for further analysis (including filtering, normalization, PCA, clustering). *(Uses: `scanpy`)*  
- **cell_annotation_scRNAseqDBC.ipynb** – Assigns cell-type annotations based on gene expression profiles using [SCSA](https://github.com/bioinfo-ibms-pumc/SCSA). *(Uses: `SCSA`)*  
- **Trajectory_inference_scRNAseqDBC.ipynb** – Performs trajectory inference on single-cell RNA sequencing data. *(Uses: `scanpy`)*  
- **DecisionTree.py** – Contains decision tree algorithms for identifying gene drivers in scRNA-seq data. *(Uses: `scikit-learn`)*  
- **Cell_Label_Couple_single_tree.py** – Implements tree-based models to analyze cell-label relationships. *(Uses: `scikit-learn`)*

The Python dependencies are specified in the requirements.txt file and can be installed (preferrably in a virtual environment) using the command `pip install -r requirements.txt`.
## Citation

If you use any material from this repository, please cite the following work:

*Applying tree-based models to single-cell RNA sequencing data for identifying breast cancer gene drivers*  

Authors: Vanessa Verrina et al.

<!-- DOI/Link: [Your DOI or URL]  -->

BibTeX format:
```bibtex
@article{Verrina2025,
  author    = {Vanessa Verrina and Marianna Talia and Eugenio Cesario and Santina Capalbo and Domenica Scordamaglia and Rosamaria Lappano and Anna Maria Miglietta and Marcello Maggiolini and Sabrina Giordano},
  title     = {Applying tree-based models to single-cell RNA sequencing data for identifying breast cancer gene drivers},
  journal   = {xxx},
  year      = {2025},
  note      = {Submitted}
}
```
## Contact
For questions or collaboration, contact Vanessa Verrina at vanessa.verrina@unical.it.
