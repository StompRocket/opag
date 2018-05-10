import base64
import sys

path = sys.argv[1]

try:
	readPath = open(path)
except FileNotFoundError as e:
	print("Specified file was not found, please specify it as the first parameter")