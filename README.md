# Unsupervised Crop Data Analysis Project

## 📖 Overview

This project leverages **Unsupervised Machine Learning** techniques to analyze agricultural data. By applying Clustering (K-Means) and Anomaly Detection (Isolation Forest), the system identifies distinct farming patterns and flags potential irregularities (such as crop stress or data errors). The high-dimensional data is visualized using Principal Component Analysis (PCA).

This tool is designed for agronomists, data scientists, and researchers to gain insights into crop yield factors and soil health.

---

## 📊 Dataset Description

The analysis is based on the `unsupervised_crop_dataset_5000.csv` file, which contains **5000+ records**. Each row represents a specific farmed area with the following features:

| Feature              | Description                                                                          |
| :------------------- | :----------------------------------------------------------------------------------- |
| **soil_moisture**    | Moisture content percentage in the soil.                                             |
| **soil_ph**          | Acidity or alkalinity level of the soil (pH scale).                                  |
| **soil_nitrogen**    | Nitrogen content in the soil (essential nutrient).                                   |
| **avg_temperature**  | Average ambient temperature (°C).                                                    |
| **rainfall_mm**      | Total rainfall received in millimeters.                                              |
| **humidity**         | Relative humidity percentage.                                                        |
| **ndvi**             | _Normalized Difference Vegetation Index_ – a measure of plant health/greenness.      |
| **evi**              | _Enhanced Vegetation Index_ – similar to NDVI but corrected for atmospheric signals. |
| **irrigation_level** | Categorical level of irrigation applied (e.g., 1-4).                                 |
| **fertilizer_kg**    | Amount of fertilizer applied in kilograms.                                           |
| **crop_yield_tph**   | **Target Variable**: Crop yield in Tons Per Hectare.                                 |

---

## 🧠 Methodology

### 1. Data Preprocessing

- **Standard Scaling**: All features are scaled using `StandardScaler` to have a mean of 0 and variance of 1. This ensures that features with larger ranges (like Rainfall ~800mm) don't dominate features with smaller ranges (like NDVI ~0.5) during clustering.

### 2. Clustering (K-Means)

- **Algorithm**: K-Means Clustering.
- **Configuration**: `n_clusters=4`.
- **Goal**: To segment the farming data into 4 distinct groups (clusters) based on similarities in soil, weather, and yield conditions.
- **Metric**: The script calculates the **Silhouette Score** to evaluate how well-separated the clusters are.

### 3. Anomaly Detection (Isolation Forest)

- **Algorithm**: Isolation Forest.
- **Configuration**: `contamination=0.08` (assumes ~8% of the data is anomalous).
- **Goal**: To identify outliers. In an agricultural context, these could represent:
  - **Stress Zones**: Areas with unusually low yield despite standard inputs.
  - **Data Errors**: Sensor malfunctions or recording errors.
  - **High Yield Zones**: Exceptionally productive areas worth investigating.

### 4. Visualization (PCA)

- **Algorithm**: Principal Component Analysis (PCA).
- **Goal**: Reduces the 10+ feature dimensions down to 2 principal components (`PC1` and `PC2`) so the data can be plotted on a 2D scatter graph.

---

## 🛠️ Usage

### Prerequisites

Ensure you have Python installed. Install the required dependencies:

```bash
pip install pandas numpy matplotlib scikit-learn
```

### Running the Analysis

Execute the main script:

```bash
python project.py
```

---

## 📂 Outputs & Interpretation

### 1. CSV Report (`final_unsupervised_results.csv`)

The script generates a new CSV file containing the original data plus two new analytical columns:

- `kmeans_cluster`: The cluster ID (0, 1, 2, or 3) assigned to the row.
- `anomaly`: The anomaly status.
  - `1`: **Normal** data point.
  - `-1`: **Anomaly** (Outlier/Stress Zone).

### 2. Cluster Visualization (`kmeans_pca.png`)

- A scatter plot showing the 4 distinct clusters in different colors.
- **Interpretation**: Points grouped together share similar agricultural characteristics. You can analyze the `kmeans_cluster` column in the CSV to find the average yield of each group.

### 3. Anomaly Visualization (`isolation_forest_pca.png`)

- A scatter plot highlighting normal points vs. anomalies.
- **Interpretation**: The distinct colored points (usually few in number) are the anomalies. These specific rows should be manually inspected to understand why they deviate from the norm.

---

## 📉 Console Metrics

When you run the script, it will print:

1.  **Silhouette Score**: A score closer to 1.0 indicates excellent clustering.
2.  **Cluster Means**: The average yield and soil properties for each cluster, helping you label them (e.g., "High Yield / High Nitrogen Cluster" vs "Low Yield / Dry Cluster").
3.  **Anomaly Means**: A comparison of average values between Normal (`1`) and Anomalous (`-1`) data.
