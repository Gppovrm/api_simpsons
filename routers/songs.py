from fastapi import APIRouter, HTTPException
from starlette import status

from models import Song
from starlette.responses import JSONResponse

router = APIRouter()

songs_db = [
    Song(id=1, title="Spider Pig", lyrics="Spider Pig, Spider Pig, Does whatever a Spider Pig does", character_id=1, episode="The Simpsons Movie"),
    Song(id=2, title="We Do", lyrics="We Do! We Do!", character_id=7, episode="Homer the Great"),
    Song(id=3, title="See My Vest", lyrics="See my vest, see my vest, made from real gorilla chest", character_id=7, episode="Two Dozen and One Greyhounds"),
    Song(id=4, title="Baby on Board", lyrics="Baby on board, how I've adored", character_id=1, episode="Homer's Barbershop Quartet"),
    Song(id=5, title="Monorail Song", lyrics="Monorail! Monorail! Monorail!", character_id=8, episode="Marge vs. the Monorail"),
    Song(id=6, title="Happy Birthday, Mr. Burns", lyrics="Happy Birthday, Mr. Burns, Happy Birthday to you", character_id=5, episode="Burns' Heir"),
    Song(id=7, title="The Stonecutters' Song", lyrics="Who controls the British crown? Who keeps the metric system down?", character_id=7, episode="Homer the Great"),
    Song(id=8, title="Do the Bartman", lyrics="Do the Bartman, do the Bartman, everybody if you can do the Bartman", character_id=3, episode="Bart Simpson's Guide to Life"),
    Song(id=9, title="Happy Just the Way We Are", lyrics="We're happy just the way we are", character_id=1, episode="Bart Sells His Soul"),
    Song(id=10, title="We Put the Spring in Springfield", lyrics="We put the Spring in Springfield", character_id=8, episode="Bart After Dark")
]


@router.get("/songs/", response_model=list[Song], tags=["Песни 🎶"])
def get_songs():
    return songs_db


@router.get("/songs/{song_id}", response_model=Song, tags=["Песни 🎶"])
def get_song(song_id: int):
    song = next((s for s in songs_db if s.id == song_id), None)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song


@router.post("/songs/", response_model=Song, tags=["Песни 🎶"])
def create_song(song: Song):
    songs_db.append(song)
    return song


@router.patch("/songs/{song_id}", response_model=Song, tags=["Песни 🎶"])
def update_song(song_id: int, updated_song: Song):
    song = next((s for s in songs_db if s.id == song_id), None)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    song.title = updated_song.title
    song.lyrics = updated_song.lyrics
    song.character_id = updated_song.character_id
    song.episode = updated_song.episode
    return song


@router.delete("/songs/{song_id}", tags=["Песни 🎶"], status_code=status.HTTP_202_ACCEPTED, summary="Удалить песню")
def delete_song(song_id: int):
    song_index = next((index for index, s in enumerate(songs_db) if s.id == song_id), None)

    if song_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Song not found"
        )

    del songs_db[song_index]

    return {"message": "Song deleted"}
# @router.delete("/songs/{song_id}", tags=["Песни 🎶"])
# def delete_song(song_id: int):
#     try:
#         song_index = next((index for index, s in enumerate(songs_db) if s.id == song_id), None)
#
#         if song_index is None:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail="Song not found"
#             )
#
#         del songs_db[song_index]
#
#         return {"message": "Song deleted"}, status.HTTP_202_ACCEPTED
#
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail={
#                 "status": 500,
#                 "reason": str(e)
#             }
#         )
# @router.delete("/songs/{song_id}")
# def delete_song(song_id: int):
#     global songs_db
#     song = next((c for c in songs_db if c.id == songs_db), None)
#     if song is None:
#         raise HTTPException(status_code=404, detail="Song not found")
#
#     songs_db = [s for s in songs_db if s.id != song_id]
#     return {"message": "Song deleted", "status": 202}
#
#
# @router.exception_handler(HTTPException)
# def custom_http_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=500,
#         content={"status": exc.status_code, "reason": exc.detail},
#     )
