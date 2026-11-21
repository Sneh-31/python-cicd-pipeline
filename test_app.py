from app import greet, get_app_status

def test_greet():
    assert greet("Snehlata") == "Hello, Snehlata! Welcome to CI/CD."
def test_app_status():
    assert get_app_status() == "Application is running successfully!"