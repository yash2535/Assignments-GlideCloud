from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_create_student():
    response = client.post(
        "/students/",
        json={
            "prn": 104,
            "name": "Test Student",
            "age": 22,
            "contact": 9876543210
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Student created successfully" 

def test_get_all_students():
    response = client.get("/students/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_student_by_prn():
    response = client.get("/students/101")

    assert response.status_code == 200
    assert response.json()["prn"] == 101


def test_update_student():
    response = client.put(
        "/students/102",
        json={
            "prn": 102,
            "name": "Updated Student",
            "age": 23,
            "contact": 9999999999
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Student updated successfully"

def test_delete_student():
    response = client.delete("/students/102")

    assert response.status_code == 200
    assert response.json()["message"] == "Student deleted successfully"
