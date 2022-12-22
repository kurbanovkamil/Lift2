from fastapi import APIRouter
from server.sql_base.models import Firm
from resolvers.firms import create_firm, get_firm, get_all_firms, upd_firm, del_firm

firm_router = APIRouter(prefix="/firms", tags=["Firms"])


@firm_router.get("/")
def start_page():
    return "Hello new user!"


@firm_router.post("/create/")
def new_firm(firm: Firm):
    return create_firm(firm)


@firm_router.get("/get/{firm_id}")
def get_firm_rout(firm_id: int):
    return get_firm(firm_id)


@firm_router.get("/get/")
def get_all_firms_rout():
    return get_all_firms()


@firm_router.put("/update/{firm_id}")
def update_firm(firm_id: int, new_data: Firm):
    return upd_firm(firm_id, new_data)


@firm_router.delete("/delete/{firm_id}")
def delete_firm(firm_id: int):
    return del_firm(firm_id)
