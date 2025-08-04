from fastapi import APIRouter, HTTPException
from fastapi import FastAPI
import subprocess
import json

router = APIRouter()

@router.post("/create-user/")
def new_user(repo_url):
    pass

@router.post("/new-repository/")
def new_repository():
    pass

@router.post("/new-message")
def new_message():
    pass

