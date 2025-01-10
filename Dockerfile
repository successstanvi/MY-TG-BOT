# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the container
COPY . /app/

# Install system dependencies (if necessary)
# Remove unnecessary apt packages
RUN apt-get update && apt-get install -y \
    # Add system dependencies if needed, e.g.:
    # libpq-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set file permissions (chmod +x)
RUN chmod +x /app/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "main.py"]
