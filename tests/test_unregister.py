from urllib.parse import quote

from src.app import activities


def test_unregister_removes_existing_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    encoded_activity_name = quote(activity_name, safe="")

    # Act
    response = client.delete(
        f"/activities/{encoded_activity_name}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]


def test_unregister_returns_404_for_missing_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"
    encoded_activity_name = quote(activity_name, safe="")

    # Act
    response = client.delete(
        f"/activities/{encoded_activity_name}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_returns_404_for_non_registered_student(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not.registered@mergington.edu"
    encoded_activity_name = quote(activity_name, safe="")

    # Act
    response = client.delete(
        f"/activities/{encoded_activity_name}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not registered for this activity"}