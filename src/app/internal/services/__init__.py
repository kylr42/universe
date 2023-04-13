from dependency_injector import containers, providers

from src.app.internal.repository import Repositories, postgresql
from src.app.internal.services import auth, message, message_type, room, user, user_roles
from src.app.pkg.settings import settings

__all__ = ["Services", "auth", "user", "room", "message_type", "message"]


class Services(containers.DeclarativeContainer):
    """Containers with services."""

    configuration = providers.Configuration(
        name="settings",
        pydantic_settings=[settings],
    )

    repositories: postgresql.Repositories = providers.Container(
        Repositories.postgres,
    )  # type: ignore
    user_role_service = providers.Factory(
        user_roles.UserRoleService,
        repositories.user_role,
    )
    user_service = providers.Factory(user.UserService, repositories.user_repository)

    auth_service = providers.Factory(
        auth.AuthService,
        user_service=user_service,
        refresh_token_repository=repositories.refresh_token_repository,
    )

    room_service = providers.Factory(
        room.RoomService,
        room_repository=repositories.room_repository,
        user_room_mapping_repository=repositories.user_room_mapping_repository,
    )

    message_type_service = providers.Factory(
        message_type.MessageTypeService,
        message_type_repository=repositories.message_type_repository,
    )

    message_service = providers.Factory(
        message.MessageService,
        message_repository=repositories.message_repository,
        user_room_mapping_repository=repositories.user_room_mapping_repository,
    )
