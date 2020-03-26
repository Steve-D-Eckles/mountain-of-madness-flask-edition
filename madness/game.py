from flask import (
    Blueprint, flash, g, render_template, request, session, url_for
)

from madness.db import get_db

bp = Blueprint('game', __name__, url_prefix='/game')

def get_scenes(action):
    next_scene = None
    action_dict = {
        'mountain_exterior': [('approach', 'ex_approach'), ('wait', 'ex_wait'), ('search', 'ex_search')],
        'first_fork': [('left', 'first_fork_left'), ('right', 'first_fork_right')],
        'first_fork_left': [('wooden door', 'end'), ('iron door', 'end'), ('footlockers', 'footlockers'), ('bugbear', 'end')],
        'first_fork_right': [('ram', 'door_ram'), ('back', 'first_fork_left')],
        'footlockers': [('wooden door', 'end'), ('iron door', 'end'), ('bugbear', 'end')],
        'door_ram': [('back', 'first_fork_left')]
    }

    valid_actions = action_dict.get(session.get('scene'))

    if valid_actions:
        for pair in valid_actions:
            if action == pair[0]:
                next_scene = pair[1]

    return next_scene


@bp.route('/play', methods=("GET", 'POST'))
def play():
    if not session.get('scene'):
        session['scene'] = 'mountain_exterior'

    if request.method == 'POST':
        action = request.form['action']
        error = None
        next_scene = get_scenes(action)

        if not action:
            error = 'Specify an action'
        elif not next_scene:
            error = 'Not a valid action'

        if error is None:
            # Move to the next scene
            pass

        flash(error)
