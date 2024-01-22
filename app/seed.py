from random import randint,choice as rc
import random
from faker import Faker

from app import app
from models import db,Power,Hero,HeroPowers

fake=Faker()

with app.app_context():
    #clearing the existing data
    HeroPowers.query.delete()
    Hero.query.delete()
    Power.query.delete()

#seeding hero
    heros=[] #empty list to store the heros
    for i in range(10):
        b=Hero(name=fake.name(),
                     super_name=fake.name())
        heros.append(b)
    
    db.session.add_all(heros)
    db.session.commit()
    
    #seeding powers
    powers = []
    power_data = [
            ('Super Strength', 'This power grants immense physical strength.'),
            ('Flight', 'The ability to soar through the skies at will.'),
            ('Telekinesis', 'Move objects with the power of your mind.'),
            ('Invisibility', 'Become invisible to the naked eye.'),
            ('X-ray Vision', 'See through solid objects.'),
            ('Fire Manipulation', 'Control and create fire at your will.'),
            ('Ice Control', 'Command the power of ice and cold.'),
            ('Time Travel', 'Travel through time and alter the past or future.'),
            ('Teleportation', 'Instantly transport yourself to any location.'),
            ('Mind Reading', 'Read the thoughts of others with ease.'),
        ]

    for name, description in power_data:
            power = Power(
                name=name,
                description=description,
            )
            powers.append(power)

    db.session.add_all(powers)
    db.session.commit()


 #seeding heropowers
    heropowers=[] #empty list to store the heropowers
    strength_names=['Strong', 'Weak', 'Average']


    for i in range(10):
        hero=rc(heros)
        power=rc(powers)
        b=HeroPowers(strength = random.choice(strength_names),hero=hero,power=power)
        heropowers.append(b)
    
    db.session.add_all(heropowers)
    db.session.commit()
    
    print('seeding completed ')