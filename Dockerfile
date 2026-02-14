FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock* README.md ./
RUN uv sync --frozen --no-dev --no-install-project

COPY src/ ./src/

RUN useradd -m appuser
RUN chown -R appuser:appuser /app

ENV PATH="/app/.venv/bin:$PATH"

USER appuser

CMD ["uvicorn", "src.setup.app_factory:create_web_app", "--host","0.0.0.0", "--port","8000", "--factory"]
