from typing import List

from src.app.internal import get_connection
from src.app.internal import (
    collect_response,
)
from src.app.internal.repository.repository import Repository
from src.app.pkg import models

__all__ = ["UserRepository"]


class UserRepository(Repository):
    @collect_response
    async def create(self, cmd: models.CreateUserCommand) -> models.User:
        q = """
            insert into users(
                username, password, phone_number, is_active, role_id
            ) values (
                %(username)s,
                %(password)s::bytea,
                %(phone_number)s,
                %(is_active)s,
                (select id from user_roles where role_name = %(role_name)s)
            )
            returning id, username, password, phone_number, is_active, (
                select role_name from user_roles where role_name = %(role_name)s
            );
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict(show_secrets=True))
            return await cur.fetchone()

    @collect_response
    async def read(self, query: models.ReadUserByIdQuery) -> models.User:
        q = """
            select
                users.id,
                username,
                password,
                phone_number,
                is_active,
                ur.role_name
            from users
                left join user_roles ur on ur.id = users.role_id
            where users.id = %(id)s;
        """
        async with get_connection() as cur:
            await cur.execute(q, query.to_dict(show_secrets=True))
            return await cur.fetchone()

    @collect_response
    async def read_by_username(
        self,
        query: models.ReadUserByUserNameQuery,
    ) -> models.User:
        q = """
            select
                users.id, username, password, phone_number, is_active, ur.role_name as role_name
            from users
                left join user_roles ur on ur.id = users.role_id
            where username = %(username)s
        """
        async with get_connection() as cur:
            await cur.execute(q, query.to_dict(show_secrets=True))
            return await cur.fetchone()

    @collect_response
    async def read_all(self) -> List[models.User]:
        q = """
            select
                users.id,
                username,
                password,
                phone_number,
                is_active,
                ur.role_name
            from users
                left join user_roles ur on ur.id = users.role_id;
        """
        async with get_connection() as cur:
            await cur.execute(q)
            return await cur.fetchall()

    @collect_response
    async def update(self, cmd: models.UpdateUserCommand) -> models.User:
        q = """
            with ur as (
                select id, role_name from user_roles where role_name = %(role_name)s
            )
            update users
                set
                    username = %(username)s,
                    password = %(password)s,
                    phone_number = %(phone_number)s,
                    password_updated_at = current_timestamp
                where id = %(id)s
            returning
                id, username, password, phone_number
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict(show_secrets=True))
            return await cur.fetchone()

    @collect_response
    async def update_user_status(
        self,
        cmd: models.UpdateUserStatusCommand,
    ) -> models.User:
        q = """
            update users
                set is_active = %(is_active)s
                where id = %(id)s
            returning
                id, username, password, phone_number, is_active, (
                    select role_name from user_roles where id = users.role_id
                );
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict(show_secrets=True))
            return await cur.fetchone()

    @collect_response
    async def delete(self, cmd: models.DeleteUserCommand) -> models.User:
        q = """
            delete from users where id = %(id)s
            returning id, username, password, phone_number, is_active, (
                select role_name from user_roles where id = users.role_id
            );
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict(show_secrets=True))
            return await cur.fetchone()
