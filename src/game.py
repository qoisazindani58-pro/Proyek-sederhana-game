from src.character import Hero, Monster


class Game:
    """Mengatur alur permainan dan interaksi antarobjek."""

    def __init__(self):
        self.hero = None
        self.monsters = [
            Monster("Goblin", health=35, attack_power=8, reward_xp=10),
            Monster("Orc", health=55, attack_power=12, reward_xp=20),
            Monster("Naga Kecil", health=75, attack_power=15, reward_xp=30),
        ]
        self.total_xp = 0

    def start(self) -> None:
        print("=" * 42)
        print("       PETUALANGAN DUNGEON")
        print("=" * 42)
        name = input("Masukkan nama hero: ").strip() or "Pahlawan"
        self.hero = Hero(name)
        print(f"\nSelamat datang, {self.hero.name}!")
        print("Kalahkan 3 monster untuk menyelesaikan dungeon.\n")

        for monster in self.monsters:
            if not self.hero.is_alive:
                break
            self.battle(monster)

        self.show_result()

    def battle(self, monster: Monster) -> None:
        print(f"\n--- MUSUH MUNCUL: {monster.name} ---")
        while self.hero.is_alive and monster.is_alive:
            print(f"\n{self.hero.name}: {self.hero.health} HP | "
                  f"{monster.name}: {monster.health} HP")
            print("1. Serang")
            print("2. Gunakan potion (+30 HP)")
            print("3. Lihat status")
            choice = input("Pilih aksi: ").strip()

            if choice == "1":
                self.hero.attack(monster)
            elif choice == "2":
                self.hero.use_potion()
            elif choice == "3":
                self.show_status()
                continue
            else:
                print("Pilihan tidak valid. Pilih 1, 2, atau 3.")
                continue

            if monster.is_alive:
                monster.attack(self.hero)

        if self.hero.is_alive:
            self.total_xp += monster.reward_xp
            print(f"\n{monster.name} berhasil dikalahkan! "
                  f"+{monster.reward_xp} XP.")

    def show_status(self) -> None:
        print("\n===== STATUS HERO =====")
        print(f"Nama       : {self.hero.name}")
        print(f"HP         : {self.hero.health}/100")
        print(f"Attack     : {self.hero.attack_power}")
        print(f"Potion     : {self.hero.potions}")
        print(f"Total XP   : {self.total_xp}")
        print("=======================\n")

    def show_result(self) -> None:
        print("\n========== HASIL PERMAINAN ==========")
        if self.hero.is_alive:
            print("SELAMAT! Kamu berhasil menaklukkan dungeon.")
            print(f"Total XP diperoleh: {self.total_xp}")
        else:
            print("GAME OVER! Hero kehabisan HP.")
            print(f"Total XP sebelum kalah: {self.total_xp}")
        print("Terima kasih sudah bermain!")
        print("=====================================")
