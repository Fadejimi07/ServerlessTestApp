# Which version of python
FROM python:3.13.3-slim-bullseye

# What code and docs to copy
COPY . /app
WORKDIR /app/

# default installs
RUN apt-get update && \ 
    apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    gcc \
    make

# Create a virtual environment
RUN python -m venv /opt/venv && \
    /opt/venv/bin/python -m pip install --upgrade pip && \
    /opt/venv/bin/python -m pip install gunicorn && \
    /opt/venv/bin/python -m pip install -r requirements.txt

#purge unused
RUN apt-get purge -y --auto-remove build-essential python3-dev gcc make && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# make the entrypoint script executable
RUN chmod +x entrypoint.sh

# run the application
CMD ["./entrypoint.sh"]