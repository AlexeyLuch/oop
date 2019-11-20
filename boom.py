import random
class GameObject():
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 0
        self.position = (0, 0)

    def __repr__(self):
        return "<%s Level: %s, Country: %s, Health: %s>" % (self.name, self.level, self.race, self.health)

    def level_up(self):
        if self.level > 10:
            self.level += 1

class Bmp(GameObject):

    def __init__(self, name, level, race):
        super().__init__(name, level, race)
        self.health = 100
        self.bullet = 300


    # Selects random coortinates

    def move(self):
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        print("Hero %s start moving to %s, %s" % (self.name, x, y))
        return (x, y)

    def hit_by(self, bul):
        """ Random for hit chance"""
        d = random.randint(1,3)

        if d == 2:
            self.health -= bul.get_damage()
            print(self.name, self.health, "Fucking shot")

            if self.health == 0:
                print(self.name, 'BOOM!!! We`re all dead')


    def _blow_up(self):
        print('BOOM!!! We`re all dead')

    def get_damage(self):
        return 50

class Rocket(GameObject):

    def __init__(self, name, level, race):
        super().__init__(name, level, race)
        self.health = 100
        self.bullet = 3

    # Selects random coortinates

    def move(self):
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        print("Hero %s start moving to %s, %s" % (self.name, x, y))
        return (x, y)



    def hit_by(self, bul):

        """ Random for hit chance """
        c = random.randint(1,10)

        if c == 2:
            self.health -= bul.get_damage()
            print(self.name,self.health,"Fucking shot")
            if self.health == 0:
                print(self.name, 'BOOM!!! We`re all dead')

    def get_damage(self):
        return 10

tank1 = Bmp("BMP", 12, "Germany")
rocket = Rocket("Konkurs", 7, "Ukraine")

print(tank1)
print(rocket)
tank1.level_up()

# Move until they are at one point
while rocket.move() != tank1.move():
    rocket.move()
    tank1.move()

#
while tank1.health or rocket.health >=0:
    tank1.hit_by(rocket)
    if tank1.health <= 0:
        break
    rocket.hit_by(tank1)
    if rocket.health <= 0:
        break

# tank1.show_hero()