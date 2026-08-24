from backend.main import app


def test_application_exists():
    assert app is not None


def test_application_title():
    assert app.title == "AlgoVault API"