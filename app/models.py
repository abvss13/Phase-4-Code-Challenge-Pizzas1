from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heros'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,nullable=False)
    super_name=db.Column(db.String)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,onupdate=db.func.now())

    hero_powers = db.relationship('HeroPowers', back_populates='hero')

   
    def __repr__(self):
        return f'<Hero {self.name} {self.super_name}>'
    
class HeroPowers(db.Model):
     __tablename__='hero_powers'
     id = db.Column(db.Integer, primary_key=True)
     strength=db.Column(db.String,nullable=False)
     hero_id=db.Column(db.Integer,db.ForeignKey('heros.id'))
     power_id=db.Column(db.Integer,db.ForeignKey('powers.id'))
     created_at=db.Column(db.DateTime,server_default=db.func.now())
     updated_at=db.Column(db.DateTime,onupdate=db.func.now())

     


        
    #defining the relationships
     hero = db.relationship('Hero', back_populates='hero_powers')
     power = db.relationship('Power', back_populates='hero_powers')
    #validation for the strength
     @validates('strength')
     def validate_strength(self,key,strength):
            valid_strengths = ['Strong', 'Weak', 'Average']
            if strength not in valid_strengths:
                raise ValueError(f"Strength must be one of: {', '.join(valid_strengths)}")

            return strength
        
     def __repr__(self):
            return f'<Heropowers {self.strength} >'
        
class Power(db.Model):
     __tablename__='powers'
     id = db.Column(db.Integer, primary_key=True)
     name=db.Column(db.String,nullable=False)
     description=db.Column(db.String,nullable=False)
     created_at=db.Column(db.DateTime,server_default=db.func.now())
     updated_at=db.Column(db.DateTime,onupdate=db.func.now())

    
     hero_powers = db.relationship('HeroPowers', back_populates='power')
#validation for the description
     @validates('description')
     def validate_description(self,key,description):
      if len(description) < 20:
         raise ValueError('description must be greater than 20 characters')
      return description
    

     def __repr__(self):
        return f'<power {self.name} {self.description}>'
    


