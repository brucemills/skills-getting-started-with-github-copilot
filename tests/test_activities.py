def test_get_activities_returns_success_and_payload(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()) > 0


def test_get_activities_contains_expected_activity_key(client):
    # Arrange
    endpoint = "/activities"
    expected_activity = "Chess Club"

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity in payload


def test_get_activities_activity_has_required_fields(client):
    # Arrange
    endpoint = "/activities"
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    for activity in payload.values():
        assert required_fields.issubset(activity.keys())
