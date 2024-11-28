#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="Unknown"):
       
        self._name = None
        self._job = None
        
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
            self._name = None
        else:
            self._name = value.title() 

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self._job = None
        else:
            self._job = value

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

person1 = Person("Alice", "Sales")
print(person1.name)
print(person1.job) 

person2 = Person("", "Doctor")  
print(person2.name) 
print(person2.job)  

person3 = Person("Bob", "Engineer") 
print(person3.name)  
print(person3.job)  

person4 = Person("VeryLongNameExceeding25Characters", "Admin")  
print(person4.name)  
print(person4.job) 