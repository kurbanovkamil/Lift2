from fastapi import APIRouter
from server.sql_base.models import Staff
from resolvers.staff import get_staff, get_all_staff, create_staff, upd_staff, del_staff

staff_router = APIRouter(prefix="/staff", tags=["Staff"])


@staff_router.get("/")
def start_page():
    return "Hello new user!"


@staff_router.post("/create/")
def new_staff(staff: Staff):
    return create_staff(staff)


@staff_router.get("/get/{staff_id}")
def get_staff_rout(staff_id: int):
    return get_staff(staff_id)


@staff_router.get("/get/")
def get_all_staff_rout():
    return get_all_staff()


@staff_router.put("/update/{staff_id}")
def update_staff(staff_id: int, new_data: Staff):
    return upd_staff(staff_id, new_data)


@staff_router.delete("/delete/{staff_id}")
def delete_staff(staff_id: int):
    return del_staff(staff_id)
