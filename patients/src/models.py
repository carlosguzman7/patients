import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    date_of_birth = db.Column(db.DateTime, default=datetime.datetime, unique=False, nullable=False)
    phone_number = db.Column(db.Integer, unique=False, nullable=False)
    email = db.Column(db.String(40), unique=False, nullable=True)
    #current_clrx = db.relationship('CL_Rx', backref='patient')
    #current_srx = db.relationship('S_Rx', backref='patient')

    def __init__(self, name: str, date_of_birth: datetime, phone_number: int, email: str): #cl_rx: int, #s_rx: int
        self.name = name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.email = email
        #self.cl_rx = cl_rx
        #self.s_rx = s_rx
        
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_of_birth': self.date_of_birth,
            'phone_number': self.phone_number,
            'email': self.email
            #'current_clrx': self.current_clrx,
            #'current_srx': self.current_srx
        }
    

class Glasses_Rx(db.Model):
    __tablename__ = 'glasses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exp_date = db.Column(db.DateTime, default=datetime.datetime, nullable=False)
    valid = db.Column(db.Boolean, nullable=False)
    prescription = db.Column(db.Integer, nullable=False)
    pres_od = db.Column(db.String, nullable=False)
    #patient_id = db.relationship('Pt_ID', backref='glasses_rx')

    def __init__(self, exp_date: datetime, valid: bool, prescription: str, pres_od: str, patient_id: int):
        self.exp_date = exp_date
        self.valid = valid
        self.prescription = prescription
        self.pres_od = pres_od
        self.patient_id = patient_id

    def serialize(self):
        return {
            'id': self.id,
            'exp_date': self.exp_date,
            'valid': self.valid,
            'prescription': self.prescription,
            'pres_od': self.pres_od,
            'patient_id': self.patient_id
        }


class Contacts_Rx(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exp_date = db.Column(db.DateTime, default=datetime.datetime, nullable=False)
    valid = db.Column(db.Boolean, nullable=False)
    lens_brand = db.Column(db.String, nullable=False)
    prescription = db.Column(db.Integer, nullable=False)
    pres_od = db.Column(db.String, nullable=False)
    #patient_id = db.relationship('Pt_ID', backref='contacts_rx')

    def __init__(self, exp_date: datetime, valid: bool, lens_brand: str, prescription: str, pres_od: str, patient_id: str):
        self.exp_date = exp_date
        self.valid = valid
        self.lens_brand = lens_brand
        self.prescription = prescription
        self.pres_od = pres_od
        self.patient_id = patient_id

    def serialize(self):
        return {
            'id': self.id,
            'exp_date': self.exp_date,
            'valid': self.valid,
            'lens_brand': self.lens_brand,
            'prescription': self.prescription,
            'pres_od': self.pres_od,
            'patient_id': self.patient_id
        }

    
cls_pres = db.Table('contacts_prescribed',
    db.Column('contacts_rx_id', db.Integer, db.ForeignKey('contacts.id'), primary_key=True),
    db.Column('patients_id', db.Integer, db.ForeignKey('patients.id'), primary_key=True)
)

specs_pres = db.Table('glasses_prescribed',
    db.Column('glasses_rx_id', db.Integer, db.ForeignKey('glasses.id'), primary_key=True),
    db.Column('patients_id', db.Integer, db.ForeignKey('patients.id'), primary_key=True)
)
