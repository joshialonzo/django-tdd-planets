# Planets Project

This is a set of restful endpoints to show planets information with terrains and climates together. You can see, add, update, and delete planets from the database. See the list of endpoints below.

| Endpoint         | HTTP Method | CRUD Method | Result          |
|------------------|-------------|-------------|-----------------|
| /api/planets      | GET         | READ        | get all planets  |
| /api/planets/:id  | GET         | READ        | get a single planet |
| /api/planets      | POST        | CREATE      | add a planet     |
| /api/planets/:id  | PUT         | UPDATE      | update a planet  |
| /api/planets/:id  | DELETE      | DELETE      | delete a planet  |

You can populate the database using a Django Command through a GraphQL API endpoint. The data model is composed of three models: Planet, Terrain, and Climate with the following fields:

* Planet
    * name
    * population
    * terrains
    * climates
* Terrain
    * name
* Climate
    * name

## Run the project

To run the project you need to install Docker and Docker Compose in your machine. Move to the folder where there is a docker-compose file and run:

```bash
docker-compose up -d --build
```

## Run tests

Some unit tests were created to verify basic functionality of the project. These can run with this command:

```bash
docker-compose exec planets pytest
```

## Populate the database

A GraphQL API endpoint can be used to populate the three different models using:

```bash
docker-compose exec planets python manage.py populate
```

## Create a super user

If you want to see the populated elements in the database, you will need to create a superuser:

```bash
docker-compose exec planets python manage.py createsuperuser
```

## References

* [GraphQL Clients](https://graphql.org/graphql-js/graphql-clients/)
* [GraphQL Clients with Python](https://graphql.org/community/tools-and-libraries/?tags=python)
* [Python GraphQL Client: GQL](https://github.com/graphql-python/gql)
* [How to create custom django-admin commands](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/)
