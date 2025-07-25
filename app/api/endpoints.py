from fastapi import APIRouter, HTTPException
from fastapi import FastAPI
import subprocess
import json

router = APIRouter()

#@router.post("/update")
def new_update(repo_url):
    try:

        result = subprocess.run(
            ["docker", "run", "--rm", "sandbox-image", repo_url],
            capture_output=True,
            text=True,
            timeout=60
        )
        print("passei aqui")
        if result.returncode != 0:

            return {"erro": "Falha na sandbox", "log": result.stderr}

        # Aqui assumimos que a sandbox imprimiu um JSON
        return {"saida": result.stdout.strip()}

    except Exception as e:
        return {"erro": str(e)}

@router.post("/new-repository/")
def new_repository():
    pass

