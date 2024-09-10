# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG POSTGRES_DB
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
ARG POSTGRES_HOST
ARG POSTGRES_PORT

ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_HOST=${POSTGRES_HOST}
ENV POSTGRES_PORT=${POSTGRES_PORT}

# Set the working directory in the container to /app
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  libpq-dev \
  build-essential \
  chromium-driver \
  && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
  && pip install -r /app/requirements.txt \
  && chmod +x /app/startup.sh

# Make port 8000 available to the world outside this container
EXPOSE 8000


# Run the application
CMD ["/app/startup.sh"]

