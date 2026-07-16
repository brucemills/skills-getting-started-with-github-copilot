def test_unregister_removes_participant_and_returns_success_message(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(endpoint, params={"email": email})
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Removed {email} from {activity_name}"}
    assert email not in participants


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_non_participant_returns_404(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not.enrolled@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not signed up for this activity"}
