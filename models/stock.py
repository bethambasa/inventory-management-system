from main import db
from datetime import datetime

class StockModel(db.Model):
    _tablename_='new_stock'
    id=db.Column(db.Integer,primary_key=True)
    invid=db.Column(db.Integer,db.Foreign key)
    stock=db.Column(db,Integer)
    created_at=db.Column(db.Datetime,default=datetime.utcnow))
    

    def add_stock(self):
        db.session.add(self)
        db.session.commit()