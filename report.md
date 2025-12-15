# Crop Data Analysis: Full Scale Report

## 1. Executive Summary

This report details the findings from an unsupervised machine learning analysis of 5,000+ agricultural records. The objective was to identify distinct farming patterns (Clustering) and detect irregularities (Anomaly Detection).

**Key Findings:**

- **Four Distinct Agronomic Profiles Identified**: The analysis segmented the farms into four clusters. While yields are relatively consistent across clusters (~4.3 - 4.6 TPH), they differ significantly in input factors like rainfall and soil pH.
- **Low Cluster Separation**: A Silhouette Score of **0.067** indicates that the agricultural profiles are not highly distinct; the data points overlap significantly, suggesting that most farms operate under a continuous spectrum of conditions rather than in rigid categories.
- **Anomalies Detected**: Approximately **8%** of the data points were flagged as anomalies. Interestingly, the anomalous group has a slightly _lower_ average yield (4.33 TPH) compared to the normal group (4.47 TPH), indicating that "abnormal" conditions in this dataset generally correlate with stress or suboptimal performance.

---

## 2. Methodology

### 2.1 Data Preprocessing

The dataset `unsupervised_crop_dataset_5000.csv` was processed to ensure fair comparison between diverse features:

- **Features Used**: Soil Moisture, pH, Nitrogen, Temperature, Rainfall, Humidity, NDVI, EVI, Irrigation Level, and Fertilizer usage.
- **Scaling**: All features were normalized using Standard Scaling (mean=0, variance=1) to prevent high-magnitude variables (like Rainfall) from dominating the distance calculations.

### 2.2 Algorithms Employed

1.  **K-Means Clustering**: Used to group similar farms. `k=4` was selected as the optimal number of clusters.
2.  **Isolation Forest**: Used for anomaly detection with a contamination rate of 8%.
3.  **PCA (Principal Component Analysis)**: Used for dimensionality reduction to visualize the 10-dimensional data on a 2D plane.

---

## 3. Results & Analysis

### 3.1 Clustering Analysis (K-Means)

The K-Means algorithm identified 4 clusters. Below is the average crop yield for each:

| Cluster ID | Average Yield (TPH) | Key Characteristics (Inferred)                                |
| :--------- | :------------------ | :------------------------------------------------------------ |
| **0**      | **4.61** (Highest)  | Likely optimal balance of inputs; highest productivity group. |
| **1**      | 4.54                | High performing, potentially favorable soil conditions.       |
| **2**      | 4.33                | Moderate yield performance.                                   |
| **3**      | 4.35                | Moderate yield performance.                                   |

**Observation**: The yield difference between the best (Cluster 0) and worst (Cluster 2) performing groups is approximately **6.5%**. This suggests that while clusters exist, the overall variability in yield is essentially low.

### 3.2 Anomaly Detection (Isolation Forest)

The model flagged outliers based on their statistical deviation from the norm.

| Group            | Count | Avg Yield (TPH) | Interpretation                                                                                    |
| :--------------- | :---- | :-------------- | :------------------------------------------------------------------------------------------------ |
| **Normal (1)**   | ~4600 | **4.47**        | The majority of farms operating under standard conditions.                                        |
| **Anomaly (-1)** | ~400  | 4.33            | Outliers representing unusual conditions (e.g., extreme rainfall, sensor errors, or soil stress). |

**Insight**: The anomalies are underperforming on average. This validates the model's ability to detect "stress zones" or suboptimal farming practices effectively.

### 3.3 Model Performance Metrics

- **Silhouette Score**: `0.067`
  - _Interpretation_: This is a low score (range is -1 to 1). It indicates that the clusters are not dense or well-separated. In agricultural datasets, this is common as soil and weather data tends to vary continuously rather than changing abruptly.

---

## 4. Visualizations

Two key visualizations were generated (see files in directory):

1.  **`kmeans_pca.png`**: Visualizes the 4 clusters. The overlap visible in this plot confirms the low Silhouette Score.
2.  **`isolation_forest_pca.png`**: Highlights the anomalies (outliers) in a distinct color, showing they are essentially scattered around the fringes of the main data distribution.

---

## 5. Recommendations

1.  **Investigate Cluster 0**: Identify the specific practices (fertilizer rates, irrigation schedules) of Cluster 0, as they achieve the highest yields. Replicating these conditions could boost overall production.
2.  **Analyze Anomalies**: Manually inspect the top 10 anomalous records with the lowest yields. Determine if these are due to data quality issues (sensor malfunction) or genuine agronomic problems (pest infestation, drought).
3.  **Refine Clustering**: Given the low Silhouette Score, consider experimenting with:
    - Different clustering algorithms (e.g., DBSCAN) that handle continuous density better.
    - Feature engineering: creating new variables like "Nitrogen per unit Rainfall" to highlight efficiency.
4.  **Targeted Interventions**: Since anomalies correlate with lower yields, an automated alert system could be built to flag these conditions in real-time for proactive management.
