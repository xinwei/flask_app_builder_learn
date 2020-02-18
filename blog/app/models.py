from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey,Text,Date
from sqlalchemy.orm import relationship

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
class Article(Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    keys = Column(String(50))
    context = Column(Text)
    date = Column(Date)
    def __repr__(self):
     return self.name