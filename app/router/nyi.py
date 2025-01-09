from fastapi import APIRouter

router = APIRouter(
    prefix="/nyi",
    tags=["nyi"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", description="not yet implemented")
def nyi():
    return {"output": "nyi"}
