FROM python:3.12-slim

# Install WeasyPrint and PostgreSQL dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libgirepository1.0-dev \
    libglib2.0-0 \
    libglib2.0-dev \
    libpq-dev \
    shared-mime-info \
    netcat-openbsd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Set workdir
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Entrypoint (optional script for waiting DB, etc.)
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy the rest of the application code
COPY . .

# Entrypoint handles migrations, collectstatic, etc.
ENTRYPOINT ["/entrypoint.sh"]

# Default command: Django dev server (for production, replace with gunicorn)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
