from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a Spark session
spark = SparkSession.builder.appName("ClusteringExample").getOrCreate()

# Define the file path for the dataset
url = "adult.data"

# Define the schema for the dataset
schema = StructType([
    StructField("age", IntegerType()),
    StructField("workclass", StringType()),
    StructField("fnlwgt", IntegerType()),
    StructField("education", StringType()),
    StructField("education-num", IntegerType()),
    StructField("marital-status", StringType()),
    StructField("occupation", StringType()),
    StructField("relationship", StringType()),
    StructField("race", StringType()),
    StructField("sex", StringType()),
    StructField("capital-gain", IntegerType()),
    StructField("capital-loss", IntegerType()),
    StructField("hours-per-week", IntegerType()),
    StructField("native-country", StringType()),
    StructField("income", StringType())
])

# Load the dataset with the specified schema
data = spark.read.csv(url, header=False, schema=schema, sep=',', ignoreLeadingWhiteSpace=True, ignoreTrailingWhiteSpace=True, encoding="utf-8")

# Select attributes for clustering (e.g., age, education-num, and hours-per-week)
selected_attributes = ["age", "education-num", "hours-per-week"]

# Assemble the features into a single vector
assembler = VectorAssembler(inputCols=selected_attributes, outputCol="features")
data = assembler.transform(data)

# Scale the features
scaler = StandardScaler(inputCol="features", outputCol="scaled_features")
scaler_model = scaler.fit(data)
data = scaler_model.transform(data)

# Perform K-Means clustering with K clusters
k = 3  # You can choose the number of clusters based on your requirements
kmeans = KMeans(featuresCol="scaled_features", predictionCol="cluster", k=k)
model = kmeans.fit(data)

# Add cluster labels to the dataset
data = model.transform(data)

# Show the resulting clusters
data.select("age", "education-num", "hours-per-week", "cluster").show()
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a Spark session
spark = SparkSession.builder.appName("ClusteringExample").getOrCreate()

# Define the file path for the dataset
url = "adult.data"

# Define the schema for the dataset
schema = StructType([
    StructField("age", IntegerType()),
    StructField("workclass", StringType()),
    StructField("fnlwgt", IntegerType()),
    StructField("education", StringType()),
    StructField("education-num", IntegerType()),
    StructField("marital-status", StringType()),
    StructField("occupation", StringType()),
    StructField("relationship", StringType()),
    StructField("race", StringType()),
    StructField("sex", StringType()),
    StructField("capital-gain", IntegerType()),
    StructField("capital-loss", IntegerType()),
    StructField("hours-per-week", IntegerType()),
    StructField("native-country", StringType()),
    StructField("income", StringType())
])

# Load the dataset with the specified schema
data = spark.read.csv(url, header=False, schema=schema, sep=',', ignoreLeadingWhiteSpace=True, ignoreTrailingWhiteSpace=True, encoding="utf-8")

# Select attributes for clustering (e.g., age, education-num, and hours-per-week)
selected_attributes = ["age", "education-num", "hours-per-week"]

# Assemble the features into a single vector
assembler = VectorAssembler(inputCols=selected_attributes, outputCol="features")
data = assembler.transform(data)

# Scale the features
scaler = StandardScaler(inputCol="features", outputCol="scaled_features")
scaler_model = scaler.fit(data)
data = scaler_model.transform(data)

# Perform K-Means clustering with K clusters
k = 3  # You can choose the number of clusters based on your requirements
kmeans = KMeans(featuresCol="scaled_features", predictionCol="cluster", k=k)
model = kmeans.fit(data)

# Add cluster labels to the dataset
data = model.transform(data)

# Show the resulting clusters
data.select("age", "education-num", "hours-per-week", "cluster").show()

# Task i: The country from which the highest number of adults are there except USA
highest_country = data.filter(data["native-country"] != "USA")\
    .groupBy("native-country")\
    .count()\
    .orderBy("count", ascending=False)\
    .first()
#print("i) The country with the highest number of adults (except USA) is:", highest_country["native-country"])

# Task ii: No of people who are at least Masters and work in “Tech-support”
masters_in_tech_support = data.filter((data["education"] == "Masters") & (data["occupation"] == "Tech-support")).count()
#print("ii) Number of people with at least Masters working in Tech-support:", masters_in_tech_support)

# Task iii: No of unmarried males who work in “Local_govt”
#unmarried_males_in_local_govt = data.filter((data["marital-status"] != "Married-civ-spouse") & (data["sex"] == "Male") & (data["workclass"] == "Local-gov")).count()
#print("iii) Number of unmarried males working in Local_govt:", unmarried_males_in_local_govt)

# Stop the Spark session
spark.stop()

