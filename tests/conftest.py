import pytest
from flaskdev.app import app


@pytest.fixture(scope="session")
def app_test():
    app_test = app
    app_test.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app_test

    # clean up / reset resources here


@pytest.fixture()
def client(app_test):
    return app_test.test_client()


@pytest.fixture()
def runner(app_test):
    return app_test.test_cli_runner()