from server.sql_base.archeology_db import base_worker
from server.sql_base.models import Resource


def create_resource(resource: Resource):
    return base_worker.execute(query="INSERT INTO resources(resource) VALUES (?)",
                               args=(resource.resource,))


def get_resource(resource_id: int):
    return base_worker.execute(query="SELECT id, resource FROM resources WHERE id=?",
                               args=(resource_id,))


def get_all_resources():
    return base_worker.execute(query="SELECT id, resource FROM resources",
                               many=True)


def upd_resource(resource_id: int, new_data: Resource):
    return base_worker.execute(query="UPDATE resources SET resource=? WHERE id=?",
                               args=(new_data.resource, resource_id))


def del_resource(resource_id: int):
    return base_worker.execute(query="DELETE FROM resources WHERE id=?",
                               args=(resource_id,))
