#!/usr/bin/python

import json
import sys

def loadFromJson(filename):
	global alphabet, states, initial_state, final_states, transitions
	with open(filename) as f:
		data = json.load(f)
	alphabet = data["alphabet"]
	states = data["states"]
	initial_state = data["initial_state"]
	final_states = data["final_states"]
	transitions = data["transitions"]

def process_string(input_string, starting_state):
	global alphabet, states, initial_state, final_states, transitions
	if len(input_string) == 0:
		return starting_state in final_states
	if process_string(input_string[1:], transitions[starting_state][input_string[0]]):
		return True
	return False




if len(sys.argv) > 1:
	loadFromJson(sys.argv[1])
else:
	print("Must specify dfa file")

if len(sys.argv) > 2:
	input_string = sys.argv[2]
else:
	input_string = "11001011001101101"


if process_string(input_string, initial_state):
	print("accepted")
else:
	print("rejected")
