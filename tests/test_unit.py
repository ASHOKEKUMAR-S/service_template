from app.models import Device
from sqlalchemy.orm import Session
from unittest.mock import MagicMock

def test_get_distinct_applications():
    mock_session = MagicMock(spec=Session)
    mock_session.query().distinct().all.return_value = [Device(application="app1"), Device(application="app2")]
    result = [r.application for r in mock_session.query().distinct().all()]
    assert result == ["app1", "app2"]
