from fastapi import APIRouter
from server.sql_base.models import Resource
from resolvers.resources import create_resource, get_resource, get_all_resources, upd_resource, del_resource

resource_router = APIRouter(prefix="/resources", tags=["Resources"])


@resource_router.get("/")
def start_page():
    return "Hello new user!"


@resource_router.post("/create/")
def new_resource(resource: Resource):
    return create_resource(resource)


@resource_router.get("/get/{resource_id}")
def get_resource_rout(resource_id: int):
    return get_resource(resource_id)


@resource_router.get("/get/")
def get_all_resources_rout():
    return get_all_resources()


@resource_router.put("/update/{resource_id}")
def update_resource(resource_id: int, new_data: Resource):
    return upd_resource(resource_id, new_data)


@resource_router.delete("/delete/{resource_id}")
def delete_resource(resource_id: int):
    return del_resource(resource_id)
