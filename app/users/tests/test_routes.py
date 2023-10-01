from http import HTTPStatus

import pytest
from fastapi_users.password import PasswordHelper
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.users.models import User
from app.utils import is_response_match_object_fields


async def test_register_route(client: AsyncClient, session: AsyncSession):
    data = {
        "name": "TestName",
        "email": "email@example.com",
        "password": "*%&$#(%*$&$#*%&",
    }
    response = await client.post("api/v1/users/register", json=data)

    response_data = response.json()

    query = select(User).where(User.id == response_data["id"])
    result = await session.execute(query)

    assert response.status_code == HTTPStatus.CREATED
    assert is_response_match_object_fields(
        response.json(),
        result.scalar_one_or_none(),
        ("name", "email"),
    )


async def test_user_login(client: AsyncClient, session: AsyncSession):
    password = "*%&$#(%*$&$#*%&"
    data = {
        "name": "TestName",
        "email": "email@example.com",
        "hashed_password": PasswordHelper().hash(password),
    }
    user = User(**data)  # noqa
    session.add(user)
    await session.commit()

    response = await client.post(
        "api/v1/users/login",
        data={
            "username": data["email"],
            "password": password,
        },
    )

    assert response.status_code == HTTPStatus.OK


if __name__ == "__main__":
    pytest.main()
