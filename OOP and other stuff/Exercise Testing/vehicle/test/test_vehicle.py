from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 500)

    def test_create_vehicle(self):
        self.assertEqual(50.0, self.vehicle.fuel)
        self.assertEqual(500.0, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
        self.assertEqual(50, self.vehicle.capacity)

    def test_drive_with_proper_data(self):
        self.vehicle.drive(15)
        self.assertEqual(31.25, self.vehicle.fuel)

    def test_drive_with_incorrect_data(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_proper_data(self):
        self.vehicle.drive(15)
        self.vehicle.refuel(10)
        self.assertEqual(41.25, self.vehicle.fuel)

    def test_refuel_with_incorrect_data(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method(self):
        result = str(self.vehicle)
        excepted = "The vehicle has 500 horse power with 50 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    main()
