from main import db
from datetime import datetime

class StockModel(db.Model):
    __tablename__='new_stock'
    id=db.Column(db.Integer,primary_key=True)
    stock=db.Column(db.Integer)
    created_at=db.Column(db.String(100),default=datetime.now())
    inv_id=db.Column(db.Integer,db.ForeignKey('inventories.id'))

    

    def add_stock(self):
        db.session.add(self)
        db.session.commit()