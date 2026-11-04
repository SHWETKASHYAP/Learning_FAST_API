from fastapi import APIRouter  #--A router is a mini-app that groups related endpoints together(e.g. :- health , users, auth)

router = APIRouter(tags=["Health"]) #--Creates the group ,tags are used to group endpoints in the documentation

@router.get("/health")                             #-- registers a GET endpoint at the path /health
async def health_check() -> dict[str, str]:        #-- asyncronous function that returns a dictionary with string keys and string values
    """Liveness probe: answers 'is the process alive?'"""
    return {"status": "ok"}        #-- FastAPI converts the dict to JSON, sets Content-Type: application/json, and status 200.