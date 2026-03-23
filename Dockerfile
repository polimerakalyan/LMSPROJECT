# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run with Gunicorn (PRODUCTION)
CMD ["gunicorn", "LMSPROJECT.wsgi:application", "--bind", "0.0.0.0:8000"]
