from server.sql_base.archeology_db import base_worker
from server.sql_base.models import Firm


def create_firm(firm: Firm):
    return base_worker.execute(query="INSERT INTO firms(equipment_id, resource_id, title_firm, phone, city) VALUES (?, ?, ?, ?, ?)",
                               args=(firm.equipment_id, firm.resource_id, firm.title, firm.phone, firm.city))


def get_firm(firm_id: int):
    return base_worker.execute(query="SELECT id, equipment_id, resource_id, title_firm, phone, city FROM firms WHERE id=?",
                               args=(firm_id,))


def get_all_firms():
    return base_worker.execute(query="SELECT id, equipment_id, resource_id, title_firm, phone, city FROM firms",
                               many=True)


def upd_firm(equip_id: int, new_data: Firm):
    return base_worker.execute(query="UPDATE firms SET (equipment_id, resource_id, title_firm, phone, city)=(?, ?, ?, ?, ?) WHERE id=?",
                               args=(new_data.equipment_id, new_data.resource_id, new_data.title, new_data.phone, new_data.city, equip_id))


def del_firm(firm_id: int):
    return base_worker.execute(query="DELETE FROM firms WHERE id=?",
                               args=(firm_id,))