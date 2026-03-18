from random import randint

class Gladiator:
    def __init__(self, name, weapon = None):
        self.name = name
        self.hp = 50 # fixing it for testing randint(80,100) 
        self.speed = randint(1,10)
        self.is_alive = 1
        self.acts_every = 11-self.speed
        self.base_damage = randint(1,2)
        self.weapon = weapon
    
    def report_speed(self):
        return f"I am {self.speed} fast"
        
    def report_hp(self):
        return f"I have {self.hp} hitpoints"
        
    def report_stats(self):
        return f"{self.report_hp()} and {self.report_speed()}"
    
    def take_damage(self, amount):
        self.hp -= amount
        
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = 0
            print(f"{self.name} has fallen!")
        
    def calculate_attack(self):
        bonus = self.weapon.bonus_damage if self.weapon else 0
        return self.base_damage + bonus
        
        
class Gladius:
    def __init__(self):
        self.name = "Gladius"
        self.bonus_damage = 5


class Arena:
    def __init__(self, fighter_1, fighter_2):
        if fighter_1.speed >= fighter_2.speed: 
            self.p1 = fighter_1
            self.p2 = fighter_2 
        else: 
            self.p1 = fighter_2
            self.p2 = fighter_1
        
        
    def do_battle(self):
        tick = 1
        while (self.p1.is_alive == 1 and self.p2.is_alive == 1) and tick <= 30:
            print(f"---Tick {tick} ---")
            attackers = []
            if tick % self.p1.acts_every == 0:
                attackers.append(self.p1)
            if tick % self.p2.acts_every == 0:
                attackers.append(self.p2)
            if len(attackers) > 0:
                attackers.sort(key = lambda x: x.speed, reverse = True)
                for attacker in attackers:
                    target = self.p2 if attacker == self.p1 else self.p1
                    
                    if attacker.is_alive == 1 and target.is_alive == 1:
                        damage = attacker.calculate_attack()
                        print(f"{attacker.name} strikes for {damage}!")
                        target.take_damage(damage)
            tick +=1
            if tick >= 31:
                print("Combat has ended indecisively")
                print(f"{self.p1.name} has {self.p1.hp} hitpoints left")
                print(f"{self.p2.name} has {self.p2.hp} hitpoints left")
                break


sword1 = Gladius()
sword2 = Gladius()
        
angry_bob = Gladiator("angry bob", sword1)
big_dave = Gladiator("big dave", sword2)

arena = Arena(angry_bob, big_dave)

arena.do_battle()

        
        