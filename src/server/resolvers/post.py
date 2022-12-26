from server.sql_base.archeology_db import base_worker
from server.sql_base.models import Post


def create_post(post: Post):
    return base_worker.execute(query="INSERT INTO post(position) VALUES (?)",
                               args=(post.position,))


def get_post(post_id: int):
    return base_worker.execute(query="SELECT id, position FROM post WHERE id=?",
                               args=(post_id,))


def get_all_post():
    return base_worker.execute(query="SELECT id, position FROM post",
                               many=True)


def upd_post(post_id: int, new_data: Post):
    return base_worker.execute(query="UPDATE post SET position=? WHERE id=?",
                               args=(new_data.position, post_id))


def del_post(post_id: int):
    return base_worker.execute(query="DELETE FROM post WHERE id=?",
                               args=(post_id,))
