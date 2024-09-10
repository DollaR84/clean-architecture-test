# Clean Architecture Test
Clean Architecture Test Project

* Build image:
``docker build \
  --build-arg POSTGRES_DB=yourdbname \
  --build-arg POSTGRES_USER=yourdbuser \
  --build-arg POSTGRES_PASSWORD=yourdbpassword \
  --build-arg POSTGRES_HOST=yourdbhost \
  --build-arg POSTGRES_PORT=yourdbport \
  -t yourimagename .``

  * Run container

``  docker run -d \
  -p 8000:8000 \
  --name yourcontainername \
  yourimagename``

