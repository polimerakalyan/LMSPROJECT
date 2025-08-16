# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose Django port
EXPOSE 8000

# Run Django app with Gunicorn (better than runserver for production)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "lms_main.wsgi:application"]
