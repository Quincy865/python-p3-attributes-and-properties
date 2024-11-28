#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", 
    "Pug", "Pointer"
]

class Dog:
    def __init__(self, name, breed=None):
        # Validate the name
        if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            self.name = None  # Set to None if name is invalid
        else:
            self.name = name
        
        # Validate the breed if provided
        if breed and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self.breed = None  # Set to None if breed is invalid
        else:
            self.breed = breed
