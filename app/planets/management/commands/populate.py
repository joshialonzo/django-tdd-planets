from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

from django.core.management.base import BaseCommand, CommandError

from planets.models import Climate
from planets.models import Planet
from planets.models import Terrain


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
        try:
            client = self.init_gql_client(self.url)
            result = self.execute_query(client)
            return result["allPlanets"]["planets"]
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
            return []

    def create_or_update_planet(self, planet):
        planet_name = planet["name"]
        population = planet["population"]
        planet, _ = Planet.objects.update_or_create(
            name=planet_name,
            defaults={"population": population},
        )
        self.stdout.write(self.style.SUCCESS(f"Planet: {planet_name}"))
        return planet

    def add_terrains_to_planet(self, planet, terrains):
        for terrain in terrains:
            terrain_obj, _ = Terrain.objects.get_or_create(name=terrain)
            planet.terrains.add(terrain_obj)

    def add_climates_to_planet(self, planet, climates):
        for climate in climates:
            climate_obj, _ = Climate.objects.get_or_create(name=climate)
            planet.climates.add(climate_obj)

    def populate_database(self, planets):
        for planet in planets:
            planet_obj = self.create_or_update_planet(planet)
            self.add_terrains_to_planet(planet_obj, planet.get("terrains", []))
            self.add_climates_to_planet(planet_obj, planet.get("climates", []))

    def handle(self, *args, **options):
        self.stdout.write("Querying planets...")

        planets = self.get_planets()
        self.populate_database(planets)

        self.stdout.write("Done!")
