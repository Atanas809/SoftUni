from unittest import TestCase, main

from projects.hero import Hero


class HeroTests(TestCase):
    def test_player_init_is_initialized_correctly(self):
        player = Hero("Tom", 10, 100, 20)

        self.assertEqual("Tom", player.username)
        self.assertEqual(10, player.level)
        self.assertEqual(100, player.health)
        self.assertEqual(20, player.damage)

    def test_enemy_init_is_initialized_correctly(self):
        enemy = Hero("Jhon", 5, 100, 10)

        self.assertEqual("Jhon", enemy.username)
        self.assertEqual(5, enemy.level)
        self.assertEqual(100, enemy.health)
        self.assertEqual(10, enemy.damage)

    def test_battle_enemy_hero_trying_to_fight_himself_raises(self):
        player = Hero("Tom", 10, 100, 20)
        enemy = Hero("Tom", 5, 100, 10)

        with self.assertRaises(Exception) as ex:
            player.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_player_health_reaches_zero_raises(self):
        player = Hero("Tom", 10, 0, 20)
        enemy = Hero("Jhon", 5, 100, 10)

        with self.assertRaises(Exception) as ex:
            player.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_player_health_negative_raises(self):
        player = Hero("Tom", 10, -1, 20)
        enemy = Hero("Jhon", 5, 100, 10)

        with self.assertRaises(Exception) as ex:
            player.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_reaches_zero_raises(self):
        player = Hero("Tom", 10, 100, 20)
        enemy = Hero("Jhon", 5, 0, 10)

        with self.assertRaises(Exception) as ex:
            player.battle(enemy)

        self.assertEqual(f"You cannot fight Jhon. He needs to rest", str(ex.exception))

    def test_battle_enemy_health_negative_raises(self):
        player = Hero("Tom", 10, 100, 20)
        enemy = Hero("Jhon", 5, -1, 10)

        with self.assertRaises(Exception) as ex:
            player.battle(enemy)

        self.assertEqual(f"You cannot fight Jhon. He needs to rest", str(ex.exception))

    def test_battle_draw_between_heroes(self):
        player = Hero("Tom", 10, 100, 20)
        enemy = Hero("Jhon", 10, 100, 15)

        self.assertEqual(100, player.health)
        self.assertEqual(100, enemy.health)

        result = player.battle(enemy)

        self.assertEqual("Draw", result)

    def test_battle_player_wins(self):
        player = Hero("Tom", 10, 100, 20)
        enemy = Hero("Jhon", 5, 100, 10)

        self.assertEqual(100, player.health)
        self.assertEqual(100, enemy.health)

        result = player.battle(enemy)
        #             self.level += 1
        #             self.health += 5
        #             self.damage += 5

        self.assertEqual("You win", result)
        self.assertEqual(11, player.level)
        self.assertEqual(55, player.health)
        self.assertEqual(25, player.damage)

    def test_battle_enemy_wins(self):
        player = Hero("Tom", 5, 100, 10)
        enemy = Hero("Jhon", 10, 100, 20)

        self.assertEqual(100, player.health)
        self.assertEqual(100, enemy.health)

        result = player.battle(enemy)
        #             self.level += 1
        #             self.health += 5
        #             self.damage += 5

        self.assertEqual("You lose", result)
        self.assertEqual(11, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(25, enemy.damage)

    def test_str_method_working_correctly(self):
        player = Hero("Tom", 5, 100, 10)

        expected_result = "Hero Tom: 5 lvl\n" \
                          "Health: 100\n" \
                          "Damage: 10\n"

        result = str(player)

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
