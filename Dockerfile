FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for OpenCV and ADB
RUN apt-get update && apt-get install -y \
    android-tools-adb \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose Flask port
EXPOSE 5000

CMD ["python", "app.py"]
