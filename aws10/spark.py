import pandas as pd
from sklearn.cluster import KMeans
from ucimlrepo import fetch_ucirepo

# Fetch the datasetpi
adult = fetch_ucirepo(id=2)

# Data (as pandas DataFrame)
X = adult.data.features

# Define the columns you want to use for clustering (e.g., age, workclass, education)
selected_columns = ['age', 'workclass', 'education']

# Select the relevant columns
X_cluster = X[selected_columns]

# Perform one-hot encoding for categorical columns
categorical_columns = ['workclass', 'education']
X_cluster_encoded = pd.get_dummies(X_cluster, columns=categorical_columns)

# Perform clustering using K-Means
num_clusters = 3  # You can change this as needed
kmeans = KMeans(n_clusters=num_clusters, n_init = 'auto')
X['cluster'] = kmeans.fit_predict(X_cluster_encoded)

# Save the clustering results to a CSV file
X.to_csv("clustered_adult_data.csv", index=False)

# Now, you can print the first few rows of the clustered dataset if desired
print(X.head())

# i) The country from which the highest number of adults are there except USA.
filtered_data = X[X['native-country'] != 'United-States']
country_counts = filtered_data['native-country'].value_counts().reset_index()
country_counts.columns = ['native-country', 'count']
highest_count_country = country_counts.sort_values(by='count', ascending=False).iloc[0]
print(f"The country with the highest number of adults (excluding USA) is {highest_count_country['native-country']} with {highest_count_country['count']} adults.")

# ii) No of people who are at least Masters and work in "Tech-support."
masters_in_tech_support = X[(X['education'] == 'Masters') & (X['occupation'] == 'Tech-support')]
count_masters_in_tech_support = masters_in_tech_support.shape[0]
print(f"The number of adults with at least a Masters degree working in 'Tech-support' is {count_masters_in_tech_support}.")

# iii) No of unmarried males who work in "Local-govt."
unmarried_local_govt_males = X[(X['marital-status'] != 'Married') & (X['sex'] == 'Male') & (X['workclass'] == 'Local-govt')]
count_unmarried_local_govt_males = unmarried_local_govt_males.shape[0]
print(f"The number of unmarried males working in 'Local-govt' is {count_unmarried_local_govt_males}.")
