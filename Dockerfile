FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install fastapi
RUN pip install aiofiles
RUN pip install PyYAML
RUN pip install jinja2
COPY ./app /app