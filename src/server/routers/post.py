from fastapi import APIRouter
from server.sql_base.models import Post
from resolvers.post import create_post, get_post, get_all_post, upd_post, del_post

post_router = APIRouter(prefix="/posts", tags=["Posts"])


@post_router.get("/")
def start_page():
    return "Hello new user!"


@post_router.post("/create/")
def new_post(post: Post):
    return create_post(post)


@post_router.get("/get/{post_id}")
def get_post_rout(post_id: int):
    return get_post(post_id)


@post_router.get("/get/")
def get_all_posts_rout():
    return get_all_post()


@post_router.put("/update/{post_id}")
def update_post(post_id: int, new_data: Post):
    return upd_post(post_id, new_data)


@post_router.delete("/delete/{post_id}")
def delete_post(post_id: int):
    return del_post(post_id)
