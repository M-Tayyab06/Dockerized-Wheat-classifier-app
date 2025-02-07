# Using official python image
FROM python:3.10-slim

# Setting the working directory
WORKDIR /app

# Installing system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt file
COPY requirements.txt .

# Installing python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of application 
COPY . .

# Exposing Port
EXPOSE 8501

# Running the application 
CMD ["streamlit","run","owl.py","--server.port=8501","--server.address=0.0.0.0"]
