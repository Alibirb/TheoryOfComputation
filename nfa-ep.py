#!/usr/bin/python

import json

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
			
	if len(input_string) > 0:
		for state in transitions[starting_state][input_string[0]]:
			if process_string(input_string[1:], state):
				return True
	elif starting_state in final_states:
		return True		# ended in an accepting state
			
	# epsilon transforms
	if("e" in transitions[starting_state].keys()):
		for state in transitions[starting_state]["e"]:
			if process_string(input_string, state):
				return True
	
	return False


loadFromJson("sample_nfa-ep.json")
if process_string("000011", initial_state):
	print ("accepted")
else:
	print("rejected")
