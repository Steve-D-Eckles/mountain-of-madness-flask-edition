from madness import game
from flask import session

def test_get_scenes(app):
    with app.app_context():
        session['scene'] = 'mountain_exterior'
        assert game.get_scenes(wait) == 'ex_wait'
