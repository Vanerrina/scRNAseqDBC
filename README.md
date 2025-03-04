# Applying tree-based models to single-cell RNA sequencing data for identifying breast cancer gene drivers
This repository contains code and data used for applying tree-based models to single-cell RNA sequencing (scRNA-seq) data to identify breast cancer gene drivers. The goal is to leverage machine learning techniques to uncover important genetic markers associated with breast cancer progression.

## Table of Contents
- [Overview](#overview)
- [Usage Notes](#usage)
- [Dataset](#dataset)
- [Citation](#citation)
- [Contact](#contact)

## Overview
Breast cancer (BC) relies on an intricate environment comprising diverse cancer cell clones that shape the disease evolution. Single-cell RNA sequencing (scRNA-seq) is a valuable resource for the characterization of BC tumor biology, the assessment of its heterogeneity along with multifaceted networks existing between the malignant cells and other components of the tumor microenvironment (TME). Furthermore, scRNA-seq provides the opportunity to identify novel BC druggable targets, thus allowing the advancement of precision therapeutic approaches. The employment of machine learning techniques in cancer research can efficiently analyze large-scale omics data, making them well-suited for scRNA-seq applications. Here, we provide a novel scRNA-seq BC dataset, which uncovers 6 distinct cell clusters encompassing cancer cells and TME cell populations. By leveraging the transparency and interpretability of tree-based machine learning models, we identify gene expression changes that drive the dynamic evolutionary trajectories of the cell populations. Our dataset provides a novel transcriptomic resource that can further enhance the understanding of the complex BC ecosystem.

![Figure 1](https://github.com/user-attachments/assets/0b10c17f-f918-462b-9e33-8efeefad8271)

## Dataset
The sequencing data generated in this study have been deposited in the GEO repository with accession number GSE288223.

Raw counts and processed scRNA-seq data (including filtering, normalization, PCA, clustering labels, cell annotations, and UMAP coordinates) are available as h5ad files. Both datasets are stored [here](https://drive.google.com/file/d/1JGtv232LbYCtL7wDkQYgUUPMus9MOueS/view?usp=sharing) as AnnData objects.

## Usage Notes
This repository contains several Python scripts and Jupyter notebooks for processing and analyzing single-cell RNA sequencing (scRNA-seq). Below is a brief description of each file:

- **data_preprocessing_scRNAseqDBC.ipynb** – Prepares and cleans scRNA-seq data for further analysis (it includes (including filtering, normalization, PCA, clustering).
- **cell_annotation_scRNAseqDBC.ipynb** – Assigns cell-type annotations based on gene expression profiles.
- **Trajectory_inference_scRNAseqDBC.ipynb** – Performs trajectory inference on single-cell RNA sequencing data.
- **DecisionTree.py** – Contains decision tree algorithms for identifying gene drivers in scRNA-seq data.
- **Cell_Label_Couple_single_tree.py** – Implements tree-based models to analyze cell-label relationships.  

## Citation

If you use any material from this repository, please cite the following work:

Applying tree-based models to single-cell RNA sequencing data for identifying breast cancer gene drivers  

Authors: Vanessa Verrina et al.

DOI/Link: [Your DOI or URL]  

BibTeX format:
```bibtex
@article{YourCitationKey,
  author = {Your Name},
  title = {Your Paper Title},
  journal = {Journal Name},
  year = {Year},
  volume = {X},
  number = {X},
  pages = {XX--XX},
  doi = {Your DOI}
}
```
## Contact
For questions or collaboration, contact Vanessa Verrina at vanessa.verrina@unical.it.
