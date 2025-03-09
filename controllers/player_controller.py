from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for
import requests

player_controller = Blueprint('player_controller', __name__, template_folder='templates')

@player_controller.get('/player', endpoint='create')
def create():
    return render_template('player_form.html')
    
@player_controller.post('/player', endpoint='store')    
def store():
    API_URL = f"{current_app.config.get('MICROCONTROLLER_BASE_URL')}/api/player"

    player_name = request.form.get('name')

    if not (1 <= len(player_name) <= 300):
        flash('Player name must be between 1 and 300 characters.', 'error')
        return redirect(url_for('player_controller.create'))
        
    try:
        response = requests.post(API_URL, json={'name': player_name})

        if response.status_code == 400:
            flash('Cannot set player name while game is running.', 'error')
            return redirect(url_for('player_controller.create'))
        return redirect(url_for('score_controller.index'))

    except requests.exceptions.RequestException as e:
        flash('Error sending player name to game device', 'error')
        return redirect(url_for('player_controller.create'))