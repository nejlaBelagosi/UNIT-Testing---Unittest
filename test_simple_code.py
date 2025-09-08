import unittest

from simple_code import is_element_in_list, Person, Student, djeljivi_sa_2, contains_phone_number


class TestMyFunctions(unittest.TestCase):

    def test_my_class(self):
        object_name = Person()
        message = "given object is not instance of Student."
        self.assertIsInstance(object_name, Student, message)

    def test_is_element_in_list(self):
        print("Testiranje da li se element nalazi u listi:")
        element = is_element_in_list(0, 10)
        self.assertIn(34, element)

    def test_neuspjesan(self):
        brojevi = [1, 2, 3, 4, 5, 6]
        ocekivani_skup = {1, 2, 4}
        self.assertSetEqual(djeljivi_sa_2(brojevi), ocekivani_skup)

    def test_contains_phone_number_failure(self):
        text = "+38761123456"  #Nevalidan format
        result = contains_phone_number(text)
        self.assertRegex(result, r'^\+\d{3}-\d{2}-\d{3}-\d{3}$')


if __name__ == '__main__':
    unittest.main()
