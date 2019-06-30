
```bash
docker build -t su_generator .

cd app/

docker run -d -p 8090:80 -v $(pwd):/app su_generator /start-reload.sh
```
Ref.: https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

