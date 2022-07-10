
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
import marshmallow as ma


from db import *
# app = Flask(__name__)

# database_host = "127.0.0.1:5432"
# database_name = "clinic"
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# ma = Marshmallow(app)


class Visits(db.Model):
    __tablename__ = "visits"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    doctor_id = db.Column(UUID(as_uuid=True), db.ForeignKey('doctors.id', ondelete="CASCADE"), nullable=False)
    patient_id = db.Column(UUID(as_uuid=True), db.ForeignKey('patients.id', ondelete="CASCADE"), nullable=False)
    date = db.Column(db.DateTime(), nullable = False)
    status = db.Column(db.String(), nullable = False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)
    
    bill = db.relationship('Bills', cascade="all,delete", backref = 'visits', lazy=True)
    prescription = db.relationship('Prescriptions', cascade="all,delete", backref = 'visits', lazy=True)
    visit_procedure = db.relationship('VisitProcedures', cascade="all,delete", backref = 'visits', lazy=True)
    doctor = db.relationship('Doctors', cascade="all,delete", backref = 'visits', lazy=True)
    
    

    def __init__(self, doctor_id, patient_id, date, status, created_at, updated_at):
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.date = date
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        

class VisitsSchema(ma.Schema):
    class Meta:
        fields = ['id','first_name', 'last-name', 'sex', 'phone', 'dob', 'active']

visit_schema = VisitsSchema()
visits_schema = VisitsSchema(many=True)