from server.sql_base.archeology_db import base_worker
from server.sql_base.models import Staff


def create_staff(staff: Staff):
    return base_worker.execute(query="INSERT INTO staff(firm_id, post_id, name, surname, patronymic, date_of_birth) VALUES (?, ?, ?, ?, ?, ?)",
                               args=(staff.firm_id, staff.post_id, staff.name, staff.surname, staff.patronymic, staff.date_of_birth))


def get_staff(staff_id: int):
    return base_worker.execute(query="SELECT id, firm_id, post_id, name, surname, patronymic, date_of_birth FROM staff WHERE id=?",
                               args=(staff_id,))


def get_all_staff():
    return base_worker.execute(query="SELECT id, firm_id, post_id, name, surname, patronymic, date_of_birth FROM staff",
                               many=True)


def upd_staff(staff_id: int, new_data: Staff):
    return base_worker.execute(query="UPDATE staff SET (firm_id, post_id, name, surname, patronymic, date_of_birth)=(?, ?, ?, ?, ?, ?) WHERE id=?",
                               args=(new_data.firm_id, new_data.post_id, new_data.name, new_data.surname, new_data.patronymic, new_data.date_of_birth, staff_id))


def del_staff(staff_id: int):
    return base_worker.execute(query="DELETE FROM staff WHERE id=?",
                               args=(staff_id,))
