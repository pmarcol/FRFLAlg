"Class representing a single agent with necessary operations on it"

from tools import add_vectors

class Agent:
    "Single agent in a swarm"

    brightness = None
    coordinates = None

    def __init__(self, coords):
        "Constructor for agent with predefined coordinates"
        self.coordinates = coords

    def move_to_coords(self, coords):
        "Allows to set new coordinates for the agent"
        if len(coords) != len(self.coordinates):
            print("Number of new coordinates does not match the number of original coordinates.")
            return

        self.coordinates = coords
        return

    def move_with_vector(self, direction):
        "Allows to move the agent with defined vector"
        if len(direction) != len(self.coordinates):
            print("Number of new coordinates does not match the number of original coordinates.")
            return

        self.coordinates = add_vectors(self.coordinates,direction)
        return

    def set_brightness(self, value = None):
        "Allows to set brightness for the agent"
        if value is None:
            print("No value passed as new brightness.")
            return

        self.brightness = value
        return
    