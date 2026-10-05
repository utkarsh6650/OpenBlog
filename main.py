from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name= "static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Utkarsh Maddheshiya",
        "title": "Utkarsh is Awesome",
        "content": "Utkarsh is an awesome developer and a great person.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Utkarsh Maddheshiya",
        "title": "Utkarsh loves Python",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

@app.get("/", include_in_schema=False,name = "home")
@app.get("/posts",include_in_schema=False,name = "posts")
def home(request: Request):
    return templates.TemplateResponse(request,
                                       "home.html",
                                       {"posts" : posts,"title" : "Home"},)

@app.get("/api/posts")
def get_posts():
    return posts