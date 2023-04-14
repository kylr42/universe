"""All connectors in declarative container."""

from dependency_injector import containers, providers

from src.app.pkg.settings import settings

from .postgresql import Postgresql

__all__ = [
    "Connectors",
    "Postgresql",
]


class Connectors(containers.DeclarativeContainer):
    """Declarative container with connectors."""

    configuration = providers.Configuration(
        name="settings",
        pydantic_settings=[settings],
    )

    # Create {% if database_type == "{% if database_type == "postgresql"%}postgresql{% endif %}" %}{% if database_type == "postgresql"%}postgresql{% endif %}{%endif%} connector.
    postgresql = providers.Factory(
        Postgresql,
        username=configuration.POSTGRES_USER,
        password=configuration.POSTGRES_PASSWORD,
        host=configuration.POSTGRES_HOST,
        port=configuration.POSTGRES_PORT,
        database_name=configuration.POSTGRES_DATABASE_NAME,
    )
