# Deon Anoth
# 08-18-2024
# Python Crash Course: Try it yourself: 9-12

import admin_privileges_class_module as apcm

# creating an instance of Admin class while storing privileges in a list and calling method to display said privileges
admin = apcm.Admin("Deon", "Anoth", "dafb9", "dafb9@umsystem.edu", "Iwantabetterfuture1")
admin.privileges.privileges = ["can add post", "can delete post", "can ban user"]
admin.privileges.show_privileges()