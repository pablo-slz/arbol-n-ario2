from fastapi import APIRouter, HTTPException, status
from model.person import Person
from service import person_service
from service.person_service import tree
from model.filterperson import FilterPerson
from service.messages_service import MessageService

router = APIRouter(prefix="/person")
messages = MessageService()

@router.post("/filter/")
def get_by_filters_json(filters: FilterPerson):
    persons = person_service.get_persons_by_conditions(filters.code, filters.typedoc, filters.gender)
    if not persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=messages.get("filter.not_found")
        )
    return persons

@router.post("/")
def create(person: Person):
    try:
        if tree.is_empty() and person.parent_id is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=messages.get("tree.root_error")
            )

        result = person_service.create_person(person)
        return result

    except HTTPException as e:
        raise e

    except Exception as e:
        print(f"Error inesperado: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=messages.get("error.internal_server")
        )

@router.get("/")
def get_all():
    persons = person_service.list_persons()
    if not persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=messages.get("tree.empty")
        )
    return persons

@router.get("/location/{code}")
def get_by_location(code: str):
    persons = person_service.get_persons_by_location(code)
    if not persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=messages.get("location.not_found")
        )
    return persons

@router.get("/adults/daughters")
def get_parents():
    parents = person_service.get_parents_with_adult_daughters()
    if not parents:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=messages.get("parents.no_adult_daughters")
        )
    return parents

@router.put("/{person_id}")
def update(person_id: int, person: Person):
    updated = person_service.update_person(person_id, person)
    if updated:
        return {"message": messages.get("update.success")}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=messages.get("update.not_found")
        )

@router.delete("/{person_id}")
def delete(person_id: int):
    deleted = person_service.delete_person(person_id)
    if deleted:
        return {"message": messages.get("delete.success")}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=messages.get("delete.not_found")
        )




