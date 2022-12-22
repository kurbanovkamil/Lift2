from fastapi import APIRouter
from server.sql_base.models import Equipment
from resolvers.equipments import create_equipment, get_equipment, get_all_equipment, upd_equipment, del_equipment

equipment_router = APIRouter(prefix="/equipments", tags=["Equipments"])


@equipment_router.get("/")
def start_page():
    return "Hello new user!"


@equipment_router.post("/create/")
def new_equipment(equipment: Equipment):
    return create_equipment(equipment)


@equipment_router.get("/get/{equipment_id}")
def get_equipment_rout(equipment_id: int):
    return get_equipment(equipment_id)


@equipment_router.get("/get/")
def get_all_equipment_rout():
    return get_all_equipment()


@equipment_router.put("/update/{equipment_id}")
def update_equipment(equipment_id: int, new_data: Equipment):
    return upd_equipment(equipment_id, new_data)


@equipment_router.delete("/delete/{equipment_id}")
def delete_equipment(equipment_id: int):
    return del_equipment(equipment_id)
