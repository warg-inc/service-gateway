from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from .api_v1_router import create_api_v1_router



def create_root_router():
    router = APIRouter()
    
    @router.get("/", tags=["General"])
    async def rederict_to_docs() -> RedirectResponse:
        return RedirectResponse(url="docs/")
    
    router.include_router(create_api_v1_router())

    return router
