FROM python:3.12

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    curl

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

ENV RYE_HOME="/opt/rye"
ENV PATH="$RYE_HOME/shims:$PATH"

RUN curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash && \
    rye config --set-bool behavior.global-python=true && \
    rye config --set-bool behavior.use-uv=true

COPY pyproject.toml .python-version README.md /app/

RUN rye pin "$(cat .python-version)" && \
    rye sync
