from fastapi.testclient import TestClient

from src.app import app


def test_unregister_participant_removes_email_from_activity():
    client = TestClient(app)

    response = client.post("/activities/Chess Club/signup?email=test@example.com")
    assert response.status_code == 200

    response = client.delete("/activities/Chess Club/unregister?email=test@example.com")
    assert response.status_code == 200

    activity = client.get("/activities").json()["Chess Club"]
    assert "test@example.com" not in activity["participants"]
