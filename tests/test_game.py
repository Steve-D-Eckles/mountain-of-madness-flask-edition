from madness import game
from flask import session
from madness import scenes

import pytest

def test_get_scenes(app):
    with app.test_request_context('/'):
        session['scene'] = 'mountain_exterior'
        assert game.get_scenes('wait') == 'ex_wait'

@pytest.mark.parametrize(('scene', 'match'), (
    ('mountain_exterior', '-APPROACH the cave'),
    ('first_fork_left', "I guess you're just dead then"),
    ('pit', True)
))
def test_get_scene_text(app, scene, match):
    assert match in game.get_scene_text(scene)

def test_play(app, client):
    assert client.get('/game/').status_code == 200
    response = client.post(
        '/game/', data={'action': 'approach'}
    )
    assert b'GOBLIN GUARDS' in response.data

def test_reset(client):
    response = client.get('/game/reset')
    assert 'http://localhost/game/' == response.headers['Location']
