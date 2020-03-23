import os

import pytest
from madness import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })

    with app.app_context():
        pass
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
