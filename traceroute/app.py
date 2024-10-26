from fastapi import FastAPI
from subprocess import run, PIPE, TimeoutExpired

from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/traceroute/")
async def traceroute(target: str):
    command = f"traceroute {target} | tail +2"
    try:
        result = run(command, shell=True, stdout=PIPE, stderr=PIPE, timeout=5)
        stdout = result.stdout.decode()
        stderr = result.stderr.decode()

        if stderr:
            return {"error": stderr}
        return {"output": stdout}
    
    except TimeoutExpired:
        return {"error": "Command timed out after 5 seconds"}

@app.get("/")
async def index():
    return FileResponse("index.html")
