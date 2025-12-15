import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.ensemble import IsolationForest

df = pd.read_csv("unsupervised_crop_dataset_5000.csv")

X = df.drop(columns=["crop_yield_tph"], errors="ignore")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df["kmeans_cluster"] = kmeans.fit_predict(X_scaled)

print(silhouette_score(X_scaled, df["kmeans_cluster"]))
print(df.groupby("kmeans_cluster")["crop_yield_tph"].mean())

iso = IsolationForest(
    n_estimators=200,
    contamination=0.08,
    random_state=42
)

df["anomaly"] = iso.fit_predict(X_scaled)

print(df.groupby("anomaly")["crop_yield_tph"].mean())
print(df.groupby("anomaly").mean())

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=df["kmeans_cluster"],
    s=10
)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("K-Means Clustering (PCA Projection)")
plt.tight_layout()
plt.savefig("kmeans_pca.png", dpi=300)
plt.close()

plt.figure(figsize=(8, 6))
plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=df["anomaly"],
    s=10
)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Isolation Forest – Stress Zone Detection (PCA View)")
plt.tight_layout()
plt.savefig("isolation_forest_pca.png", dpi=300)
plt.close()

df.to_csv("final_unsupervised_results.csv", index=False)

print("Saved: kmeans_pca.png, isolation_forest_pca.png, final_unsupervised_results.csv")
