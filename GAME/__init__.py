class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def take_damage(self, incoming_damage):
        effective_damage = max(incoming_damage - self.armor, 0)
        self.health -= effective_damage
        return effective_damage

    def is_alive(self):
        return self.health > 0


class Player(Person):
    def attack(self, enemy):
        print(f"Игрок атакует врага на {self.damage} урона.")
        damage_dealt = enemy.take_damage(self.damage)
        print(f"Враг получил {damage_dealt} урона. У врага осталось {enemy.health} здоровья.")


class Enemy(Person):
    def attack(self, player):
        print(f"Враг атакует игрока на {self.damage} урона.")
        damage_dealt = player.take_damage(self.damage)
        print(f"Игрок получил {damage_dealt} урона. У игрока осталось {player.health} здоровья.")


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        turn = 0  # 0 - игрок, 1 - враг
        while self.player.is_alive() and self.enemy.is_alive():
            if turn == 0:
                self.player.attack(self.enemy)
                turn = 1
            else:
                self.enemy.attack(self.player)
                turn = 0

        if self.player.is_alive():
            print("Игрок победил!")
        else:
            print("Враг победил!")


# Создаем экземпляры классов
player = Player(health=100, damage=20, armor=5)
enemy = Enemy(health=100, damage=15, armor=6)

# Запускаем игру
game = Game(player, enemy)
game.start_battle()