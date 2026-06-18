from urllib.parse import quote

from src.app import activities


def test_signup_adds_new_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"
    encoded_activity_name = quote(activity_name, safe="")

    # Act
    response = client.post(
        f"/activities/{encoded_activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}
    assert email in activities[activity_name]["participants"]


def test_signup_returns_400_for_duplicate_registration(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    encoded_activity_name = quote(activity_name, safe="")

    # Act
    response = client.post(
        f"/activities/{encoded_activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up"}


def test_signup_returns_404_for_missing_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"
    encoded_activity_name = quote(activity_name, safe="")

    # Act
    response = client.post(
        f"/activities/{encoded_activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}