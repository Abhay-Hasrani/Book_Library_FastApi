# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code to the container image
COPY . .


# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh

# this for execute permissions to entrypoint script
RUN chmod +x /entrypoint.sh

# Setting the entrypoint
ENTRYPOINT ["/entrypoint.sh"]