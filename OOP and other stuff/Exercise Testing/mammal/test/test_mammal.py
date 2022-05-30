from project.mammal import Mammal

from unittest import TestCase, main


class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal("Gosho", "Cat", "Meow")

    def test_create_mammal_object(self):
        self.assertEqual("Gosho", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("Meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_method(self):

        self.assertEqual("Gosho makes Meow", self.mammal.make_sound())

    def test_get_kingdom_method(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_method(self):
        result = self.mammal.info()
        expected_result = "Gosho is of type Cat"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
