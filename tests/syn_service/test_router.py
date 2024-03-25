import os

from fastapi.testclient import TestClient
from src.syn_service.router import router, ROUTE_PREFIX
from dotenv import load_dotenv

load_dotenv()

client = TestClient(router)
client.base_url = str(client.base_url) + ROUTE_PREFIX


def test_ping():
    print(client.base_url)
    response = client.get("ping")
    assert response.status_code == 200
    assert os.environ.get("SYN_SERVICE_VERSION") in response.text
