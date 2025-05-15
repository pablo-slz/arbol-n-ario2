from fastapi import APIRouter
from service.typedoc_service import TypeDocService

router = APIRouter(prefix="/typedoc", tags=["TypeDoc"])
service = TypeDocService()

@router.get("/")
def get_all():
    return service.get_all()
