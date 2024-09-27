# import this
# Python enhancement proposals - PEP 20

# import random
# import math
# from random import random
# import os
#
#
#
#
# print(random())
# print(random.randrange(1,10))

# import os
# returns our current working directory

# working_directory = os.getcwd()
# print(f"Current working directory: {working_directory}")
#
# username = os.environ.get('USERNAME') or os.environ.get('USER')
# print(f"The current user is: {username}")
#
# cpu_cores = os.cpu_count()
# print(f'Total CPU cores: {cpu_cores}')

# change directory - must exist
# os.chdir("<folder_name>")

# make a new directory
# os.mkdir("folder_name")

# import datetime
# gives us today's date
# print(f"Today's date: {datetime.date.today()}")

# import builtins
# for name in dir(builtins):
#     if name[0].islower():
#         print(name)