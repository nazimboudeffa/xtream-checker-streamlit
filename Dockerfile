# app/Dockerfile

FROM public.ecr.aws/docker/library/python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/nazimboudeffa/xtream-checker-streamlit.git . \
    && pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD ["curl", "--fail", "http://localhost:8501/_stcore/health"]

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]