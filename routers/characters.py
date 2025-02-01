from fastapi import APIRouter, HTTPException
from starlette import status

from models import Character
from starlette.responses import JSONResponse

router = APIRouter()

# Временное хранилище данных с заранее добавленными персонажами
characters_db = [
    Character(id=1, name="Homer Simpson", age=39, occupation="Nuclear Safety Inspector", catchphrase="D'oh!",
              family_id=1),
    Character(id=2, name="Marge Simpson", age=36, occupation="Homemaker", family_id=1),
    Character(id=3, name="Bart Simpson", age=10, occupation="Student", catchphrase="Eat my shorts!", family_id=1),
    Character(id=4, name="Lisa Simpson", age=8, occupation="Student",
              catchphrase="If anyone wants me, I'll be in my room.", family_id=1),
    Character(id=5, name="Maggie Simpson", age=1, occupation="Baby", family_id=1),
    Character(id=6, name="Ned Flanders", age=60, occupation="Business Owner", catchphrase="Okily Dokily", family_id=2),
    Character(id=7, name="Mr. Burns", age=104, occupation="Owner of the Springfield Nuclear Power Plant",
              catchphrase="Excellent...", family_id=None),
    Character(id=8, name="Krusty the Clown", age=55, occupation="TV Clown", family_id=None),
    Character(id=9, name="Chief Wiggum", age=45, occupation="Police Chief", family_id=None),
    Character(id=10, name="Milhouse Van Houten", age=10, occupation="Student",
              catchphrase="Everything's coming up Milhouse!", family_id=None)
]


@router.get("/characters/", response_model=list[Character], tags=["Персонажи"],
            summary="Получить всех персонажей")
def get_characters():
    return characters_db


@router.get("/characters/{character_id}", response_model=Character, tags=["Персонажи"],
            summary="Получить конкретного персонажа по id")
def get_character(character_id: int):
    character = next((c for c in characters_db if c.id == character_id), None)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


@router.post("/characters/", response_model=Character, tags=["Персонажи"], summary="Добавить нового персонажа")
def create_character(character: Character):
    characters_db.append(character)
    return character


@router.patch("/characters/{character_id}", response_model=Character, tags=["Персонажи"],
              summary="Обновить информацию о персонаже")
def update_character(character_id: int, updated_character: Character):
    character = next((c for c in characters_db if c.id == character_id), None)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    character.name = updated_character.name
    character.age = updated_character.age
    character.occupation = updated_character.occupation
    character.catchphrase = updated_character.catchphrase
    character.family_id = updated_character.family_id
    return character


@router.delete("/characters/{character_id}", tags=["Персонажи"], status_code=status.HTTP_202_ACCEPTED,
               summary="Удалить персонажа")
def delete_character(character_id: int):
    character_index = next((index for index, c in enumerate(characters_db) if c.id == character_id), None)

    if character_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Character not found"
        )

    del characters_db[character_index]

    return {"message": "Character deleted"}
# @router.delete("/characters/{character_id}", response_model=Character, tags=["GKBP Персонажи"], summary="Удалить персонажа")
# def delete_character(character_id: int):
#     try:
#         # Поиск персонажа по ID
#         character_index = next((index for index, c in enumerate(characters_db) if c.id == character_id), None)
#         # Если персонаж не найден
#         if character_index is None:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail="Character not found"
#             )
#
#         # Удаление персонажа
#         del characters_db[character_index]
#         # Возвращаем успешный ответ
#         return {"message": "Character deleted"}, status.HTTP_202_ACCEPTED
#
#     except Exception as e:
#         # В случае других ошибок возвращаем 500
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail={
#                 "status": 500,
#                 "reason": str(e)
#             }
#         )
# @router.delete("/characters/{character_id}")
# def delete_character(character_id: int):
#     global characters_db
#     character = next((c for c in characters_db if c.id == character_id), None)
#     if character is None:
#         raise HTTPException(status_code=404, detail="Character not found")
#
#     characters_db = [c for c in characters_db if c.id != character_id]
#     return {"message": "Character deleted", "status": 202}
#
#
# @router.exception_handler(HTTPException)
# def custom_http_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=500,
#         content={"status": exc.status_code, "reason": exc.detail},
#     )
