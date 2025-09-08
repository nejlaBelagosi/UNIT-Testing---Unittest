import re


class Person():
    def set_person(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old."


class Student():
    def set_student(self, student_name, student_age):
        self.name = student_name
        self.age = student_age

    def greet(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old."


def is_element_in_list(n1, n2):
    list = []
    for i in range(n1, n2 + 1):
        list.append(i)
    print(list)
    return list


def djeljivi_sa_2(lista):
    rezultat = {broj for broj in lista if broj % 2 == 0}
    return rezultat


def contains_phone_number(text):
    """
    Provjerava da li tekst sadrži broj telefona u formatu +XXX-XX-XXX-XXX.
    """
    phone_pattern = r'\+\d{3}-\d{2}-\d{3}-\d{3}'
    match = re.search(phone_pattern, text)
    return match.group(0) if match else None
