from models.db import db
from models.score import Score
from flask import jsonify, Blueprint, request

api_score_controller = Blueprint('api_score_controller', __name__, template_folder='templates', url_prefix='/api/')

@api_score_controller.get('/scores', endpoint='index')
def index():
    scores = db.session.execute(db.select(Score).order_by(Score.score.desc())).scalars()
    scores_data = [score.as_dict() for score in scores]
    return jsonify(scores_data), 200 

@api_score_controller.post('/scores', endpoint='store')
def store():
    data = request.get_json()

    player_name = data.get('player_name')
    score = data.get('score')
    bullets_used = data.get('bullets_used')

    if not isinstance(player_name, str) or not isinstance(score, int) or not isinstance(bullets_used, int):
        return jsonify({'error': 'Invalid input'}), 400

    score = Score(
        player_name=player_name,
        score=score,
        bullets_used=bullets_used
    )

    db.session.add(score)
    db.session.commit()

    return jsonify({'message': 'success'}), 200