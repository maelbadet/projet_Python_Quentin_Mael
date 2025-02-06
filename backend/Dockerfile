# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN pip install fastapi uvicorn pytest python-dotenv sqlalchemy pymysql

# Expose backend port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]