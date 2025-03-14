import pytest
from app import get_users, get_user_names, get_user_count

# Mocking the requests.get method to avoid making real API calls
from unittest.mock import patch

# Test to check if the function fetches users correctly
@patch('app.requests.get')
def test_get_users(mock_get):
    # Sample response for the mock
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"id": 1, "name": "John Doe"}]

    result = get_users()
    assert isinstance(result, list)  # It should return a list
    assert len(result) == 1  # It should contain 1 user
    assert result[0]['name'] == "John Doe"  # User name should match

# Test for getting user names
@patch('app.requests.get')
def test_get_user_names(mock_get):
    # Sample response for the mock
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"}
    ]
    
    result = get_user_names()
    assert len(result) == 2  # Two users should be fetched
    assert result[0] == "John Doe"  # First user should be John Doe
    assert result[1] == "Jane Doe"  # Second user should be Jane Doe

# Test for getting user count
@patch('app.requests.get')
def test_get_user_count(mock_get):
    # Sample response for the mock
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"}
    ]

    result = get_user_count()
    assert result == 2  # There should be two users

