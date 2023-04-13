from dependency_injector import containers, providers


__all__ = [
    "Repositories",
    "JWTRefreshTokenRepository",
    "UserRepository",
    "RoomRepository",
    "UserRoomMappingRepository",
]


class Repositories(containers.DeclarativeContainer):
    user_repository = providers.Factory(UserRepository)
    refresh_token_repository = providers.Factory(JWTRefreshTokenRepository)
    room_repository = providers.Factory(RoomRepository)
    user_room_mapping_repository = providers.Factory(UserRoomMappingRepository)
    message_type_repository = providers.Factory(MessageTypeRepository)
    message_repository = providers.Factory(MessageRepository)
    user_role = providers.Factory(UserRoleRepository)
