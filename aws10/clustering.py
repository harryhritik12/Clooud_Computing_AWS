import pandas as pd
import warnings
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the adult dataset
warnings.filterwarnings('ignore')

url = "adult.data"
column_names = [
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex",
    "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"
]
data = pd.read_csv(url, names=column_names, sep=',\s*', engine='python')

# Select three attributes for clustering (e.g., age, education-num, and hours-per-week)
selected_attributes = data[["age", "education-num", "hours-per-week"]]

# Encode categorical variables (workclass, education)
label_encoder = LabelEncoder()
selected_attributes["education"] = label_encoder.fit_transform(data["education"])
selected_attributes["workclass"] = label_encoder.fit_transform(data["workclass"])

# Standardize the data
scaler = StandardScaler()
selected_attributes = scaler.fit_transform(selected_attributes)

# Perform K-Means clustering with K clusters
k = 3  # You can choose the number of clusters based on your requirements
kmeans = KMeans(n_clusters=k)
clusters = kmeans.fit_predict(selected_attributes)

# Add cluster labels to the dataset
data['cluster'] = clusters

# Plot the clusters (you may need to install matplotlib)
plt.scatter(selected_attributes[:, 0], selected_attributes[:, 1], c=clusters, cmap='rainbow')
plt.xlabel('Age')
plt.ylabel('Education Number')
plt.title('K-Means Clustering')
plt.show()

# Print cluster information
for i in range(k):
    cluster_data = data[data['cluster'] == i]
    print(f"Cluster {i}:\n{cluster_data.describe()}\n")

# You can analyze and interpret the clusters as needed
