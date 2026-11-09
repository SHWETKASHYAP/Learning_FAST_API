from fastapi import APIRouter, Request

router = APIRouter(tags=["meta"])


@router.get("/version")
async def get_version(request: Request) -> dict[str,str]:
    """Returns the current version of the API."""
    return {"version": request.app.version}

"""Your function declares a parameter(request) with the type hint Request:
The name request is your choice. You could write req: Request and it works the same. The type hint is what matters, not the name.
"""