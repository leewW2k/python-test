from fastapi import APIRouter
import os
from dotenv import load_dotenv

load_dotenv()
ROUTE_PREFIX = "/syn-service"

router = APIRouter(prefix=ROUTE_PREFIX, tags=["syn-service"])


@router.get("/ping")
async def ping() -> str:
    return "syn-service-template:" + str(os.environ.get("SYN_SERVICE_VERSION"))
