"""Server configuration."""
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app import on_startup
from src.app import EndpointFilter
from src.app.internal import handle_api_exceptions
from src.app.internal import __routes__
from src.app.pkg import BaseAPIException
from src.app.pkg import FastAPITypes
from src.app.pkg.settings import settings

__all__ = ["Server"]


class Server:
    """Register all requirements for correct work of server instance."""

    __app: FastAPI
    __app_name: str = settings.API_INSTANCE_APP_NAME

    def __init__(self, app: FastAPI):
        self.__app = app
        self._register_routes(app)
        self._register_events(app)
        self._register_middlewares(app)
        self._register_http_exceptions(app)

    def get_app(self) -> FastAPI:
        """Get current application instance.

        Returns: ``FastAPI`` application instance.
        """
        return self.__app

    @staticmethod
    def _register_events(app: FastAPITypes.FastAPIInstance) -> None:
        """Register on startup events.

        Args:
            app: ``FastAPI`` application instance.

        Returns: None
        """

        app.on_event("startup")(on_startup)

    @staticmethod
    def _register_routes(app: FastAPITypes.FastAPIInstance) -> None:
        """Include routers in ``FastAPI`` instance from ``__routes__``.

        Args:
            app: ``FastAPI`` application instance.

        Returns: None
        """

        __routes__.register_routes(app)

    @staticmethod
    def _register_http_exceptions(app: FastAPITypes.FastAPIInstance) -> None:
        """Register http exceptions.

        FastAPIInstance handle BaseApiExceptions raises inside functions.

        Args:
            app: ``FastAPI`` application instance

        Returns: None
        """

        app.add_exception_handler(BaseAPIException, handle_api_exceptions)

    @staticmethod
    def __register_cors_origins(app: FastAPITypes.FastAPIInstance) -> None:
        """Register cors origins."""

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _register_middlewares(self, app) -> None:
        """Apply routes middlewares."""

        self.__register_cors_origins(app)

    @staticmethod
    def __filter_logs(endpoint: str) -> None:
        """Filter ignore /metrics in uvicorn logs."""
        logging.getLogger("uvicorn.access").addFilter(EndpointFilter(endpoint=endpoint))
