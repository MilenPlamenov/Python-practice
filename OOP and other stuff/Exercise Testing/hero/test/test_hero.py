from project.hero import Hero
from unittest import TestCase, main


class HeroTest(TestCase):
    def setUp(self):
        self.hero = Hero("Gosho", 10, 100, 50)

    def test_create_hero_object(self):
        self.assertEqual("Gosho", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(50, self.hero.damage)

    def test_battle_with_same_hero_object(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_already_dead_hero(self):
        enemy_hero = Hero("Pesho", 5, 100, 50)
        self.hero.health -= 101
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_already_dead_enemy(self):
        enemy_hero = Hero("Pesho", 5, 0, 50)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        enemy_hero = Hero("Pesho", 5, 100, 50)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(result, "Draw")

    def test_battle_when_our_hero_wins(self):
        enemy_hero = Hero("Pesho", 5, 1, 2)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(result, "You win")
        self.assertEqual(11, self.hero.level)
        self.assertEqual(95, self.hero.health)
        self.assertEqual(55, self.hero.damage)

    def test_battle_when_our_hero_lose(self):
        enemy_hero = Hero("Pesho", 5, 1000, 30)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(result, "You lose")
        self.assertEqual(6, enemy_hero.level)
        self.assertEqual(505, enemy_hero.health)
        self.assertEqual(35, enemy_hero.damage)

    def test_str_method(self):
        actual = str(self.hero)
        expected = f"Hero Gosho: 10 lvl\n" \
                   f"Health: 100\n" \
                   f"Damage: 50\n"

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()
