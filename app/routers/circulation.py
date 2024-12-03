from fastapi import APIRouter
router=APIRouter(prefix="/user",tags=["Circulation"])
@router.get("/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}