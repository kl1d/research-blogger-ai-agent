FROM python:3.10-slim
WORKDIR /app

# Set Python environment
ENV FLASK_APP=web.app

# Install dependencies
COPY web/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

EXPOSE 5000

# Run with auto-reload
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
