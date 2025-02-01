from fastapi import APIRouter, HTTPException
from starlette import status

from models import Family
from starlette.responses import JSONResponse

router = APIRouter()

families_db = [
    Family(id=1, name="The Simpsons", members=[1, 2, 3, 4, 5], description="The main family of the show."),
    Family(id=2, name="The Flanders", members=[6], description="The Simpsons' religious neighbors."),
    Family(id=3, name="The Burns", members=[],
           description="The wealthy and influential owner of the Springfield Nuclear Power Plant."),
    Family(id=4, name="The Krustofskys", members=[8], description="The family of Krusty the Clown."),
    Family(id=5, name="The Wiggums", members=[9], description="The family of Chief Wiggum."),
    Family(id=6, name="The Van Houtens", members=[10], description="Milhouse's family.")
]


@router.get("/families/", response_model=list[Family], tags=["Семьи 👨‍👩‍👧‍👦"])
def get_families():
    return families_db


@router.get("/families/{family_id}", response_model=Family, tags=["Семьи 👨‍👩‍👧‍👦"])
def get_family(family_id: int):
    family = next((f for f in families_db if f.id == family_id), None)
    if family is None:
        raise HTTPException(status_code=404, detail="Family not found")
    return family


@router.post("/families/", response_model=Family, tags=["Семьи 👨‍👩‍👧‍👦"])
def create_family(family: Family):
    families_db.append(family)
    return family


@router.patch("/families/{family_id}", response_model=Family, tags=["Семьи 👨‍👩‍👧‍👦"])
def update_family(family_id: int, updated_family: Family):
    family = next((f for f in families_db if f.id == family_id), None)
    if family is None:
        raise HTTPException(status_code=404, detail="Family not found")
    family.name = updated_family.name
    family.members = updated_family.members
    family.description = updated_family.description
    return family


@router.delete("/families/{family_id}", tags=["Семьи"], status_code=status.HTTP_202_ACCEPTED, summary="Удалить семью")
def delete_family(family_id: int):
    family_index = next((index for index, f in enumerate(families_db) if f.id == family_id), None)

    if family_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Family not found"
        )

    del families_db[family_index]

    return {"message": "Family deleted"}
