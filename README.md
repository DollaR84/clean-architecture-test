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


* create enums in postgresql database:
Connect to psql in database service, use database_name and run:
CREATE TYPE status_type AS ENUM ('NOT_STARTED', 'PENDING', 'PARSING', 'SAVING', 'DONE', 'ERROR');
