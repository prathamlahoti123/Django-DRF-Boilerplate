# Build image
FROM ghcr.io/astral-sh/uv:python3.12-alpine AS builder

# https://docs.astral.sh/uv/reference/environment
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_DEV=1 \
    UV_PYTHON_DOWNLOADS=0

WORKDIR /build

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

COPY pyproject.toml uv.lock run.sh src/ /build

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked && \
    chmod +x ./run.sh


# Final image
FROM ghcr.io/astral-sh/uv:python3.12-alpine

ARG USER=nonroot \
    GROUP_GID=12345 \
    USER_UID=12345

RUN addgroup --system --gid $GROUP_GID $USER && \
    adduser \
    --system \
    --disabled-password \
    --no-create-home $USER \
    --ingroup $USER \
    --uid $USER_UID \
    $USER

COPY --from=builder --chown=$USER:$USER /build /src

ENV PATH="/src/.venv/bin:$PATH"

USER $USER

WORKDIR /src

EXPOSE 8000

CMD ["./run.sh"]
