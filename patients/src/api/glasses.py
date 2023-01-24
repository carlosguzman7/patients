from flask import Blueprint, jsonify, request, abort
from ..models import Patient, Glasses_Rx, db

bp = Blueprint('glasses', __name__, url_prefix='/glasses')

@bp.route('', methods=['POST'])
def create():
    if 'patient_id' not in request.json or 'prescription' not in request.json:
        return abort(400)
    Patient.query.get_or_404(request.json['patient_id'])
    g = Glasses_Rx(
        valid=True,
        prescription= 'R -3.00 /L -4.50',
        pres_od='Von Dutch, OD',
        patient_id=1
    )
    db.session.add(g)
    db.session.commit()
    return jsonify(g.serialize())