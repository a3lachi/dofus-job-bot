import pyautogui 
import random
import time
import math
import heapq
import numpy as np
import screeninfo
from PIL import Image, ImageGrab, ImageFilter, ImageOps, ImageEnhance
import pytesseract
import matplotlib.pyplot as plt
import cv2
import itertools
from config import *

class PathFinder:
    """
    A class that finds a sortest path in dofus from a start map position to a target map position 
    Used method: Nearest neighbors with manhattan distance to simulate movement in dofus (RIGHT, LEFT, UP, DOWN)
    
    """
    def __init__(self):
        pass
    
    def manhattan_distance(self, start: list, target: list):
        pass
    
    def shortest_path_nearest_neighbors(self):
        pass
    
    
    
"""
def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def nearest_neighbor(coords):
    visited = [False] * len(coords)
    path = [0] * len(coords)
    current = 0
    visited[current] = True
    for i in range(1, len(coords)):
        nearest_dist = float('inf')
        nearest_index = -1
        for j in range(len(coords)):
            if not visited[j]:
                dist = manhattan_dist(coords[current], coords[j])
                if dist < nearest_dist:
                    nearest_dist = dist
                    nearest_index = j
        visited[nearest_index] = True
        path[i] = nearest_index
        current = nearest_index
    return [coords[i] for i in path]
"""