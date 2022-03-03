from fastapi import APIRouter
courses_api_router = APIRouter()


@courses_api_router.get("/service/getage")
async def read_item(year: int):
    if year != 0:
        if year < 0:
            return {"msg":"This value was under"}
        elif year > 2565:
            return {"msg":"This value was in the future"}
        else :
            year = 2565-year
            return {"age": year}
    return {"msg": "No value."}