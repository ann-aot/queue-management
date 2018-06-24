'''Copyright 2018 Province of British Columbia

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''

from flask_restplus import fields
from qsystem import api, db
from .base import Base 
from datetime import datetime

class Citizen(Base):

    citizen_id          = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    office_id           = db.Column(db.Integer, db.ForeignKey('office.office_id'), nullable=False)
    ticket_number       = db.Column(db.String(50), nullable=True)
    citizen_name        = db.Column(db.String(150), nullable=True)
    citizen_comments    = db.Column(db.String(1000), nullable=True)
    qt_xn_citizen_ind   = db.Column(db.Integer, default=0, nullable=False)
    cs_id               = db.Column(db.BigInteger, db.ForeignKey('citizenstate.cs_id'), nullable=False)
    start_time          = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    service_reqs        = db.relationship('ServiceReq', backref='citizen', lazy="joined")
    cs                  = db.relationship('CitizenState', backref=db.backref("state_citizens", lazy="joined"))
    #office              = db.relationship('Office', backref=db.backref("citizens", lazy=False))


    def __repr__(self):
        return '<Citizen Name:(name={self.citizen_name!r})>'.format(self=self)

    def __init__(self, **kwargs):
        super(Citizen, self).__init__(**kwargs)
        self.ticket_number = 'A1'

    #def getActiveServiceRequest():
