from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer, OneHotEncoder
from pyspark.ml.clustering import KMeans
from pyspark.sql.functions import col
from pyspark.sql.types import DoubleType

# Initialize a Spark session
spark = SparkSession.builder.appName("AdultDataClustering").getOrCreate()

# Load the Adult dataset
data = spark.read.csv('clustered_adult_data.csv', header=True)  # Replace 'clustered_adult_data.csv' with the actual file path

# Convert "age" column to a numerical data type (e.g., Double)
data = data.withColumn("age", col("age").cast(DoubleType()))

# Define the columns you want to use for clustering
categorical_columns = ['workclass', 'education', 'marital-status', 'sex', 'native-country']
numerical_column = 'age'

# Apply StringIndexer to convert categorical columns into numerical indices
indexers = [StringIndexer(inputCol=col, outputCol=col + "_index") for col in categorical_columns]

indexed_data = data
for indexer in indexers:
    indexed_data = indexer.fit(indexed_data).transform(indexed_data)

# Assemble the features including one-hot encoded columns
assembler = VectorAssembler(inputCols=[numerical_column] + [col + "_index" for col in categorical_columns], outputCol="features")
final_data = assembler.transform(indexed_data)

# Remove the existing "cluster" column if it exists
if "cluster" in final_data.columns:
    final_data = final_data.drop("cluster")

# Perform K-Means clustering (specify the number of clusters)
num_clusters = 3
kmeans = KMeans(featuresCol="features", predictionCol="cluster", k=num_clusters, seed=1)
model = kmeans.fit(final_data)
clustered_data = model.transform(final_data)

# Task i) The country from which the highest number of adults are there except USA.
filtered_data = clustered_data.filter(col('native-country_index') != 0)  # Assuming USA has an index of 0
country_counts = filtered_data.groupBy('native-country_index').count()
highest_count_country_index = country_counts.orderBy(col('count').desc()).first()['native-country_index']
highest_count_country = indexed_data.filter(col('native-country_index') == highest_count_country_index).first()['native-country']
print(f"The country with the highest number of adults (excluding USA) is {highest_count_country}.")

# Task ii) No of people who are at least Masters and work in "Tech-support".
masters_in_tech_support = clustered_data.filter((col('education_index') >= 5) & (col('workclass_index') == 8))  # Adjust index values based on your data
count_masters_in_tech_support = masters_in_tech_support.count()
print(f"The number of adults with at least a Masters degree working in 'Tech-support' is {count_masters_in_tech_support}.")

# Task iii) No of unmarried males who work in "Local-govt".
unmarried_local_govt_males = clustered_data.filter((col('marital-status_index') != 1) & (col('sex_index') == 0) & (col('workclass_index') == 4))  # Adjust index values based on your data
count_unmarried_local_govt_males = unmarried_local_govt_males.count()
print(f"The number of unmarried males working in 'Local-govt' is {count_unmarried_local_govt_males}.")

# Stop the Spark session
spark.stop()
