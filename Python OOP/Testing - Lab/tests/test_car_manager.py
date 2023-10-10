from unittest import TestCase, main

from projects.car_manager import Car


class CarTests(TestCase):
    def test_init_is_initialized_correctly(self):
        car = Car("Boo", "Audi", 2, 10)

        self.assertEqual("Boo", car.make)
        self.assertEqual("Audi", car.model)
        self.assertEqual(2, car.fuel_consumption)
        self.assertEqual(10, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_make_setter_if_empty_value_raises(self):
        car = Car("Boo", "Audi", 2, 10)

        with self.assertRaises(Exception) as ex:
            car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_if_empty_value_raises(self):
        car = Car("Boo", "Audi", 2, 10)

        with self.assertRaises(Exception) as ex:
            car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_if_zero_raises(self):
        car = Car("Boo", "Audi", 2, 10)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_setter_if_negative_raises(self):
        car = Car("Boo", "Audi", 2, 10)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_if_zero_raises(self):
        car = Car("Boo", "Audi", 2, 10)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_if_negative_raises(self):
        car = Car("Boo", "Audi", 2, 10)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_if_negative_raises(self):
        car = Car("Boo", "Audi", 2, 10)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_amount_raises(self):
        car = Car("Boo", "Audi", 2, 10)

        with self.assertRaises(Exception) as ex:
            car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_negative_amount_raises(self):
        car = Car("Boo", "Audi", 2, 10)

        with self.assertRaises(Exception) as ex:
            car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_valid_amount(self):
        car = Car("Boo", "Audi", 2, 10)

        car.refuel(112)

        self.assertEqual(10, car.fuel_amount)
        self.assertEqual(10, car.fuel_capacity)

    def test_drive_with_impossible_distance_to_reach_raises(self):
        car = Car("Boo", "Audi", 2, 10)

        with self.assertRaises(Exception) as ex:
            car.drive(10)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_possible_distance_to_reach(self):
        car = Car("Boo", "Audi", 2, 10)

        # fuel_amount = 0 (by default)
        self.assertEqual(0, car.fuel_amount)

        # then we increase the amount with 28
        # but the max fuel_capacity is 10 so 28 becomes 10
        # you can try to fill it up with 100000 but in the end the fuel_capacity will become 10 every time (10 is max)
        # but if you try to fill it up with fuel between 1 and 9 the fuel_capacity will become between 1 and 9
        # when you try to fill it with negative or zero amount raises an error
        car.refuel(28)
        self.assertEqual(10, car.fuel_amount)

        # then we drive TWICE just to be sure the fuel_amount is decreased correct

        car.drive(100)
        # needed = (distance / 100) * fuel_consumption
        # needed = (100 / 100) * 2
        # needed = 2
        # fuel_amount -= needed
        # 10 -= 2
        # car.fuel_amount = 8
        self.assertEqual(8, car.fuel_amount)

        car.drive(100)
        # needed = (distance / 100) * fuel_consumption
        # needed = (100 / 100) * 2
        # needed = 2
        # fuel_amount -= needed
        # 8 -= 2
        # car.fuel_amount = 6
        self.assertEqual(6, car.fuel_amount)


if __name__ == "__main__":
    main()
