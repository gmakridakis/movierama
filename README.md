# movierama

## Local development

### Environment prerequisites
* python3
* docker
* docker-compose
* pre-commit library, if one wants to use `git commit`. Install it with the following command:
```shell
pre-commit install
```

### Running the application
```shell
docker-compose up -d --build
```

This should create a docker container named `db` that hosts the DB, and a docker container named `django_app`, where the application runs.

### Tools
* Access DB with pgadmin, at http://localhost:5050/
  * Credentials: `admin@admin.com` / `admin`
  * Database: `postgres@db:5432`/`postgres`
  * The above credentials can be edited at `docker-compose.yml`
* Manage docker containers with portainer, at http://localhost:9000/
  * Will ask to create an admin on the first visit
