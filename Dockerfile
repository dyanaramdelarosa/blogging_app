FROM python:3.13

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # PIP CONFIG
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# System dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        bash \
        build-essential \
        curl \
        gettext \
        git \
        libpq-dev \
        wget \
    # Cleaning cache
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*


WORKDIR /home/app
COPY requirements.txt /home/app
RUN pip install -r requirements.txt

COPY main.py /home/app
COPY blogging_app /home/app/blogging_app
CMD ["python", "main.py"]