# Use the official Node.js image as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json to the working directory


# Copy the rest of the application to the working directory
COPY . .

# Specify the command to run when the container starts
CMD [ "node", "server.js" ]
