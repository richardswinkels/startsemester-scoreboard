from flask import Blueprint, render_template

score_controller = Blueprint('score_controller', __name__, template_folder='templates')

@score_controller.get('/scores', endpoint='index')
def index():
    return render_template('score_table.html')