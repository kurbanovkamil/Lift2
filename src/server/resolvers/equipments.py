from server.sql_base.archeology_db import base_worker
from server.sql_base.models import Equipment


def create_equipment(equipment: Equipment):
    return base_worker.execute(query="INSERT INTO equipments(equipment) VALUES (?)",
                               args=(equipment.equipment,))


def get_equipment(equipment_id: int):
    return base_worker.execute(query="SELECT id, equipment FROM equipments WHERE id=?",
                               args=(equipment_id,))


def get_all_equipment():
    return base_worker.execute(query="SELECT id, equipment FROM equipments",
                               many=True)


def upd_equipment(equip_id: int, new_data: Equipment):
    return base_worker.execute(query="UPDATE equipments SET equipment=? WHERE id=?",
                               args=(new_data.equipment, equip_id))


def del_equipment(equip_id: int):
    return base_worker.execute(query="DELETE FROM equipments WHERE id=?",
                               args=(equip_id,))
