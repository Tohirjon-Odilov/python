"""U9"""
from os import system
from time import sleep


class Person:
    def __init__(self, first_name: str, last_name: str, birth_date: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def get_info(self):
        return f"""
First name: {self.first_name}
Last name: {self.last_name}
Birth date: {self.birth_date}"""


class Student(Person):
    def __init__(
        self, first_name: str, last_name: str, birth_date: str, faculty: str, level: int
    ) -> None:
        super().__init__(first_name, last_name, birth_date)
        self.faculty = faculty
        self.level = level
        self.subjects = []

    def get_info(self):
        return f"""{super().get_info()}    
Faculty: {self.faculty}
Level: {self.level}
Subjects: {self.to_str()}"""

    def add_subject(self, addaction_subjects):
        check = 0
        for subject in self.subjects:
            if subject.subject == addaction_subjects.subject:
                check += 1
        if not check:
            self.subjects.append(addaction_subjects)
            return f"\033[1;36mAdded successfully\033[1;0m"
        else:
            return f"\033[1;31mThis subject already\033[1;0m"

    def remove_subject(self, removed_subject):
        if removed_subject in self.subjects:
            self.subjects.remove(removed_subject)
            return "\033[1;36mDeleted successfully\033[1;0m"
        else:
            return "\033[1;31mInvalid Subject\033[1;0m"

    def to_str(self):
        all_subjects = str()
        for i in self.subjects:
            all_subjects += i.subject + ", "
        return all_subjects[:-2]


class Subjects:
    def __init__(self, subject):
        self.subject = subject


student1 = Student("Holid", "Yusupov", "12.23.2000", "Kiber injinering", 3)
subject1 = Subjects("Tarix")
print(student1.add_subject(subject1))
sleep(0.3)
subject2 = Subjects("Ona tili")
print(student1.add_subject(subject2))
sleep(0.3)
subject3 = Subjects("Matematika")
print(student1.add_subject(subject3))
sleep(0.3)
subject4 = Subjects("Geografiya")
print(student1.add_subject(subject4))
sleep(0.3)
subject5 = Subjects("Ingiliz tili")
print(student1.add_subject(subject5))
sleep(0.3)
subject6 = Subjects("Ingiliz tili")
print(student1.add_subject(subject6))
sleep(0.3)
print(student1.remove_subject(subject6))
sleep(0.3)
print(student1.remove_subject(subject1))
sleep(0.3)
system("clear")

print(student1.get_info())
