import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    date_of_birth = db.Column(db.DateTime, default=datetime.date, unique=False, nullable=False)
    phone_number = db.Column(db.Integer, unique=False, nullable=False)
    email = db.Column(db.String(40), unique=False, nullable=True)
    current_clrx = db.relationship('Contacts_Rx', backref='patient')
    current_srx = db.relationship('Glasses_Rx', backref='patient')

    def __init__(self, name: str, date_of_birth: datetime, phone_number: int, email: str): #cl_rx: int, #s_rx: int
        self.name = name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.email = email
        
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_of_birth': self.date_of_birth,
            'phone_number': self.phone_number,
            'email': self.email
        }


cls_pres = db.Table('contacts_prescribed',
    db.Column('contacts_rx_id', db.Integer, db.ForeignKey('contacts.id'), primary_key=True),
    db.Column('patients_id', db.Integer, db.ForeignKey('patients.id'), primary_key=True)
)

specs_pres = db.Table('glasses_prescribed',
    db.Column('glasses_rx_id', db.Integer, db.ForeignKey('glasses.id'), primary_key=True),
    db.Column('patients_id', db.Integer, db.ForeignKey('patients.id'), primary_key=True)
)
    

class Glasses_Rx(db.Model):
    __tablename__ = 'glasses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exp_date = db.Column(db.DateTime, default=datetime.date, nullable=False)
    valid = db.Column(db.Boolean, nullable=False)
    od_rx = db.Column(db.String, nullable=True)
    os_rx = db.Column(db.String, nullable=True)
    pres_doc = db.Column(db.String, nullable=False)
    patients_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)

    def __init__(self, exp_date: datetime, valid: bool, od_rx: str, os_rx: str, pres_doc: str, patients_id: int):
        self.exp_date = exp_date
        self.valid = valid
        self.od_rx = od_rx
        self.os_rx = os_rx
        self.pres_doc = pres_doc
        self.patients_id = patients_id

    def serialize(self):
        return {
            'id': self.id,
            'exp_date': self.exp_date,
            'valid': self.valid,
            'od_rx': self.od_rx,
            'os_rx': self.os_rx,
            'pres_doc': self.pres_doc,
            'patients_id': self.patients_id
        }


class Contacts_Rx(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exp_date = db.Column(db.DateTime, default=datetime.date, nullable=False)
    valid = db.Column(db.Boolean, nullable=False)
    lens_brand = db.Column(db.String, nullable=False)
    od_rx = db.Column(db.String, nullable=False)
    os_rx = db.Column(db.String, nullable=False)
    pres_doc = db.Column(db.String, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)

    def __init__(self, exp_date: datetime, valid: bool, lens_brand: str, od_rx: str, os_rx: str, pres_doc: str, patient_id: str):
        self.exp_date = exp_date
        self.valid = valid
        self.lens_brand = lens_brand
        self.od_rx = od_rx
        self.os_rx = os_rx
        self.pres_doc = pres_doc
        self.patient_id = patient_id

    def serialize(self):
        return {
            'id': self.id,
            'exp_date': self.exp_date,
            'valid': self.valid,
            'lens_brand': self.lens_brand,
            'od_rx': self.od_rx,
            'os_rx': self.os_rx,
            'pres_doc': self.pres_doc,
            'patient_id': self.patient_id
        }

    


