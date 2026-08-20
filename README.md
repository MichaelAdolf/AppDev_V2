FROM python:3.11-slim

ARG BUILD_VERSION
ARG BUILD_ARCH

LABEL \
    io.hass.version="${BUILD_VERSION}" \
    io.hass.type="addon" \
    io.hass.arch="${BUILD_ARCH}"

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src
ENV STOCKMIND_DB_PATH=/share/stockmind/stockmind.db

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

COPY api /app/api
COPY src /app/src
COPY scripts /app/scripts
COPY run.sh /run.sh

RUN chmod a+x /run.sh \
    && mkdir -p /share/stockmind

EXPOSE 8000

CMD ["/run.sh"]
