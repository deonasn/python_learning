# Deon Anoth
# 06-29-2024
# Python Crash Course: Try it yourself: 8-16

# The commented lines are the additional lines from the question to showcase 'import' options.

# importing functions from a module (different file)
#import printing_functions
import printing_functions as pf
#from printing_functions import print_models
#from printing_functions import show_completed_models as scm
#from printing_functions import *

# list containing unprinted designs and an empty list for the completed models
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# function calls from the imported module
#printing_functions.print_models(unprinted_designs[:], completed_models)
#printing_functions.show_completed_models(completed_models)
pf.print_models(unprinted_designs[:], completed_models)
pf.show_completed_models(completed_models)
#print_models(unprinted_designs[:], completed_models)
#scm(completed_models)

# printing the list at the end for checking
print("\nunprinted_designs: ", unprinted_designs)
print("completed_models: ", completed_models)