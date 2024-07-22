## Run the project

Install Docker and Docker Compose, then run:

```bash
docker-compose up -d --build
```

## Run tests

```bash
docker-compose exec planets pytest
```

## Populate the database

```bash
docker-compose exec planets python manage.py query_planets
```

## References

* [GraphQL Clients](https://graphql.org/graphql-js/graphql-clients/)
* [GraphQL Clients with Python](https://graphql.org/community/tools-and-libraries/?tags=python)
* [Python GraphQL Client: GQL](https://github.com/graphql-python/gql)
* [How to create custom django-admin commands](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/)