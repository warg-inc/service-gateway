FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock* README.md ./
RUN uv sync --frozen --no-dev --no-install-project

COPY src/ ./src/

RUN mkdir -p ./src/protos/generated && \
    touch ./src/protos/generated/__init__.py && \
    ./.venv/bin/python -m grpc_tools.protoc \
    -I./src/protos \
    --python_out=./src/protos/generated \
    --grpc_python_out=./src/protos/generated \
    ./src/protos/auth.proto \
    ./src/protos/user.proto && \
    sed -i 's/^import \(.*_pb2\) as/from src.protos.generated import \1 as/' \
    ./src/protos/generated/*_pb2_grpc.py

RUN useradd -m appuser
RUN chown -R appuser:appuser /app

ENV PATH="/app/.venv/bin:$PATH"

USER appuser

CMD ["uvicorn", "src.setup.app_factory:create_web_app", "--host","0.0.0.0", "--port","8000", "--factory"]
