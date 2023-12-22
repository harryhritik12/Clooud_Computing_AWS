# Use a base image with Ubuntu
FROM ubuntu:latest

# Update the package repository and install dependencies
RUN apt-get update && apt-get install -y default-jdk wget python3

# Download and extract Hadoop
RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
RUN tar -xzvf hadoop-3.3.6.tar.gz

# Set environment variables
ENV JAVA_HOME $(readlink -f /usr/bin/java | sed "s:bin/java::")
RUN mv hadoop-3.3.6 /usr/local/hadoop
ENV PATH /usr/local/hadoop/bin:$PATH

# Clean up
RUN rm -rf hadoop-3*

# Set the working directory
WORKDIR /usr/local/hadoop
