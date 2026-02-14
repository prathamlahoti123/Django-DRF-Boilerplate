# Build image
FROM ghcr.io/astral-sh/uv:python3.12-alpine AS builder

# https://docs.astral.sh/uv/reference/environment
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0

ARG DEV=false

WORKDIR /build

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

COPY ./pyproject.toml ./uv.lock ./run.sh ./src/ /build

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --locked && \
    if [ $DEV = "true" ]; then uv sync --group dev --locked; fi && \
    chmod +x ./run.sh


# Final image
FROM ghcr.io/astral-sh/uv:python3.12-alpine

ARG USER=nonroot \
    GROUP_GID=12345 \
    USER_UID=12345

WORKDIR /src

RUN apk add --no-cache curl && \
    addgroup --system --gid $GROUP_GID $USER && \
    adduser \
    --system \
    --disabled-password \
    --no-create-home $USER \
    --ingroup $USER \
    --uid $USER_UID \
    $USER && \
    mkdir -p ./staticfiles/ ./logs/ && \
    chown -R $USER:$USER /src

COPY --from=builder /build /src

USER $USER

ENV PATH="/src/.venv/bin:$PATH"

EXPOSE 8000

CMD ["./run.sh"]
