#!/usr/bin/python

import json

def loadFromJson(filename):
	global alphabet, stack_alphabet, states, initial_state, start_symbol, final_states, transitions
	with open(filename) as f:
		data = json.load(f)
	alphabet = data["alphabet"]
	stack_alphabet = data["stack_alphabet"]
	states = data["states"]
	initial_state = data["initial_state"]
	start_symbol = data["start_symbol"]
	final_states = data["final_states"]
	transitions = data["transitions"]



def process_string(input_string, starting_state, stack):
	global alphabet, stack_alphabet, states, initial_state, start_symbol, final_states, transitions
	
	print(input_string)
	print(starting_state)
	print(stack)
	
	current_nodes = []
	starting_node = {}
	starting_node["state"] = starting_state
	starting_node["stack"] = stack
	starting_node["input_string"] = input_string
	current_nodes.append(starting_node)
	
	while(True):
		next_nodes = []
		for node in current_nodes:
			print(input_string)
			print(starting_state)
			print(stack)
			input_string = node["input_string"]
			stack = node["stack"]
			starting_state = node["state"]
			if (len(input_string) > 0) and (starting_state in transitions.keys()) and (input_string[0] in transitions[starting_state].keys()) and (stack[-1] in transitions[starting_state][input_string[0]].keys()):
				stack_top = stack[-1]
				for transition in transitions[starting_state][input_string[0]][stack_top]:
					new_state = transition[0]
					if(transition[1] == "e"):
						new_top_symbol = ""
					else:
						new_top_symbol = transition[1]
					new_node = {}
					new_node["input_string"] = input_string[1:]
					new_node["state"] = new_state
					new_node["stack"] = stack[:-1] + new_top_symbol
					next_nodes.append(new_node)
			elif (starting_state in final_states) and (len(input_string) == 0):
				print(input_string)
				print(starting_state)
				print(stack)
				return True		# ended in an accepting state
			
			# epsilon transforms
			if (starting_state in transitions.keys()) and ("e" in transitions[starting_state].keys()):
				stack_top = stack[-1]
				if(not stack_top in transitions[starting_state]["e"].keys()):
					continue
				for transition in transitions[starting_state]["e"][stack_top]:
					new_state = transition[0]
					if(transition[1] == "e"):
						new_top_symbol = ""
					else:
						new_top_symbol = transition[1]
					new_node = {}
					new_node["input_string"] = input_string
					new_node["state"] = new_state
					new_node["stack"] = stack[:-1] + new_top_symbol
					next_nodes.append(new_node)
		if(next_nodes == []):
			return False	# nowhere left to go
		current_nodes = next_nodes


loadFromJson("sample_pda.json")	# sample PDA is PDA for even-length palindrome
#loadFromJson("testing_pda.json")	# sample PDA is designed to have an infinite loop.
if process_string("101001100101", initial_state, start_symbol):
	print ("accepted")
else:
	print("rejected")



