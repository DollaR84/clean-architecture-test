# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src /app

# Ensure the entrypoint script is executable
RUN chmod a+x /app/entrypoint.sh

RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  libpq-dev \
  build-essential \
  chromium-driver \
  && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
  && pip install -r /app/requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["sh", "src/entrypoint.sh"]
