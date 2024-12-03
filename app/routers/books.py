from fastapi import APIRouter
router=APIRouter(prefix="/book",tags=["Book Management"])
@router.get("/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}