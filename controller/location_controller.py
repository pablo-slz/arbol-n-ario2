from fastapi import APIRouter
from service.location_service import LocationService

router = APIRouter(prefix="/location", tags=["Location"])
service = LocationService()

@router.get("/states")
def get_states():
    return service.get_states()

@router.get("/code/{code}")
def get_by_code(code: str):
    return service.get_location_by_code(code)

@router.get("/state/{state_code}")
def get_by_state_code(state_code: str):
    return service.get_locations_by_state_code(state_code)

@router.get("/capitals")
def get_capitals():
    return service.get_capitals()


