FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY lib/ lib/

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["app.py", "--server.address=0.0.0.0", "--server.port=8501"]
