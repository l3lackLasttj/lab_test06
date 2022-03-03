from asyncio.windows_events import NULL
from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../lab_test06')        
from main import app

client = TestClient(app)


def test_yeat_data_api():
    input = "2543"
    output = 22
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_under_yeat_data_api():
    input = "-1"
    output = "Data Underflow"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"msg":output}

def test_over_yeat_data_api():
    input = "2567"
    output = "that is the future"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"msg":output}

def test_null_yeat_data_api():
    input = "0"
    output = "No information found."
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"msg":output}

