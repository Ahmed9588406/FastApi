from fastapi import FastAPI

app = FastAPI()

# ("/") called here path like endpoint
@app.get("/") 
def hello():
    return {"data":{"name":"Ahmed","age":23}}

@app.get("/about")
def about():
    return {"data":"about page"}