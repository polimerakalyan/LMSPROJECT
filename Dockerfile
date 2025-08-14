# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies without cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only application code
COPY . .

# Expose port (if needed)
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
