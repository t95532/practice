# Use a lightweight official Python image
FROM python:3.10-slim

# Prevent Python from writing .pyc files & enable logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (needed for numpy / sklearn)
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY lib/ lib/
COPY .streamlit /app/.streamlit

# Expose Streamlit default port
EXPOSE 8501

# 🔥 Override base image ENTRYPOINT and run Streamlit correctly
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py", "--server.address=0.0.0.0", "--server.port=8501"]
