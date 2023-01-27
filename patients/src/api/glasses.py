from flask import Blueprint, jsonify, request, abort
from ..models import Patient, Glasses_Rx, db

bp = Blueprint('glasses', __name__, url_prefix='/glasses')

@bp.route('', methods=['POST'])
def create():
    if 'patients_id' not in request.json or 'prescription' not in request.json:
        return abort(400)
    Patient.query.get_or_404(request.json['patients_id'])    
    g = Glasses_Rx(
        exp_date=request.json['exp_date'],
        valid=request.json['valid'],
        prescription=request.json['prescription'],
        pres_od=request.json['pres_od'],
        patients_id=request.json['patients_id']
    )
    db.session.add(g)
    db.session.commit()
    return jsonify(g.serialize())