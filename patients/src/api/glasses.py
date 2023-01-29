from flask import Blueprint, jsonify, request, abort
from ..models import Patient, Glasses_Rx, db

bp = Blueprint('glasses', __name__, url_prefix='/glasses')

@bp.route('', methods=['POST'])
def create():
    if 'patients_id' not in request.json or 'od_rx' not in request.json or 'os_rx' not in request.json:
        return abort(400)
    Patient.query.get_or_404(request.json['patients_id'])    
    g = Glasses_Rx(
        exp_date=request.json['exp_date'],
        valid=request.json['valid'],
        od_rx=request.json['od_rx'],
        os_rx=request.json['os_rx'],
        pres_doc=request.json['pres_doc'],
        patients_id=request.json['patients_id']
    )
    db.session.add(g)
    db.session.commit()
    return jsonify(g.serialize())

@bp.route('', methods=['GET'])
def index():
    glasses = Glasses_Rx.query.all()
    result = []
    for g in glasses:
        result.append(g.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    g = Glasses_Rx.query.get_or_404(id)
    return jsonify(g.serialize())