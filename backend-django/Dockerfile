FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/backend

COPY requirements.txt /app/backend/

# Build psycopg2-binary from source -- add required dependencies
RUN apk add --virtual .build-deps --no-cache postgresql-dev gcc python3-dev musl-dev && \
        pip install --no-cache-dir -r requirements.txt && \
        apk --purge del .build-deps

COPY . /app/backend/

# Copy entrypoint script
COPY entrypoint.sh /app/backend/

# Set the entrypoint
ENTRYPOINT ["/app/backend/entrypoint.sh"]

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
