from fastapi import APIRouter


router = APIRouter()


@router.get("/hello_axitwo")
def hello_axitwo() -> dict[str, str]:
    return {"msg": "Hello Axitwo !"}
