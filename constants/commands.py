from enum import Enum
import json

class EmulatorCommand(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    SELECT = "select"
    START = "start"
    A = "a"
    B = "b"
    L = "l"
    R = "r"

def load_emulator_command_map(file_name: str):
    #"emulator_commands_map.json"
    f = open(file_name, "r")
    cmd_map = json.load(f)
    f.close()
    return cmd_map