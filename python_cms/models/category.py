from sqlalchemy import Integer, String
from python_cms.db import BaseModel, db
from sqlalchemy.orm import mapped_column, relationship

class CategoryModel(BaseModel):
    __tablename__ = 'category'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(80), nullable=False)
    
    
    posts = relationship("PostModel", back_populates="category")

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get(cls, category_id):
        return cls.query.filter_by(id=category_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()