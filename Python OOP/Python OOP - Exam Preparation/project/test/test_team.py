from unittest import TestCase, main

from project.team import Team


class TeamTests(TestCase):
    def test_init_is_initialized_correctly(self):
        team = Team('Barca')

        self.assertEqual('Barca', team.name)
        self.assertDictEqual({}, team.members)

    def test_name_with_non_alpha_char_raises(self):
        team = Team('Barca')

        with self.assertRaises(ValueError) as ex:
            team.name = "33ss"

        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member_with_new_members_only(self):
        team = Team('Barca')

        self.assertDictEqual({}, team.members)

        result = team.add_member(Ivan=22, Gogo=22)
        expected_result = "Successfully added: Ivan, Gogo"

        self.assertEqual(expected_result, result)
        self.assertDictEqual({"Ivan": 22, "Gogo": 22}, team.members)

    def test_add_member_with_existing_member(self):
        team = Team('Barca')

        self.assertDictEqual({}, team.members)

        team.add_member(Ivan=22, Gogo=22)
        result = team.add_member(Ivan=50)
        expected_result = "Successfully added: "

        self.assertEqual(expected_result, result)
        self.assertDictEqual({"Ivan": 22, "Gogo": 22}, team.members)

    def test_remove_existing_member_returns_correct_message(self):
        team = Team('Barca')

        team.add_member(Ivan=22, Gogo=22)

        result = team.remove_member("Ivan")
        expected_result = "Member Ivan removed"

        self.assertEqual(expected_result, result)
        self.assertDictEqual({"Gogo": 22}, team.members)

    def test_remove_non_existing_member_returns_correct_message(self):
        team = Team('Barca')

        team.add_member(Ivan=22, Gogo=22)

        result = team.remove_member("Peter")
        expected_result = "Member with name Peter does not exist"

        self.assertEqual(expected_result, result)
        self.assertDictEqual({"Ivan": 22, "Gogo": 22}, team.members)

    def test_self_gt_other_method_returns_correct_bool(self):
        team = Team('Barca')
        team2 = Team('Real')

        team.add_member(Ivan=22, Gogo=22)

        result = team > team2

        self.assertTrue(result)

    def test_other_gt_self_method_returns_correct_bool(self):
        team = Team('Barca')
        team2 = Team('Real')

        team2.add_member(Ivan=22, Gogo=22)

        result = team > team2

        self.assertFalse(result)

    def test_len_method_returns_correct_length_of_members_dict(self):
        team = Team('Barca')

        team.add_member(Ivan=22, Gogo=22)

        result = len(team)
        expected_result = 2

        self.assertEqual(expected_result, result)

    def test_add_method_returns_new_instance_correctly(self):
        team = Team('Barca')
        team2 = Team('Real')

        team.add_member(Peter=22, Tony=22)
        team2.add_member(Ivan=22, Gogo=22)

        team3 = team + team2

        self.assertEqual("BarcaReal", team3.name)
        self.assertDictEqual({"Peter": 22, "Tony": 22, "Ivan": 22, "Gogo": 22}, team3.members)

    def test_str_method_returns_correct_message(self):
        team = Team('Barca')

        team.add_member(Peter=22, Tony=22)

        result = str(team)
        expected_result = "Team name: Barca\n" \
                          "Member: Peter - 22-years old\n" \
                          "Member: Tony - 22-years old"

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
