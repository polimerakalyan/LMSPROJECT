# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy requirements.txt first and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose Django default port
EXPOSE 8000

# Run the app using Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
