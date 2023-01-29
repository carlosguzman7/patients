from flask import Blueprint, jsonify, request, abort
from ..models import Patient, Contacts_Rx, db

bp = Blueprint('contacts', __name__, url_prefix='/contacts')

@bp.route('', methods=['POST'])
def create():
    if 'patients_id' not in request.json or 'lens_brand' not in request.json:
        return abort(400)
    Patient.query.get_or_404(request.json['patients_id'])
    c = Contacts_Rx(
        exp_date=request.json['exp_date'],
        valid=request.json['valid'],
        lens_brand=request.json['lens_brand'],
        od_rx=request.json['od_rx'],
        os_rx=request.json['os_rx'],
        pres_doc=request.json['pres_doc'],
        patient_id=request.json['patients_id']
    )
    db.session.add(c)
    db.session.commit()
    return jsonify(c.serialize())

@bp.route('', methods=['GET'])
def index():
    contacts = Contacts_Rx.query.all()
    result = []
    for c in contacts:
        result.append(c.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    c = Contacts_Rx.query.get_or_404(id)
    return jsonify(c.serialize())