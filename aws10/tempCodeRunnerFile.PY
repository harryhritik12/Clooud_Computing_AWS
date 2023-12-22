from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("ClusteringExample").getOrCreate()

# Define the file path for the dataset
url = "adult.data"

# Load the dataset
data = spark.read.option("header", False).option("delimiter", ", ").csv(url)

# Define the schema for the dataset
data = data.withColumnRenamed("_c0", "age") \
           .withColumnRenamed("_c1", "workclass") \
           .withColumnRenamed("_c2", "fnlwgt") \
           .withColumnRenamed("_c3", "education") \
           .withColumnRenamed("_c4", "education-num") \
           .withColumnRenamed("_c5", "marital-status") \
           .withColumnRenamed("_c6", "occupation") \
           .withColumnRenamed("_c7", "relationship") \
           .withColumnRenamed("_c8", "race") \
           .withColumnRenamed("_c9", "sex") \
           .withColumnRenamed("_c10", "capital-gain") \
           .withColumnRenamed("_c11", "capital-loss") \
           .withColumnRenamed("_c12", "hours-per-week") \
           .withColumnRenamed("_c13", "native-country") \
           .withColumnRenamed("_c14", "income")

# Task i: The country from which the highest number of adults are there except USA
country_counts = data.filter(data["native-country"] != "United-States") \
                    .groupBy("native-country") \
                    .count() \
                    .orderBy(col("count").desc()) \
                    .limit(1)

highest_country = country_counts.first()["native-country"]
print("i) The country with the highest number of adults (except USA) is:", highest_country)

# Task ii: No of people who are at least Masters and work in "Tech-support"
masters_in_tech_support = data.filter((data["education"] == "Masters") & (data["occupation"] == "Tech-support")).count()
print("ii) Number of people with at least Masters working in Tech-support:", masters_in_tech_support)

# Task iii: No of unmarried males who work in "Local_govt"
unmarried_males_in_local_govt = data.filter((data["marital-status"] != "Married-civ-spouse") & (data["sex"] == "Male") & (data["workclass"] == "Local-gov")).count()
print("iii) Number of unmarried males working in Local-govt:", unmarried_males_in_local_govt)

# Stop the Spark session
spark.stop()
