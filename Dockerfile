# Build Stage
FROM python:3.9-slim-buster as wheel-builder

WORKDIR /app

RUN apt update && \
    apt install -y --no-install-recommends jq

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


# Final Stage
FROM python:3.9-slim-buster
WORKDIR /app

RUN pip install --upgrade pip setuptools wheel
RUN pip install gunicorn

COPY --from=wheel-builder /app/wheels /wheels
RUN pip install --no-cache /wheels/* && rm -rf /wheels

COPY --from=wheel-builder /app/requirements.txt .
COPY --from=wheel-builder /usr/bin/jq /usr/bin/jq

# Copy the application code
COPY tests /app/tests
COPY svc /app/svc
COPY app.py .

EXPOSE 5000
CMD ["gunicorn", "app:create_app()", "--bind", "0.0.0.0:5000"]

