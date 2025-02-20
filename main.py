from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()

# ("/") called here path like endpoint

class Blog(BaseModel):
    title: str
    body: str
    published : Optional[bool]

@app.get("/") 
def hello():
    return {"data":{"name":"Ahmed","age":23}}


@app.get("/blog")
def blog(limit = 10,published = True,sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from db"}
    else:
        return {"data": f"{limit} from db"}
        

@app.get("/blog/unpublished")
def unpublished():
     return {"data":"unpublished blogs"}

@app.get("/blog/{id}")
def blog(id:int):
    return {"data":id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data":{"1","2"}}


@app.post("/blog")
def create_blog(blog:Blog):
    return {"data": f"blog is created {blog.title}"}



