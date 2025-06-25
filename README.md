# Tree-based models on single-cell RNA sequencing data to identify breast cancer gene drivers

This repository contains Python scripts and data used for applying trajectory inference and tree-based models to single-cell RNA sequencing (scRNA-seq) data to identify breast cancer gene drivers. The goal is to leverage machine learning techniques to uncover important genetic markers associated with breast cancer progression.
The implementation was developed and tested using [Python](https://www.python.org/) version 3.11.2.

## Table of Contents
- [Overview](#overview)
- [Usage Notes](#usage)
- [Dataset](#dataset)
- [Citation](#citation)
- [Contact](#contact)

## Overview
Breast cancer (BC) is characterized by a highly heterogeneous cellular enviroment composed of diverse malignant clones and components of the tumor microenvironment (TME) that collectively influence the progression of the disease. Single-cell RNA sequencing (scRNA-seq) offers a powerful tool to dissect this complexity, enabling high
resolution characterization of tumor heterogeneity and the functional interactions within the TME. Moreover, it also supports the discovery of clinically relevant subpopulations and potential therapeutic targets. In this study, we present a novel scRNA-seq dataset from an infiltrating ductal BC, profiling over 5,000 cells and identifying six distinct clusters spanning cancer and TME populations. To explore the molecular drivers of cell state transitions, we integrate pseudotime trajectory inference with interpretable, tree-based machine learning. This approach enables the identification of key genes and expression thresholds associated with dynamic phenotypic shifts. Unlike black-box models, our framework yields transparent, rule-based insights into transcriptional reprogramming during tumour evolution. 
The resulting dataset and accessible and transparent analytical pipeline offer a valuable resource for the breast cancer research community and lay the groundwork for future studies aimed at refining molecular classification and precision therapy development. 

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
- **Couple_single_tree.py** – Implements tree-based models to analyze cell-label relationships. *(Uses: `scikit-learn`)*

The Python dependencies are specified in the requirements.txt file and can be installed (preferrably in a virtual environment) using the command `pip install -r requirements.txt`.
## Citation

If you use any material from this repository, please cite the following work:

*Applying tree-based models to single-cell RNA sequencing data for identifying breast cancer gene drivers*  

Authors: Vanessa Verrina et al.

<!-- DOI/Link: [Your DOI or URL]  -->

BibTeX format (to be updated):
```bibtex
@article{Verrina2025,
  author    = {Vanessa Verrina and Marianna Talia and Eugenio Cesario and Santina Capalbo and Domenica Scordamaglia and Rosamaria Lappano and Anna Maria Miglietta and Marcello Maggiolini and Sabrina Giordano},
  title     = {Integrating Trajectory Inference and Self-Explainable Predictive Models to Explore Cell State Transitions in Breast Cancer at Single-Cell Resolution},
  journal   = {xxx},
  year      = {2025},
  note      = {Submitted}
}
```
## Contact
For questions or collaboration, contact Vanessa Verrina at vanessa.verrina@unical.it.
