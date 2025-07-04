FROM python:3.12-slim

WORKDIR /app

# Install system dependencies (for psycopg2-binary)
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "-c", "sqlmesh plan && python alert.py"]
