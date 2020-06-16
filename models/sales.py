from main import db
from datetime import datetime

class SalesModel(db.Model):
   __tablename__='sales'
   id=db.Column(db.Integer,primary_key=True)
   quantity=db.Column(db.Integer)
   created_at=db.Column(db.String(100),default=datetime.now()) 
   inv_id=db.Column(db.Integer,db.ForeignKey('inventories.id'))


   def add_sales(self):
      db.session.add(self)
      db.session.commit()
        
   @classmethod
   def get_sales_by_id(cls,inv_id):
      return cls.query.filter_by(inv_id=inv_id).all()
   
   #n the child model:
      #- we store the FK and describe it (tablename and which column)

      # We also need to declare a relationship between the models.
      #- To do that, we introduce a db.relationship() - A function that signifies the relationship between two models
      #- we also describe the relationship using
         # 1. the Model the parent is related to
         # 2. how the child will call the parent
         # 3. how to load the data
      #- it is always advisable to place the relationship() inside the parent model for easy reference
