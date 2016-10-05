__author__ = 'B. Furtado'


import subprocess


for index in range(len([True, False])):
    # Call the main.py module
    subprocess.call("python main.py %s" % index, shell=False)

