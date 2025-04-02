from fastapi import FastAPI, HTTPException
from supabase import create_client
import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from.env file


app = FastAPI()

# Connect to Supabase
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)


# Simple Post Model
class Post(BaseModel):
    title: str
    content: str
    author: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Simple Blog API!"}

@app.post("/posts")
def create_post(post: Post):
    # Insert into Supabase
    data = supabase.table("posts").insert(post.dict()).execute()
    return data.data[0]

@app.get("/posts")
def get_posts():
    # Get all posts from Supabase
    data = supabase.table("posts").select("*").execute()
    return data.data

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    # Get a single post by ID from Supabase
    data = supabase.table("posts").select("*").eq("id", post_id).execute()
    
    if not data.data:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return data.data[0]