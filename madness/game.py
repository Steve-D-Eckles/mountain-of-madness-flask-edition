from flask import (
    Blueprint, flash, g, render_template, redirect, request, session, url_for
)

from madness.db import get_db
from madness import scenes

bp = Blueprint('game', __name__, url_prefix='/game')

def get_scenes(action):
    next_scene = None
    action_dict = {
        'mountain_exterior': [('approach', 'ex_approach'), ('wait', 'ex_wait'), ('search', 'ex_search')],
        'first_fork': [('left', 'first_fork_left'), ('right', 'first_fork_right')],
        'ex_approach': [('left', 'first_fork_left'), ('right', 'first_fork_right')],
        'ex_wait': [('left', 'first_fork_left'), ('right', 'first_fork_right')],
        'ex_search': [('left', 'first_fork_left'), ('right', 'first_fork_right')],
        'first_fork_left': [('wooden door', 'end'), ('iron door', 'end'), ('footlockers', 'footlockers'), ('bugbear', 'end')],
        'first_fork_right': [('ram', 'door_ram'), ('back', 'first_fork_left')],
        'footlockers': [('wooden door', 'end'), ('iron door', 'end'), ('bugbear', 'end')],
        'door_ram': [('back', 'first_fork_left'),('again', 'door_ram')]
    }

    valid_actions = action_dict.get(session.get('scene'))

    if valid_actions:
        for pair in valid_actions:
            if action == pair[0]:
                next_scene = pair[1]

    return next_scene

def get_scene_text(scene):
    scene_list = {
        'mountain_exterior': scenes.MountainExterior(),
        'ex_search': scenes.ExteriorSearch(),
        'ex_approach': scenes.ExteriorApproach(),
        'ex_wait': scenes.ExteriorWait(),
        'first_fork': scenes.FirstFork(),
        'first_fork_left': scenes.FirstForkLeft(),
        'first_fork_right': scenes.FirstForkRight(),
        'door_ram': scenes.DoorRam(),
        'pit': scenes.Pit(),
        # 'footlockers': scenes.Footlockers()
    }

    return scene_list.get(scene).enter()


@bp.route('/', methods=("GET", 'POST'))
def play():
    if not session.get('scene'):
        session['scene'] = 'mountain_exterior'

    if request.method == 'POST':
        action = request.form['action'].lower()
        error = None
        next_scene = get_scenes(action)

        if not action:
            error = 'Specify an action'
        elif not next_scene:
            error = 'Not a valid action'

        if error is None:
            session['scene'] = next_scene
        else:
            flash(error)

    text = get_scene_text(session['scene'])
    dead = text.pop(-1)

    return render_template('game/play.html', text=text, dead=dead)

@bp.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('game.play'))
