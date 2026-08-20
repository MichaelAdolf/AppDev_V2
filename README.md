ARG BUILD_FROM
FROM $BUILD_FROM

WORKDIR /app

COPY . /app

RUN apk add --no-cache \
    python3 \
    py3-pip

RUN pip install --no-cache-dir -r requirements.txt

ENV STOCKMIND_DB_PATH=/config/stockmind/stockmind.db

EXPOSE 8000

CMD ["uvicorn", "api.stockmind_api:app", "--host", "0.0.0.0", "--port", "8000"]
