from unittest import TestCase, main

from projects.worker import Worker


class WorkerTest(TestCase):
    def test_init_is_initialized_correctly(self):
        worker = Worker("Ivan", 100, 100)

        self.assertEqual("Ivan", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_work_with_zero_energy_raises(self):
        worker = Worker("Ivan", 100, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_with_negative_energy_raises(self):
        worker = Worker("Ivan", 100, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_money_is_increased_correctly_after_work(self):
        worker = Worker("Ivan", 100, 100)

        self.assertEqual(0, worker.money)

        worker.work()

        self.assertEqual(100, worker.money)

        worker.work()

        self.assertEqual(200, worker.money)

    def test_work_energy_is_decreased_correctly_after_work(self):
        worker = Worker("Ivan", 100, 100)

        self.assertEqual(100, worker.energy)

        worker.work()

        self.assertEqual(99, worker.energy)

        worker.work()

        self.assertEqual(98, worker.energy)

    def test_rest_energy_is_increased_correctly_after_rest(self):
        worker = Worker("Ivan", 100, 100)

        self.assertEqual(100, worker.energy)

        worker.rest()

        self.assertEqual(101, worker.energy)

        worker.rest()

        self.assertEqual(102, worker.energy)

    def test_get_info_working_correctly(self):
        worker = Worker("Ivan", 100, 100)

        expected_result = 'Ivan has saved 0 money.'
        result = worker.get_info()

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
