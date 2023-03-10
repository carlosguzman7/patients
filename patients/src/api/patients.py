from flask import Blueprint, jsonify, abort, request
from ..models import Patient, db

bp = Blueprint('patients', __name__, url_prefix='/patients')

@bp.route('', methods=['GET'])
def index():
    patients = Patient.query.all()
    result = []
    for p in patients:
        result.append(p.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Patient.query.get_or_404(id)
    return jsonify(p.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json and 'date_of_birth' not in request.json and 'phone_number' not in request.json:
        return abort(400)
    p = Patient(
        name=request.json['name'],
        date_of_birth=request.json['date_of_birth'],
        phone_number=request.json['phone_number'],
        email=request.json['email']
    )
    db.session.add(p)
    db.session.commit()
    return jsonify(p.serialize())