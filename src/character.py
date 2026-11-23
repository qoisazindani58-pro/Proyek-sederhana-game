from abc import ABC, abstractmethod


class Character(ABC):
    """Kelas abstrak untuk semua karakter dalam permainan."""

    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self._health = health
        self.attack_power = attack_power

    @property
    def health(self) -> int:
        """Encapsulation: health dibaca melalui property."""
        return self._health

    @property
    def is_alive(self) -> bool:
        return self._health > 0

    def take_damage(self, damage: int) -> None:
        damage = max(0, damage)
        self._health = max(0, self._health - damage)
        print(f"{self.name} menerima {damage} damage. HP tersisa: {self._health}")

    @abstractmethod
    def attack(self, target: "Character") -> None:
        """Setiap jenis karakter wajib memiliki cara menyerang sendiri."""
        raise NotImplementedError


class Hero(Character):
    def __init__(self, name: str):
        super().__init__(name, health=100, attack_power=22)
        self.potions = 2
        self.level = 1

    def attack(self, target: Character) -> None:
        print(f"{self.name} menebas {target.name}!")
        target.take_damage(self.attack_power)

    def use_potion(self) -> None:
        if self.potions <= 0:
            print("Potion kamu habis!")
            return
        if self.health >= 100:
            print("HP kamu sudah penuh.")
            return
        self._health = min(100, self._health + 30)
        self.potions -= 1
        print(f"Potion digunakan. HP sekarang {self.health}. Sisa potion: {self.potions}")


class Monster(Character):
    def __init__(self, name: str, health: int, attack_power: int, reward_xp: int):
        super().__init__(name, health, attack_power)
        self.reward_xp = reward_xp

    def attack(self, target: Character) -> None:
        print(f"{self.name} menyerang {target.name}!")
        target.take_damage(self.attack_power)
