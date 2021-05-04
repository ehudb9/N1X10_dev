"""
Constants for documets expressions
"""

__name__ = "constants"
__author__ = "Ehud Barda"

import json
import logging
import os

import utils.log
# DOC_INDEXES_EXP = {}
patient_name = [],

date_of_document = [],

date_of_procedure = [],

doctor_name = [],

department= [],

institution = [],

procedure_type = {

                 },

num_of_pages = 0,

document_reference = ""












# application related.
HOST_IP = '127.0.0.1'
PORT = 5000
UPLOAD_FOLDER_NAME = "export_files"
SCORE_FILE_NAME = "bud_statistics.xlsx"
CONFIG_FILE_NAME = "config.json"
TRANS_PROTOCOL = "tcp"

# robot related.
NUM_PILLARS = 4
BLANK_LETTER_POSITION = 2048
JOINT_MAX_VALUE = 4095
FULL_TURN = 4096
FIFTH_OF_A_TURN = 819
THRESHOLD_FOR_LETTER_CORRECT = 409
PULL_LIMIT = 1900

# registers & values.
SLOW_MOVING_SPEED = '15'
MAX_MOVING_SPEED = '0'
MODERATE_MOVING_SPEED = '30'
GOAL_POSITION_REGISTER = 'goal-position'
MOVING_SPEED_REGISTER = 'moving-speed'
GOAL_ACCELERATION_REGISTER = 'goal-acceleration'

# motor names.
LEAN_ONE = "leanone"
LEAN_TWO = "leantwo"
LEAN_THREE = "leanthree"
LEAN_FOUR = "leanfour"
TURN_ONE = "turnone"
TURN_TWO = "turntwo"
TURN_THREE = "turnthree"
TURN_FOUR = "turnfour"
# The pillars will counts from left to right
dict_pillars = {
    "3" : { "lean": LEAN_ONE, "turn": TURN_ONE},
    "2" : { "lean": LEAN_TWO, "turn": TURN_TWO},
    "1": { "lean": LEAN_THREE, "turn": TURN_THREE},
    "0": { "lean": LEAN_FOUR, "turn": TURN_FOUR}
} 
motor_turn_names = ["turnone", "turntwo", "turnthree", "turnfour"]
motor_lean_names = ["leanone", "leantwo", "leanthree", "leanfour"]

# responses.
UNKNOWN_MOTOR_POSITION = "Unknown motor position response when reading motor"

# logger's min level.
LOG_LEVEL = "DEBUG"

# initialize logger in global scope.
LOGGER = setup_project_logger(LOG_LEVEL, 'root')
