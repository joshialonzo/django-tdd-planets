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
        """
        Initializes a GraphQL client with the given URL.

        Args:
            url (str): The URL of the GraphQL server.

        Returns:
            Client: The initialized GraphQL client.

        """
        transport = AIOHTTPTransport(url=url)
        return Client(transport=transport, fetch_schema_from_transport=True)

    def execute_query(self, client):
        """
        Executes the GraphQL query using the provided client.

        Args:
            client: The GraphQL client used to execute the query.

        Returns:
            The result of the query execution.

        """
        query = gql(self.string)
        return client.execute(query)
    
    def get_planets(self):
        """
        Retrieves a list of planets from the GraphQL API.

        Returns:
            A list of planets retrieved from the API.
        """
        try:
            client = self.init_gql_client(self.url)
            result = self.execute_query(client)
            return result["allPlanets"]["planets"]
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
            return []

    def create_or_update_planet(self, planet):
        """
        Creates or updates a planet in the database.

        Args:
            planet (dict): A dictionary containing the planet's name and population.

        Returns:
            Planet: The created or updated planet object.

        """
        planet_name = planet["name"]
        population = planet["population"]
        planet, _ = Planet.objects.update_or_create(
            name=planet_name,
            defaults={"population": population},
        )
        self.stdout.write(self.style.SUCCESS(f"Planet: {planet_name}"))
        return planet

    def add_terrains_to_planet(self, planet, terrains):
        """
        Add terrains to a planet.

        Args:
            planet (Planet): The planet to add terrains to.
            terrains (list): A list of terrain names to add.

        Returns:
            None
        """
        for terrain in terrains:
            terrain_obj, _ = Terrain.objects.get_or_create(name=terrain)
            planet.terrains.add(terrain_obj)

    def add_climates_to_planet(self, planet, climates):
        """
        Adds the given climates to the specified planet.

        Args:
            planet (Planet): The planet to which the climates will be added.
            climates (list): A list of climate names to be added.

        Returns:
            None
        """
        for climate in climates:
            climate_obj, _ = Climate.objects.get_or_create(name=climate)
            planet.climates.add(climate_obj)

    def populate_database(self, planets):
        """
        Populates the database with planet data.

        Args:
            planets (list): A list of planet dictionaries containing planet data.

        Returns:
            None
        """
        for planet in planets:
            planet_obj = self.create_or_update_planet(planet)
            self.add_terrains_to_planet(planet_obj, planet.get("terrains", []))
            self.add_climates_to_planet(planet_obj, planet.get("climates", []))

    def handle(self, *args, **options):
        """
        Handle method for the populate command.

        This method is called when the populate command is executed. It queries the planets,
        populates the database with the retrieved planets, and prints a success message.

        Returns:
            None
        """
        self.stdout.write("Querying planets...")

        planets = self.get_planets()
        self.populate_database(planets)

        self.stdout.write("Done!")
