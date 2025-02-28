# Use Python 3.12 slim base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV FLASK_APP=api.py
ENV FLASK_ENV=production
ENV PORT=5000

# Create data directory if it doesn't exist
RUN mkdir -p data

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "api.py"]