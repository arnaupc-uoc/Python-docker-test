from app import create_app
import os


def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['SECRET_KEY'] = 'uYl0f/J0jDbWkYxFe3foWLtYIRCcKlzCFziePQK0lDlQcjDTLyJZCa9Yz+sJZGrp'
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    os.environ['MAIL_DEFAULT_SENDER'] = '"MyApp" <noreply@example.com>'
    os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:8889/python_test'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Demo Site" in response.data