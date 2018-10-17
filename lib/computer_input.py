import random

options = { 0: "r", 1: "p", 2: "s" }

def read_choice():
   random.seed()
   option = random.randint(0, 2)
   return options[option]
