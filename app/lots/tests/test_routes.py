from http import HTTPStatus

import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.lots.models import Lot
from app.main import router
from app.utils import is_response_match_object_fields


async def test_lot_retrieve(client: AsyncClient, lot: Lot, session: AsyncSession):
    response = await client.get(router.url_path_for("lot:retrieve", lot_id=lot.id))

    assert response.status_code == HTTPStatus.OK
    assert is_response_match_object_fields(
        response.json(),
        lot,
        (
            "title",
            "description",
            "starting_price",
        ),
    )


async def test_lot_create(client: AsyncClient, session: AsyncSession):
    data = {
        "title": "Test",
        "description": "Test",
        "starting_price": 100,
    }
    response = await client.post(
        router.url_path_for("lot:create"),
        json=data,
    )

    query = select(Lot).where(Lot.id == response.json()["id"])
    result = await session.execute(query)

    assert response.status_code == HTTPStatus.CREATED
    assert is_response_match_object_fields(
        response.json(),
        result.scalar_one_or_none(),
        ("title", "description", "starting_price"),
    )


if __name__ == "__main__":
    pytest.main()
