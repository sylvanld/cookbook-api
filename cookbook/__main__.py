from click import Group as CliGroup

from cookbook.api.factory import create_api
from cookbook.core.config import EnvironmentConfig
from cookbook.core.extensions import ExtensionsManager
from cookbook.core.logging import setup_logging
from cookbook.extensions.database import DatabaseExtension

cli = CliGroup()
config = EnvironmentConfig()

setup_logging(config)

api = create_api(config)

extensions = ExtensionsManager(api, cli, config)
extensions.register(DatabaseExtension)


if __name__ == "__main__":
    cli()
