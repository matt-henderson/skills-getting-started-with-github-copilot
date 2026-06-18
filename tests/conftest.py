import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


ORIGINAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory data before and after each test for isolation."""
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app)