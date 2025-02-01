# import pytest
# from httpx import AsyncClient
# from main import app
#
#
# @pytest.fixture
# async def client():
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         yield client
#
#
# # Тесты для персонажей
# @pytest.mark.asyncio
# async def test_get_characters(client):
#     response = await client.get("/characters/")
#     assert response.status_code == 200
#     assert len(response.json()) > 0
#
#
# @pytest.mark.asyncio
# async def test_get_character_by_id(client):
#     response = await client.get("/characters/1")
#     assert response.status_code == 200
#     assert response.json()["id"] == 1
#
#
# @pytest.mark.asyncio
# async def test_get_character_not_found(client):
#     response = await client.get("/characters/999")
#     assert response.status_code == 404
#
#
# @pytest.mark.asyncio
# async def test_create_character(client):
#     new_character = {
#         "id": 11,
#         "name": "New Character",
#         "age": 30,
#         "occupation": "New Occupation",
#         "catchphrase": "New Catchphrase",
#         "family_id": 1
#     }
#     response = await client.post("/characters/", json=new_character)
#     assert response.status_code == 200
#     assert response.json()["name"] == "New Character"
#
#
# @pytest.mark.asyncio
# async def test_update_character(client):
#     updated_character = {
#         "name": "Updated Name",
#         "age": 40,
#         "occupation": "Updated Occupation",
#         "catchphrase": "Updated Catchphrase",
#         "family_id": 2
#     }
#     response = await client.patch("/characters/1", json=updated_character)
#     assert response.status_code == 200
#     assert response.json()["name"] == "Updated Name"
#
#
# @pytest.mark.asyncio
# async def test_delete_character(client):
#     response = await client.delete("/characters/1")
#     assert response.status_code == 202
#     response = await client.get("/characters/1")
#     assert response.status_code == 404
#
#
# # для семей
# @pytest.mark.asyncio
# async def test_get_families(client):
#     response = await client.get("/families/")
#     assert response.status_code == 200
#     assert len(response.json()) > 0
#
#
# @pytest.mark.asyncio
# async def test_get_family_by_id(client):
#     response = await client.get("/families/1")
#     assert response.status_code == 200
#     assert response.json()["id"] == 1
#
#
# @pytest.mark.asyncio
# async def test_create_family(client):
#     new_family = {
#         "id": 7,
#         "name": "New Family",
#         "members": [],
#         "description": "New Description"
#     }
#     response = await client.post("/families/", json=new_family)
#     assert response.status_code == 200
#     assert response.json()["name"] == "New Family"
#
#
# @pytest.mark.asyncio
# async def test_update_family(client):
#     updated_family = {
#         "name": "Updated Family Name",
#         "members": [1, 2, 3],
#         "description": "Updated Description"
#     }
#     response = await client.patch("/families/1", json=updated_family)
#     assert response.status_code == 200
#     assert response.json()["name"] == "Updated Family Name"
#
#
# @pytest.mark.asyncio
# async def test_delete_family(client):
#     response = await client.delete("/families/1")
#     assert response.status_code == 202
#     response = await client.get("/families/1")
#     assert response.status_code == 404
#
#
# # для песен
# @pytest.mark.asyncio
# async def test_get_songs(client):
#     response = await client.get("/songs/")
#     assert response.status_code == 200
#     assert len(response.json()) > 0
#
#
# @pytest.mark.asyncio
# async def test_get_song_by_id(client):
#     response = await client.get("/songs/1")
#     assert response.status_code == 200
#     assert response.json()["id"] == 1
#
#
# @pytest.mark.asyncio
# async def test_create_song(client):
#     new_song = {
#         "id": 11,
#         "title": "New Song",
#         "lyrics": "New Lyrics",
#         "character_id": 1,
#         "episode": "New Episode"
#     }
#     response = await client.post("/songs/", json=new_song)
#     assert response.status_code == 200
#     assert response.json()["title"] == "New Song"
#
#
# @pytest.mark.asyncio
# async def test_update_song(client):
#     updated_song = {
#         "title": "Updated Song Title",
#         "lyrics": "Updated Lyrics",
#         "character_id": 2,
#         "episode": "Updated Episode"
#     }
#     response = await client.patch("/songs/1", json=updated_song)
#     assert response.status_code == 200
#     assert response.json()["title"] == "Updated Song Title"
#
#
# @pytest.mark.asyncio
# async def test_delete_song(client):
#     response = await client.delete("/songs/1")
#     assert response.status_code == 202
#     response = await client.get("/songs/1")
#     assert response.status_code == 404
import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

client = TestClient(app)

def test_get_characters():
    response = client.get("/characters/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_character_by_id():
    response = client.get("/characters/1")
    assert response.status_code == 200
    assert "name" in response.json()

def test_create_character():
    new_character = {
        "id": 11,
        "name": "Test Character",
        "age": 30,
        "occupation": "Tester",
        "catchphrase": "Test catchphrase",
        "family_id": 1
    }
    response = client.post("/characters/", json=new_character)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Character"

def test_update_character():
    updated_character = {
        "id": 1,
        "name": "Updated Character",
        "age": 35,
        "occupation": "Updated Occupation",
        "catchphrase": "Updated catchphrase",
        "family_id": 1
    }
    response = client.patch("/characters/1", json=updated_character)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Character"

def test_delete_character():
    response = client.delete("/characters/1")
    assert response.status_code == 202

def test_create_character_invalid_data():
    invalid_character = {"id": 12, "name": "Invalid Character", "age": "invalid_age", "occupation": "Tester"}
    response = client.post("/characters/", json=invalid_character)
    assert response.status_code == 422  # Unprocessable Entity

def test_delete_family():
    response = client.delete("/families/1")
    assert response.status_code == 202

def test_get_songs():
    response = client.get("/songs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_song_by_id():
    response = client.get("/songs/1")
    assert response.status_code == 200
    assert "title" in response.json()

def test_create_song():
    new_song = {"id": 1, "title": "New Song", "lyrics": "La la la", "character_id": 1, "episode": "Season 1"}
    response = client.post("/songs/", json=new_song)
    assert response.status_code == 200
    assert response.json()["title"] == "New Song"

def test_update_song():
    updated_song = {"id": 1, "title": "Updated Song", "lyrics": "Updated lyrics", "character_id": 1, "episode": "Season 1"}
    response = client.patch("/songs/1", json=updated_song)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Song"

def test_delete_song():
    response = client.delete("/songs/1")
    assert response.status_code == 202
