FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for OpenCV)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Create uploads folder
RUN mkdir -p static/uploads

# Expose port (Hugging Face uses 7860)
EXPOSE 7860

# Run Flask app
CMD ["python", "app.py"]