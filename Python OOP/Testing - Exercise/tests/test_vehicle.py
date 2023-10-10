from unittest import TestCase, main

from projects.vehicle import Vehicle


class VehicleTests(TestCase):
    def test_init_is_initialized_correct(self):
        car = Vehicle(10, 20)

        self.assertEqual(10, car.fuel)
        self.assertEqual(10, car.capacity)
        self.assertEqual(20, car.horse_power)
        self.assertEqual(1.25, car.fuel_consumption)

    def test_drive_needed_fuel_more_than_fuel_amount_raises(self):
        car = Vehicle(10, 20)

        with self.assertRaises(Exception) as ex:
            car.drive(10)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_possible_kilometers_given(self):
        car = Vehicle(10, 20)

        car.drive(2)

        expected_result = 10 - (1.25 * 2)

        self.assertEqual(expected_result, car.fuel)

    def test_refuel_if_added_amount_more_than_fuel_capacity_raises(self):
        car = Vehicle(10, 20)

        with self.assertRaises(Exception) as ex:
            car.refuel(2)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_add_max_possible_fuel_amount(self):
        car = Vehicle(10, 20)
        self.assertEqual(10, car.fuel)
        car.drive(2)
        self.assertEqual(7.5, car.fuel)

        car.refuel(2.5)

        self.assertEqual(10, car.fuel)

    def test_str_method_working_correctly(self):
        car = Vehicle(10, 20)

        expected_result = "The vehicle has 20 horse power with 10 fuel left and 1.25 fuel consumption"
        result = str(car)

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
