# 1. Use an official Python base image
FROM python:3.10-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Set work directory inside container
WORKDIR /app

# 4. Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 6. Copy project files
COPY . /app/

# 7. Collect static files (without running the dev server)
RUN python manage.py collectstatic --noinput

# 8. Expose port 8000
EXPOSE 8000

# 9. Run the app using gunicorn (production-ready server)
CMD ["gunicorn", "LMSPROJECT.wsgi:application", "--bind", "0.0.0.0:8000"]
