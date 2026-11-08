from fastapi import APIRouter, Request

router = APIRouter(tags=["meta"])


@router.get("/version")
async def get_version(request: Request) -> dict[str,str]:
    """Returns the current version of the API."""
    return {"version": request.app.version}

