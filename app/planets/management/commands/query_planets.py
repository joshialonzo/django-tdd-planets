from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Populate the database with planets"
    url = "https://swapi-graphql.netlify.app/.netlify/functions/index"
    string = "query Query {allPlanets{planets{name population terrains climates}}}"

    def init_gql_client(self, url):
        transport = AIOHTTPTransport(url=url)
        return Client(transport=transport, fetch_schema_from_transport=True)

    def execute_query(self, client):
        query = gql(self.string)
        return client.execute(query)
    
    def get_planets(self):
        client = self.init_gql_client(self.url)
        result = self.execute_query(client)
        return result["allPlanets"]["planets"]

    def print_planets(self, planets):
        print(planets)
        for planet in planets:
            planet_name = planet["name"]
            self.stdout.write(self.style.SUCCESS(f"Planet: {planet_name}"))

    def handle(self, *args, **options):
        self.stdout.write("Querying planets...")

        planets = self.get_planets()
        self.print_planets(planets)

        self.stdout.write("Done!")
