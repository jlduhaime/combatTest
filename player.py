import sys
import pygame as pg

class Player:
    def __init__(self, name):
        print("Creating player " + name + "...")
        self.name = name
        