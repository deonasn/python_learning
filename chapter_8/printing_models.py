# Deon Anoth
# 06-28-2024
# Python Crash Course: Try it yourself: 8-15

# importing functions from a module (different file)
import printing_functions as pf

# list containing unprinted designs and an empty list for the completed models
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# function calls from the imported module
pf.print_models(unprinted_designs[:], completed_models)
pf.show_completed_models(completed_models)

# printing the list at the end for checking
print("\nunprinted_designs: ", unprinted_designs)
print("completed_models: ", completed_models)