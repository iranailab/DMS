#!/bin/bash

# Build the Docker image
docker build -t dms-app .

# Run the Docker container
docker run -p 8000:8000 --name dms-container dms-app