# movierama

## Demo environment
* Visit http://164.92.92.64/movies
* View the movies list, sort by (descending) date, number of likes or number of hates
* Click on a username to filter the movies that this user has added
* Select "Sign up" in order to create an account and add your own movies

## Local development
This a python django application.

Development environment is dockerized, however a few prerequisites are required in order to work on it.

### Environment prerequisites
* `python`
* `docker`
* `docker-compose`
* `git` and `pre-commit` library, if one wants to commit any changes. Install `pre-commit` with
```shell
pre-commit install
```

### Running the application locally
* Start the application with
```shell
docker-compose up -d --build
```

This creates a docker container named `db` that hosts the database, and a docker container named `django_app`, where the application runs.

* Access the app at `http://localhost:8000/movies`

* Note that if any of the ports that are used by the containers of this app is reserved, then `docker-compose up` will fail.
We can edit the exposed ports at `docker-compose.yml`

* Stop the application with
```shell
docker-compose stop
```

### Tools
* Access DB with pgadmin, at http://localhost:5050/
  * Credentials: `admin@admin.com` / `admin`
  * Database: `postgres@db:5432`/`postgres`
  * The above credentials can be edited at `docker-compose.yml`
* Manage docker containers with portainer, at http://localhost:9000/
  * It will ask to create an admin on the first visit
