# PDF Classification using LLMs, Embedding Models, XGBoost and Linear Regressors

## Overview

This project focuses on classifying a massive dataset of PDFs from the **SafeDocs corpus** using a combination of **Large Language Models (LLMs)**, **XGBoost**, and other machine learning techniques. The dataset includes over **8.4 million PDFs**, making this a large-scale exploration of both deep learning and traditional machine learning methods.

---

## Features

- **Few-Shot Prompting**: Leveraged LLMs (Llama-3-70B) for initial label generation from PDF metadata.
- **Embeddings-Based Classification**: Used pretrained embeddings models (e.g., `gte-large`) fine-tuned for specific labels.
- **Tabular Data Techniques**: Applied XGBoost and TF-IDF for lightweight and efficient classification.
- **Dimensionality Reduction**: Visualized embeddings and classifications with PCA and UMAP.

---

## Dataset

1. **SafeDocs PDF Dataset**  
   - 📥 [Download from Digital Corpora](https://corp.digitalcorpora.org/corpora/files/CC-MAIN-2021-31-PDF-UNTRUNCATED/)  
   - Total size: 8TB (uncompressed)  
   - Includes metadata for all PDFs.

2. **Generated Labels and Embeddings**  
   - 📥 [Labels on Hugging Face](https://huggingface.co/datasets/snats/url-classifications)  
   - 📥 [Embeddings on Kaggle](https://www.kaggle.com/datasets/santiagopedroza/url-embeddings-cc-provenance)  

---

## Results

| **Model**                      | **Accuracy** |  
|--------------------------------|--------------|  
| gte-large (59k labels)         | 59.14%       |  
| **XGBoost (Embeddings)**       | **85.26%**   |  
| XGBoost (TF-IDF)               | 67.52%       |  
| Linear Regressor (TF-IDF)      | 70.68%       |  
| gte-large (400k labels)        | 69.22%       |  

---

## Visualizations

### PCA
- A 2D projection of 8.4M PDFs based on their embeddings.

![PCA Visualization](./assets/pca_visualization_8448751_samples.png)

### UMAP
- A high-dimensional visualization of 6.5M classified PDFs.

![UMAP Visualization](./assets/umap_visualization_6500000_samples.png)

